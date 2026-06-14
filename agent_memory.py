from agno.agent import Agent
from agno.models.google import Gemini
from agno.knowledge.embedder.google import GeminiEmbedder
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.knowledge.knowledge import Knowledge
from agno.vectordb.lancedb import LanceDb, SearchType
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GEMINI_API_KEY"]=os.getenv("GEMINI_API_KEY")

agent = Agent(
    model=Gemini(id="gemini-2.0-flash"),
    description="You are a Thai cuisine expert!",
    instructions=[
        "Search your knowledge base for Thai recipes.",
        "If the question is better suited for the web, search the web to fill in gaps.",
        "Prefer the information in your knowledge base over the web results."
    ],
    knowledge=Knowledge(
        vector_db=LanceDb(
            uri="tmp/lancedb",
            table_name="recipes",
            search_type=SearchType.hybrid,
            embedder=GeminiEmbedder(id="text-embedding-3-small"),
        ),
    ),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)

# Comment out after the knowledge base is loaded
if agent.knowledge is not None:
    agent.knowledge.insert(
        url="https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf",
        skip_if_exists=True
    )

agent.print_response("How do I make chicken and galangal in coconut milk soup", stream=True)
agent.print_response("What is the history of Thai curry?", stream=True)