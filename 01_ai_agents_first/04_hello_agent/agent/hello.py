


import chainlit as cl
from agents import Agent, RunConfig, AsyncOpenAI, OpenAIChatCompletionsModel, Runner
from dotenv import load_dotenv, find_dotenv
import os

# Load environment variables
load_dotenv(find_dotenv())

# Step 1: Provider (no nesting)
provider = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# Step 2: Model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider,
)

# Step 3: Run Config
run_config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True,
)

# Step 4: Agent
agent1 = Agent(
    instructions="Hello! I am a Hadiqa Gohar's Agent. How can I help you?",
    name="Hadiqa Gohar Support Agent",
)

# Step 5: Runner instance
runner = Runner()

# Optional: Run once at start (just for testing)
async def test_run():
    result = await runner.run(
        input="What is the capital of Pakistan?",
        run_config=run_config,
        starting_agent=agent1,
    )
    print(result.final_output)

@cl.on_chat_start
async def handle_chat_start():   
    cl.user_session.set("history", []) 
    await cl.Message(content="Hello! I am Hadiqa Gohar's Agent. How can I help you?").send()

# Chainlit message handler
@cl.on_message
async def handle_message(message: cl.Message):
    # Run the agent on the user's message content
    result = await runner.run(
        input=message.content,
        run_config=run_config,
        starting_agent=agent1,
    )
    # Send back only the final output string
    await cl.Message(content=result.final_output).send()


