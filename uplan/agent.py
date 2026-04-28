from google.adk.agents.llm_agent import Agent
from dotenv import load_dotenv

load_dotenv()

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)
