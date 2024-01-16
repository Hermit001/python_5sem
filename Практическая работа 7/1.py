import csv

def get_books(param):
    matching_books = []

    with open('books.csv', 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Прочитать заголовки столбцов

        for row in reader:
            isbn, title, author, quantity, price = row
            if param.lower() in title.lower() or param.lower() in author.lower():
                matching_books.append([isbn, title, author, int(quantity), float(price)])

    return matching_books