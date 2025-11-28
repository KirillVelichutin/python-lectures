from agno.agent import Agent
from agno.workflow import Workflow
from agno.models.cohere import Cohere
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.memory import MemoryManager
from agno.knowledge.knowledge import Knowledge
from agno.vectordb.pgvector import PgVector
from agno.db.sqlite import SqliteDb
import dotenv


dotenv.load_dotenv(dotenv.find_dotenv())

db = SqliteDb(db_file="./data/memory/agno.db")

memory_manager = MemoryManager(
    db=db,
    additional_instructions="Don't store the user's real name",
)

knowledge = Knowledge(
    vector_db=PgVector(
        table_name="knowledge_documents",
        db_url="postgresql+psycopg://agno_user:secret@localhost:5432/agno_kb"
    ),
)

researcher = Agent(
            model=Cohere(
                        id="command-a-03-2025",
                        api_key="zkoZYaHSZbzDYrCGAreEt4gLIr1lqMZGcSnBOtLR",
                        ),
            tools=[
                DuckDuckGoTools(),
            ],
            db=db,
            memory_manager=memory_manager,
            enable_user_memories=True,
            knowledge=knowledge,
            search_knowledge=True,
            instructions=[
                """
                Try to recall things first and if you fail search for them in knowldge base.
                If you fail to find answer in knowledge base search the internet for the answer.
                Always include source references in your responses.
                """
            ],
            reasoning=True,
            markdown=True
            )

research_workflow = Workflow(
    name="Search info",
    steps=[researcher]
)

while True:
    user_input = input("User: ")
    research_workflow.print_response(f"{user_input}", stream=True)