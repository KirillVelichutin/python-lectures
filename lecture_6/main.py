import time
from functools import lru_cache

@lru_cache()
def calculate_name(name: str, age: int):
    wait_time: int = 2
    print(f"Waiting {wait_time} seconds...")
    time.sleep(wait_time)
    print("I am awake!")
    print(f"Hello {name} ({age} y. o.)")    
    

MY_CACHE: dict[str, str] = {}
def calculate_surname(name: str = "Vova"):
    if name in MY_CACHE:
        return MY_CACHE[name]
    time.sleep(2)
    surname = name + "4kin"
    MY_CACHE[name] = surname
    return surname

if __name__ == "__main__":
    print(f"{MY_CACHE=}")
    _ = calculate_surname("Ilya")
    _ = calculate_surname()
    _ = calculate_surname("Andrey")
    print(
        calculate_surname("Ilya")
    )
    print(
        calculate_surname()
    )
    print(
        calculate_surname("Vova")
    )
    print(
        calculate_surname("Ilya")
    )
    print(
        calculate_surname("Andrey")
    )
    print(f"{MY_CACHE=}")