rubles_per_pasta: float = 300.54 #рублей за единицу
rubles_per_palka: float = 152.89 #рублей за единицу

n_persons = int(input("Скольким людям нужно начистить зубы?: "))

result: int | float = (rubles_per_palka * n_persons) + (rubles_per_pasta * (n_persons / 2))

print(
    "Тебе надо вот столько рублей:", result
)