from collections import Counter
from googletrans import Translator

# Открываем нормализованный файл
with open('normalized_dialog.txt', 'r', encoding='utf-8') as input_file:
    words = input_file.read().split()

# Создаем словарь слово - количество упоминаний
word_count = Counter(words)

# Сортируем словарь по количеству упоминаний
sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# Создаем объект Translator
translator = Translator()

# Создаем словарь для хранения результатов перевода
translated_words = {}

# Переводим слова и сохраняем результаты в словаре
for word, count in sorted_word_count:
    translation = translator.translate(word, src="ru", dest="en").text
    translated_words[word] = (translation, count)

# Сохраняем результаты в текстовый файл с указанием кодировки utf-8
with open('translated_words.txt', 'w', encoding='utf-8') as output_file:
    for word, (translation, count) in translated_words.items():
        output_file.write(f'{word} | {translation} | {count}\n')

print("Перевод выполнен и сохранен в файл 'translated_words.txt'.")
