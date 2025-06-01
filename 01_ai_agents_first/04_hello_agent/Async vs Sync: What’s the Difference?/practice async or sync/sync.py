import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    openai_client=external_client,
    model="gemini-2.0-flash",
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,
)

agent : Agent = Agent(name="Assistant", instructions="You are a helpful assistant.", model=model)
result = Runner.run_sync(agent, "What is the capital of Pakistan?", run_config=config)
print(f"Result: {result.final_output}")