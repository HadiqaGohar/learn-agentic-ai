import os
from dotenv import load_dotenv
from typing import cast
import chainlit as cl
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

# Import necessary libraries for file handling
import io
import PyPDF2  # For PDF files (you might need to install: pip install PyPDF2)
import docx #For Docx files
# Load the environment variables from the .env file
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")


@cl.on_chat_start
async def start():
    #Reference: https://ai.google.dev/gemini-api/docs/openai
    external_client = AsyncOpenAI(
        api_key=gemini_api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )

    model = OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=external_client
    )

    config = RunConfig(
        model=model,
        model_provider=external_client,
        tracing_disabled=True
    )
    """Set up the chat session when a user connects."""
    # Initialize an empty chat history in the session.
    cl.user_session.set("chat_history", [])

    cl.user_session.set("config", config)
    agent: Agent = Agent(name="Assistant", instructions="You are a helpful assistant.  You can analyze uploaded files to provide solutions or answer questions related to the file content.", model=model)  # Modified instruction!
    cl.user_session.set("agent", agent)

    await cl.Message(content="Welcome to the Hadiqa Gohar's AI Assistant! How can I help you today? You can upload a file for analysis.").send()

async def process_file(file: cl.UploadedFile) -> str:
    """
    Processes the uploaded file and extracts text content.
    Supports .txt, .pdf, and .docx files.
    """
    content = file.content
    file_name = file.name
    file_extension = file_name.split(".")[-1].lower()

    try:
        if file_extension == "txt":
            text = content.decode("utf-8")
        elif file_extension == "pdf":
            pdf_file = io.BytesIO(content)
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
        elif file_extension == "docx":
            docx_file = io.BytesIO(content)
            document = docx.Document(docx_file)
            text = ""
            for paragraph in document.paragraphs:
                text += paragraph.text + "\n"
        else:
            raise ValueError(f"Unsupported file type: {file_extension}")

        return text

    except Exception as e:
        return f"Error processing file: {str(e)}"



@cl.on_message
async def main(message: cl.Message):
    """Process incoming messages and generate responses."""

    files = message.files  # Check if files were uploaded

    if files:  #If file exist in the prompt
        file = files[0] #Get the first file (handle only one for simplicity)
        # Process the file and get the text
        file_text = await process_file(file)
        if "Error processing file" in file_text: #If error exist while process the file prompt user and exit to the code
            await cl.Message(content=file_text).send()
            return
        # Append the file content to the user's message.  This is crucial!
        user_message = f"Here is the content of the file '{file.name}':\n\n{file_text}\n\nUser's question/request: {message.content}"

    else: #if file does not exist
        user_message = message.content


    # Retrieve the chat history from the session.
    history = cl.user_session.get("chat_history") or []

    # Append the user's message to the history.
    history.append({"role": "user", "content": user_message})

    # Create a new message object for streaming
    msg = cl.Message(content="")
    await msg.send()

    agent: Agent = cast(Agent, cl.user_session.get("agent"))
    config: RunConfig = cast(RunConfig, cl.user_session.get("config"))

    try:
        print("\n[CALLING_AGENT_WITH_CONTEXT]\n", history, "\n")
        # Run the agent with streaming enabled
        result = Runner.run_streamed(agent, history, run_config=config)

        # Stream the response token by token
        async for event in result.stream_events():
            if event.type == "raw_response_event" and hasattr(event.data, 'delta'):
                token = event.data.delta
                await msg.stream_token(token)

        # Append the assistant's response to the history.
        history.append({"role": "assistant", "content": msg.content})

        # Update the session with the new history.
        cl.user_session.set("chat_history", history)

        # Optional: Log the interaction
        print(f"User: {user_message}")
        print(f"Assistant: {msg.content}")

    except Exception as e:
        await msg.update(content=f"Error: {str(e)}")
        print(f"Error: {str(e)}")
