import random

def birthday_paradox(num_people, num_simulations):
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

def month_hall(num_simulations):
    num_people = 23  # Количество людей в группе
    probability = birthday_paradox(num_people, num_simulations)
    return probability

# Пример использования функции month_hall
result = month_hall(1000)
print(f"Вероятность совпадения дней рождений среди 23 человек: {result:.2%}")
