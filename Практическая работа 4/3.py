def save_file(file_name, words):
    try:
        # Открываем файл с указанным именем для записи (utf-8 используется для корректной работы с кириллицей)
        with open(file_name, 'w', encoding='utf-8') as file:
            # Сначала записываем количество уникальных слов
            unique_word_count = len(words)
            file.write(f"Всего уникальных слов: {unique_word_count}\n\n")
            
            # Сортируем слова в алфавитном порядке
            sorted_words = sorted(words)
            
            # Записываем каждое слово в файл
            for word in sorted_words:
                file.write(word + '\n')
        
        print(f"Результат записан в файл '{file_name}'")
    except Exception as e:
        # В случае ошибки выводим сообщение
        print(f"Произошла ошибка при записи в файл '{file_name}': {str(e)}")

def read_file(file_name):
    # Создаем пустой множество для хранения уникальных слов
    unique_words = set()
    
    try:
        # Открываем файл с указанным именем для чтения (utf-8 используется для корректной работы с кириллицей)
        with open(file_name, 'r', encoding='utf-8') as file:
            # Считываем весь текст из файла
            text = file.read()
            # Разделяем текст на слова (просто по пробелам, без учета знаков препинания)
            words = text.split()
            
            # Перебираем слова из текста
            for word in words:
                # Приводим каждое слово к нижнему регистру и добавляем его в множество
                unique_words.add(word.lower())
        
        # Преобразуем множество обратно в список и возвращаем его
        return list(unique_words)
    except FileNotFoundError:
        # В случае ошибки (файл не найден) выводим сообщение и возвращаем пустой список
        print(f"Файл '{file_name}' не найден.")
        return []

# Пример использования
file_name = 'data.txt'
words = read_file(file_name)
print(words)


# Пример использования
file_name = 'count.txt'
save_file(file_name, words)