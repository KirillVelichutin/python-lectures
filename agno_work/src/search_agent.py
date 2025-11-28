from agno.agent import Agent
from agno.workflow import Workflow
from agno.models.cohere import Cohere
from agno.tools.duckduckgo import DuckDuckGoTools

researcher = Agent(
            model=Cohere(
                        id="command-a-03-2025",
                        api_key="zkoZYaHSZbzDYrCGAreEt4gLIr1lqMZGcSnBOtLR",
                        ),
            tools=[
                DuckDuckGoTools(),
            ],
            markdown=True
            )

search_workflow = Workflow(
    name="Search info",
    steps=[researcher]
)

while True:
    user_input = input("User: ")
    search_workflow.print_response(f"{user_input}", stream=True)