import random

def simulate_game():
    # Создаем список из трех дверей, одна из которых содержит приз
    doors = ['empty', 'empty', 'prize']
    
    # Участник выбирает случайную дверь
    choice = random.randrange(3)
    
    # Ведущий открывает одну из оставшихся дверей, за которой нет приза
    for i in range(3):
        if i != choice and doors[i] == 'empty':
            revealed = i
            break
    
    # Участник может изменить свой выбор и выбрать другую дверь
    for i in range(3):
        if i != choice and i != revealed:
            new_choice = i
            break
    
    # Возвращаем результат: True, если участник выиграл приз, иначе False
    return doors[new_choice] == 'prize'

# Проводим множество симуляций
total_simulations = 1000000
switched_wins = 0

for _ in range(total_simulations):
    if simulate_game():
        switched_wins += 1

# Рассчитываем процент побед, когда участник изменил свой выбор
percentage_switched_wins = (switched_wins / total_simulations) * 100

print(f"Процент побед при смене выбора: {percentage_switched_wins}%")
