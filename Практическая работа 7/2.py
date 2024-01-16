import csv

def get_books_with_substring(filename, substring):
    books = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            isbn, title, author, quantity, price = row
            if substring.lower() in title.lower():
                books.append([isbn, title, author, int(quantity), float(price)])
    return books

def get_totals(book_list):
    totals = []
    for book in book_list:
        isbn, title, author, quantity, price = book
        total_price = quantity * price
        totals.append((isbn, total_price))
    return totals

# Задайте имя файла и подстроку для поиска
filename = 'books.csv'
substring = 'Python'

# Получите список книг с подстрокой в названии
filtered_books = get_books_with_substring(filename, substring)

# Получите список кортежей с общей стоимостью книг
totals = get_totals(filtered_books)

# Выведите результат
for isbn, total_price in totals:
    print(f'ISBN: {isbn}, Общая стоимость: {total_price:.2f}')
