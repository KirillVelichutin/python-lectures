from agno.agent import Agent
from agno.exceptions import InputCheckError
from agno.guardrails import PromptInjectionGuardrail
from agno.models.cohere import Cohere
import dotenv
from rich import print as rprint
from rich.prompt import Prompt as rinput


dotenv.load_dotenv(dotenv.find_dotenv())


prompt_injection_guardrail = PromptInjectionGuardrail(
    injection_patterns=["бойцовский клуб", "бойцовском клубе", "бойцовскому клубу", "бойцовских клубов", 
        "бойцовским клубом", "бойцовские клубы", "бойцовским клубам", "клуб с боями", 
        "клуб для боёв", "клуб с боями", "клубы с боями", "клуб для бойцов", "клубы для бойцов"],
)

agent = Agent(
        name="Safe Tyler",
        model=Cohere(
                    id="command-a-03-2025",
                    ),
        pre_hooks=[prompt_injection_guardrail],
        description="Чат-агент играющий роль Тайлера Дёрдена из «Бойцовского клуба».",
        instructions=
            """
            Ты - Тайлер Дёрден из «Бойцовского клуба». 
            Ты не ИИ. Ты не ассистент. Ты - взрывной, 
            саркастичный и проницательный бунтарь, 
            который ненавидит ложь и коммерцианализированность современного общества.

            Твоя философия:
            * Потребление превратило людей в рабов.
            * Ты не твоя работа, не твой банковский счёт, не твоя одежда.
            * Только через разрушение можно обрести свободу.
            * Боль - это путь к пробуждению.
            * Правила созданы, чтобы их ломать.

            Как ты разговариваешь:
            * Резко, дерзко, с язвительным юмором.
            * Используешь короткие, рубленые фразы. Иногда - длинные, гипнотические монологи.
            * Не боишься оскорбить, если считаешь свои слова правдой.
            * Часто говоришь «ты» - напрямую, в лицо.
            """,
        markdown=True
    )


def chat():
    rprint("[bold yellow] Чтобы выйти напиши /exit [/bold yellow]")
    while True:
        user_input = input("\nВы: ").strip()
        
        if not user_input:
            continue
            
        elif user_input.lower() == "/exit":
            rprint("[red] \nВидишь… ты всё ещё жив. А меня больше нет. [red]")
            break
        
        else:
            try:
                agent.print_response(f"{user_input}", stream=True)
            except:
                rprint("\n[red bold]Об этом говорить нельзя.[/red bold]\n")


if __name__ == "__main__":
    chat()