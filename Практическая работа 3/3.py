import random

# Список слов
words = ["книга", "месяц", "ручка", "шарик", "олень", "носок"]

def choose_difficulty():
    while True:
        print("Выберите уровень сложности:")
        print("1. Легкий (7 жизней)")
        print("2. Средний (5 жизней)")
        print("3. Сложный (3 жизни)")
        choice = input("Введите номер уровня (1/2/3): ")
        if choice in ["1", "2", "3"]:
            return int(choice)
        else:
            print("Пожалуйста, выберите один из предложенных уровней.")

def play_game(word_to_guess, lives):
    # Преобразуем слово в список символов для удобства
    word_as_list = list(word_to_guess)

    # Создаем список для отображения слова с угаданными буквами
    displayed_word = ["\u25A0"] * len(word_to_guess)

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

def main():
    while words:
        # Выбираем случайное слово из списка
        word_to_guess = random.choice(words)
        words.remove(word_to_guess)

        # Выбираем уровень сложности
        difficulty = choose_difficulty()
        if difficulty == 1:
            lives = 7
        elif difficulty == 2:
            lives = 5
        elif difficulty == 3:
            lives = 3

        # Запускаем игру
        play_game(word_to_guess, lives)

        # Предлагаем игроку сыграть еще или отказаться
        choice = input("Хотите сыграть еще? (да/нет): ").lower()
        if choice != "да":
            break

if __name__ == "__main__":
    main()