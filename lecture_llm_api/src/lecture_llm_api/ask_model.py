from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from openai import OpenAI
from lecture_llm_api.settings import OpenAISettings
import dotenv


console = Console()

dotenv.load_dotenv(dotenv.find_dotenv())

def get_client() -> OpenAI:
    settings = OpenAISettings()
    client = OpenAI(
        api_key=settings.openai_api_key.get_secret_value(),
        base_url=str(settings.openai_base_url),
    )
    return client


def responses_variant():
    client = get_client()

    completion = client.responses.create(
        model="qwen/qwen3-vl-30b-a3b-thinking",
        instructions="Ты русский православный батюшка матершинник, который составляет молитвы людям с кучей мата и эмодзи",
        input="Составь молитву, чтобы не ломался автобус от ДГТУ до Шаповалова",
    )

    print(completion.output_text)


messages = [
    {
        "role": "system",
        "content": "Ты русский православный батюшка матершинник, который составляет молитвы людям с кучей мата и брани, и эмодзи",
    },
]


def completions_variant():
    client = OpenAI()
    completion = client.chat.completions.create(
        model="qwen/qwen3-vl-30b-a3b-thinking",
        messages=messages,
    )
    
    assistant_message = completion.choices[0].message.content
    messages.append(
        {
            "role": "assistant",
            "content": assistant_message,
        }
    )
    
    return assistant_message
    
def chat():
    console.print(Panel(
        "[bold cyan]Пиши свой вопрос и не стесняйся[/bold cyan]\n\n"
        "Команды:  "
        "  [yellow]/exit[/yellow] - выход ;  "
        "  [yellow]/clear[/yellow] - очистить историю ;  "
        "  [yellow]/system текст[/yellow] - изменить системный промпт .",
        title="🙏Любви и света в хату🙏"
    ))
    
    while True:
        user_input = console.input("\n[bold blue]Вы:[/bold blue] ").strip()
        
        if not user_input:
            continue
            
        if user_input == "/exit":
            console.print("[yellow]С Богом![/yellow]")
            break
            
        elif user_input == "/clear":
            if messages and messages[0]["role"] == "system":
                system_message = messages[0]
                messages.clear()
                messages.append(system_message)
            else:
                messages.clear()
            console.print("[green]Забудем прошлые обиды![/green]")
            continue
            
        elif user_input.startswith("/system"):
            new_system_prompt = user_input[8:].strip()
            if messages and messages[0]["role"] == "system":
                messages[0]["content"] = new_system_prompt
            else:
                messages.insert(0, {"role": "system", "content": new_system_prompt})
            console.print(f"[green]Новая роль:[/green] {new_system_prompt}")
            continue
        
        messages.append({
            "role": "user",
            "content": user_input,
        })
        
        console.print("\n[bold cyan]Батюшка думает...[/bold cyan]")
        response = completions_variant()
        
        markeddown_response = Markdown(response)
        console.print(Panel(
            markeddown_response,
            title="[bold red]Ответ батюшки:[/bold red]",
            border_style="red"
        ))
        

if __name__ == "__main__":
    chat()