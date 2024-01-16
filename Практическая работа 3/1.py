import random

# Список слов
words = ["книга", "месяц", "ручка", "шарик", "олень", "носок"]

# Выбираем случайное слово
word_to_guess = random.choice(words)

# Преобразуем слово в список символов для удобства
word_as_list = list(word_to_guess)

# Создаем список для отображения слова с угаданными буквами
displayed_word = ["\u25A0"] * len(word_to_guess)

# Количество "жизней"
lives = 5

# Основной цикл игры
while True:
    # Отображаем текущее состояние игры
    print(" ".join(displayed_word))
    print(f"Осталось жизней: {lives}")

    # Просим игрока ввести букву или слово
    guess = input("Введите букву или слово: ").lower()

    # Проверяем, что введен только один символ
    if len(guess) == 1:
        if guess in word_to_guess:
            # Если буква угадана, заменяем символы в отображаемом слове
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    displayed_word[i] = guess
        else:
            # Если буква неправильная, уменьшаем количество жизней
            lives -= 1
    elif guess == word_to_guess:
        # Если игрок угадал слово целиком, завершаем игру
        print(f"Вы угадали! Загаданное слово: {word_to_guess}")
        break

    # Проверяем условия завершения игры
    if lives == 0:
        print("Игра окончена. Вы проиграли.")
        break
    elif "\u25A0" not in displayed_word:
        print("Игра окончена. Вы выиграли!")
        break
