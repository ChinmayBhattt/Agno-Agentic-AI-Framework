from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGoTools()],
    markdown=True
)
agent.print_response("Who is the richest person on the planet?")
