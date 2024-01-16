import os
import PySimpleGUI as sg
from pdf2docx import Converter
from docx2pdf import convert
from PIL import Image

# Функция для преобразования PDF в Docx
def pdf_to_docx(file_path):
    docx_file = os.path.splitext(file_path)[0] + ".docx"
    cv = Converter(file_path)
    cv.convert(docx_file, start=0, end=None)
    cv.close()

# Функция для преобразования Docx в PDF
def docx_to_pdf(file_path):
    pdf_file = os.path.splitext(file_path)[0] + ".pdf"
    convert(file_path, pdf_file)

# Функция для сжатия изображений
def compress_images(file_paths):
    for file_path in file_paths:
        img = Image.open(file_path)
        img.save(file_path, optimize=True, quality=10)

# Функция для удаления группы файлов
def delete_files(file_paths):
    for file_path in file_paths:
        os.remove(file_path)

# Определение макета приложения
layout = [
    [sg.Text("Выберите рабочий каталог:")],
    [sg.InputText(key="-DIR-"), sg.FolderBrowse(key="-BROWSE-")],
    [sg.Listbox(values=[], size=(50, 10), key="-FILE_LIST-")],
    [sg.Button("Сменить рабочий каталог")],
    [sg.Text("Действия:")],
    [sg.Button("Преобразовать PDF в Docx")],
    [sg.Button("Преобразовать Docx в PDF")],
    [sg.Button("Сжать изображения")],
    [sg.Button("Удалить группу файлов")],
    [sg.Exit()]
]

# Создание окна приложения
window = sg.Window("Мое GUI приложение", layout)

# Основной цикл приложения
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    elif event == "Сменить рабочий каталог":
        new_dir = values["-DIR-"]
        if os.path.isdir(new_dir):
            os.chdir(new_dir)
            files = os.listdir()
            window["-FILE_LIST-"].update(files)
        else:
            sg.popup_error("Каталог не найден!")

    elif event == "Преобразовать PDF в Docx":
        selected_files = values["-FILE_LIST-"]
        for file in selected_files:
            if file.lower().endswith(".pdf"):
                pdf_to_docx(file)

    elif event == "Преобразовать Docx в PDF":
        selected_files = values["-FILE_LIST-"]
        for file in selected_files:
            if file.lower().endswith(".docx"):
                docx_to_pdf(file)

    elif event == "Сжать изображения":
        selected_files = values["-FILE_LIST-"]
        image_files = [file for file in selected_files if file.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))]
        compress_images(image_files)

    elif event == "Удалить группу файлов":
        selected_files = values["-FILE_LIST-"]
        files_to_delete = [file for file in selected_files]
        delete_files(files_to_delete)

    files = os.listdir()
    window["-FILE_LIST-"].update(files)

window.close()
