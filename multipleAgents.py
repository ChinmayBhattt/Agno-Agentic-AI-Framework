from agno.agent import Agent
from agno.team import Team
from agno.models.google import Gemini
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
os.environ["GEMINI_API_KEY"]=os.getenv("GEMINI_API_KEY")


web_agent=Agent(
    name="Web Agent",
    role="Search The Web for information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGoTools()],
    instructions="Always include the sources",
    markdown=True
)

finance_agent=Agent(
    name="Finance Agent",
    role="Get Finance Data",
    model=Gemini(id="gemini-2.0-flash"),
    tools=[YFinanceTools(enable_stock_price=True, enable_analyst_recommendations=True)],
    instructions="Use Tables to Display Data",
    markdown=True
)

agents_team=Team(
    members=[web_agent, finance_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Always include sources", "Use tables to display data"],
    markdown=True
)

agents_team.print_response("Analyze The Companies like Tesla, NVDIA, Apple and suggest which to buy for long term")