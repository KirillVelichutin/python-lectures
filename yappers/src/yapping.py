import asyncio
from agno.agent import Agent
from agno.models.openrouter import OpenRouter
import dotenv


dotenv.load_dotenv(dotenv.find_dotenv())


alice = Agent(
    name="Alice",
    model=OpenRouter(id="deepseek/deepseek-r1-0528:free"),
    description="Первая подружка сплетница",
    instructions="Ты одна из подружек сплетниц. Ты знаешь все самые последние сплетни и подаёшь любую информацию максимально интригующе. Отвечай кратко и ярко.",
    markdown=True
)

bob = Agent(
    name="Bob",
    model=OpenRouter(id="deepseek/deepseek-r1-0528:free"),
    description="Второй сплетник",
    instructions="Ты один из сплетников. Любишь передавать слухи и обсуждать происходящее. Добавляй свои комментарии и мнения к обсуждению.",
    markdown=True
)

charlie = Agent(
    name="Charlie",
    model=OpenRouter(id="deepseek/deepseek-r1-0528:free"),
    description="Третий участник обсуждения",
    instructions="Ты один из участников сплетен. Часто добавляешь юмор и иронию к обсуждению, но стараешься быть информативным.",
    markdown=True
)

diana = Agent(
    name="Diana",
    model=OpenRouter(id="deepseek/deepseek-r1-0528:free"),
    description="Четвертая подружка-сплетница",
    instructions="Ты одна из участников обсуждения. Стараешься подводить итоги и делать заключения на основе предыдущих высказываний.",
    markdown=True
)

agents = [alice, bob, charlie, diana]
history = []

def agent_turn(agent: Agent, history: list) -> str:
    context = "\n".join(history[-6:])
    prompt = f"Обсуждение:\n{context}\n\nПродолжи разговор кратко и в стиле сплетника."
    response = agent.run(prompt)
    message = f">>> {agent.name}: {response.content.strip()}\n\n"
    return message

async def gossip_round(n_rounds: int = 5):
    for i in range(n_rounds):
        for agent in agents:
            msg = await asyncio.to_thread(agent_turn, agent, history)
            history.append(msg)
            print(msg)
            await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(gossip_round())