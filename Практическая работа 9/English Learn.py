import os
import pdf2docx
from docx2pdf import convert
from PIL import Image

# Функция для смены рабочего каталога
def change_working_directory():
    new_dir = input("Укажите корректный путь к рабочему каталогу: ")
    try:
        os.chdir(new_dir)
        print("Текущий каталог:", os.getcwd())
    except FileNotFoundError:
        print("Каталог не найден.")

# Функция для конвертации PDF в DOCX
def convert_pdf_to_docx():
    pdf_files = [f for f in os.listdir() if f.endswith(".pdf")]
    if not pdf_files:
        print("В текущем каталоге нет файлов PDF.")
        return

    print("Список файлов с расширением .pdf в данном каталоге:")
    for i, pdf_file in enumerate(pdf_files, start=1):
        print(f"{i}. {pdf_file}")

    choice = input("Введите номер файла для преобразования (Чтобы преобразовать все файлы из данного каталога введите 0): ")

    if choice == "0":
        for pdf_file in pdf_files:
            pdf2docx.convert(pdf_file)
            print(f"Файл {pdf_file} успешно преобразован в Docx.")
    elif choice.isdigit() and 1 <= int(choice) <= len(pdf_files):
        selected_pdf_file = pdf_files[int(choice) - 1]
        pdf2docx.convert(selected_pdf_file)
        print(f"Файл {selected_pdf_file} успешно преобразован в Docx.")
    else:
        print("Некорректный выбор.")

# Функция для конвертации DOCX в PDF
def convert_docx_to_pdf():
    docx_files = [f for f in os.listdir() if f.endswith(".docx")]
    if not docx_files:
        print("В текущем каталоге нет файлов Docx.")
        return

    print("Список файлов с расширением .docx в данном каталоге:")
    for i, docx_file in enumerate(docx_files, start=1):
        print(f"{i}. {docx_file}")

    choice = input("Введите номер файла для преобразования (Чтобы преобразовать все файлы из данного каталога введите 0): ")

    if choice == "0":
        convert(docx_files)
        print("Все файлы успешно преобразованы в PDF.")
    elif choice.isdigit() and 1 <= int(choice) <= len(docx_files):
        selected_docx_file = docx_files[int(choice) - 1]
        convert(selected_docx_file)
        print(f"Файл {selected_docx_file} успешно преобразован в PDF.")
    else:
        print("Некорректный выбор.")

# Функция для сжатия изображений
def compress_images():
    image_files = [f for f in os.listdir() if f.endswith((".jpeg", ".gif", ".png", ".jpg"))]
    if not image_files:
        print("В текущем каталоге нет изображений для сжатия.")
        return

    print("Список файлов с расширениями .jpeg, .gif, .png, .jpg в данном каталоге:")
    for i, image_file in enumerate(image_files, start=1):
        print(f"{i}. {image_file}")

    choice = input("Введите номер файла для сжатия (Чтобы сжать все изображения из данного каталога введите 0): ")

    if choice == "0":
        for image_file in image_files:
            compress_image(image_file)
            print(f"Файл {image_file} успешно сжат.")
    elif choice.isdigit() and 1 <= int(choice) <= len(image_files):
        selected_image_file = image_files[int(choice) - 1]
        compress_image(selected_image_file)
        print(f"Файл {selected_image_file} успешно сжат.")
    else:
        print("Некорректный выбор.")

# Функция для сжатия одного изображения
def compress_image(image_file):
    try:
        with Image.open(image_file) as img:
            img.save(image_file, quality=50)
    except Exception as e:
        print(f"Ошибка при сжатии файла {image_file}: {str(e)}")

# Функция для удаления файлов по расширению
def delete_files_by_extension(extension):
    files_to_delete = [f for f in os.listdir() if f.endswith(extension)]
    if not files_to_delete:
        print(f"В текущем каталоге нет файлов с расширением {extension}.")
        return

    print(f"Список файлов с расширением {extension} в данном каталоге:")
    for i, file in enumerate(files_to_delete, start=1):
        print(f"{i}. {file}")

    choice = input("Введите номер файла для удаления (Чтобы удалить все файлы с данным расширением введите 0): ")

    if choice == "0":
        for file in files_to_delete:
            try:
                os.remove(file)
                print(f"Файл: \"{file}\" успешно удален!")
            except Exception as e:
                print(f"Ошибка при удалении файла {file}: {str(e)}")
    elif choice.isdigit() and 1 <= int(choice) <= len(files_to_delete):
        selected_file = files_to_delete[int(choice) - 1]
        try:
            os.remove(selected_file)
            print(f"Файл: \"{selected_file}\" успешно удален!")
        except Exception as e:
            print(f"Ошибка при удалении файла {selected_file}: {str(e)}")
    else:
        print("Некорректный выбор.")

# Основная функция
def main():
    while True:
        print("\nТекущий каталог:", os.getcwd())
        print("Выберите действие:")
        print("0. Сменить рабочий каталог")
        print("1. Преобразовать PDF в Docx")
        print("2. Преобразовать Docx в PDF")
        print("3. Произвести сжатие изображений")
        print("4. Удалить группу файлов")
        print("5. Выход")

        choice = input("Введите номер действия: ")

        if choice == "0":
            change_working_directory()
        elif choice == "1":
            convert_pdf_to_docx()
        elif choice == "2":
            convert_docx_to_pdf()
        elif choice == "3":
            compress_images()
        elif choice == "4":
            print("\nВыберите действие: ")
            print("1. Удалить все файлы начинающиеся на определенную подстроку")
            print("2. Удалить все файлы заканчивающиеся на определенную подстроку")
            print("3. Удалить все файлы содержащие определенную подстроку")
            print("4. Удалить все файлы по расширению")
            delete_option = input("Введите номер действия: ")
            if delete_option == "1":
                substring = input("Введите подстроку: ")
                delete_files_by_extension(substring)
            elif delete_option == "2":
                substring = input("Введите подстроку: ")
                delete_files_by_extension(substring)
            elif delete_option == "3":
                substring = input("Введите подстроку: ")
                delete_files_by_extension(substring)
            elif delete_option == "4":
                extension = input("Введите расширение файла для удаления: ")
                delete_files_by_extension(extension)
            else:
                print("Некорректный выбор.")
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор.")

if __name__ == "__main__":
    main()
