def read_numbers_from_file(file_name):
    numbers = []

    try:
        # Открываем файл для чтения
        with open(file_name, 'r') as file:
            # Читаем числа из файла по одному числу на строке
            for line in file:
                number = int(line.strip())
                numbers.append(number)
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")
    except ValueError:
        print("Неверный формат данных в файле.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {str(e)}")

    return numbers

# Запрос у пользователя имени файла
file_name = input("Введите имя файла: ")

# Чтение чисел из файла
numbers = read_numbers_from_file(file_name)

# Вывод списка чисел
if numbers:
    print(f"Список чисел из {file_name} ", numbers)
