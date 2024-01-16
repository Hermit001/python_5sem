import random

def simulate_birthday_paradox(num_simulations, num_people):
    birthday_matches = 0

    for _ in range(num_simulations):
        # Генерируем случайные дни рождения для num_people человек
        birthdays = [random.randint(1, 28) for _ in range(num_people)]

        # Если есть совпадение дней рождений, увеличиваем счетчик
        if len(birthdays) != len(set(birthdays)):
            birthday_matches += 1

    # Вычисляем вероятность совпадения
    probability = birthday_matches / num_simulations
    return probability

num_simulations = 100  # Количество симуляций
num_people = 23  # Количество людей в группе

# Запускаем симуляцию и выводим результат
probability = simulate_birthday_paradox(num_simulations, num_people)
print(f"Вероятность совпадения дней рождений среди {num_people} человек: {probability:.2%}")
