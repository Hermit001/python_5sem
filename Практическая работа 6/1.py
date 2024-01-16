import re

def process_journal(journal_file, output_file):
    try:
        with open(journal_file, 'r') as file:
            journal_lines = file.readlines()
            
            with open(output_file, 'w') as output:
                for line in journal_lines:
                    # Используем регулярное выражение для поиска информации о рейсах
                    match = re.search(r'Рейс (\d+) (прибыл из|отправился в) (\w+) в (\d+:\d+:\d+)', line)
                    if match:
                        train_number, direction, city, time = match.groups()
                        entry = f"[{time}] - Поезд № {train_number} {direction} {city}\n"
                        output.write(entry)
            
            print(f"Информация из файла журнала успешно обработана и записана в '{output_file}'.")

    except FileNotFoundError:
        print(f"Файл '{journal_file}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

# Укажите имя файла журнала и имя файла для записи преобразованной информации
journal_file = 'journal.txt'
output_file = 'processed_journal.txt'

# Обработка журнала и запись результата в файл
process_journal(journal_file, output_file)
