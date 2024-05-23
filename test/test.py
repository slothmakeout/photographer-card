from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Пути к изображениям должны начинаться с папки static,
# поэтому удалим "static/" из путей к изображениям

# photos_data = [
#     {"id": 1, "src": "images/photo1.jpg"},  # Изменили путь к изображениям
#     {"id": 2, "src": "images/photo2.jpg"},
#     # Добавьте остальные данные о фотографиях
# ]


# Функция для получения всех файлов в папке images/photos_data
def get_photos_data():
    photos_data = []
    photos_dir = "images/photos_data"

    # Проверяем существование директории
    if not os.path.exists(photos_dir):
        return photos_data

    # Получаем список файлов в директории
    files = os.listdir(photos_dir)

    # Фильтруем только файлы изображений
    image_files = [
        file for file in files if file.endswith((".jpg", ".jpeg", ".png", ".gif"))
    ]

    # Формируем данные о каждой фотографии
    for idx, file_name in enumerate(image_files, start=1):
        photo_data = {
            "id": idx,
            "src": f"images/photos_data/{file_name}",  # Формируем путь к изображению
        }
        photos_data.append(photo_data)

    return photos_data


# Пример использования функции
photos_data = get_photos_data()
print(photos_data)