# 21.05.2024 19:17
# Разобрался с тем, как повесить обработчик на элемент фотографии, следующая задача: праивльно расположить модальное окно
# Еще надо разобраться с адаптивной вёрсткой, как-то она странно работает

from flask import Flask, jsonify, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

# Функция для получения всех файлов в папке images/photos_data
def get_photos_data():
    photos_data = []
    photos_dir = "static/images/photos_data"

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
            "fullSrc": f"static/images/photos_data/{file_name}",  # Формируем путь к изображению
        }
        photos_data.append(photo_data)

    return photos_data

def get_images(directoryName):
    images_data = []
    images_dir = f"static/images/{directoryName}"

    # Проверяем существование директории
    if not os.path.exists(images_dir):
        return images_data

    # Получаем список файлов в директории
    files = os.listdir(images_dir)

    # Фильтруем только файлы изображений
    image_files = [
        file for file in files if file.endswith((".jpg", ".jpeg", ".png", ".gif"))
    ]

    # Формируем данные о каждой фотографии в алфавитном порядке
    for idx, file_name in enumerate(sorted(image_files), start=1):
        image_data = {
            "id": idx,
            "src": f"images/{directoryName}/{file_name}",  # Формируем путь к изображению
        }
        images_data.append(image_data)

    return images_data

home_images_data = get_images("home_images")
photos_data = get_images("photos_data")
photos_data = get_images("photos_data")

album1_photos_data = get_images("album1")
album1_data = [{**image, "album": 1,"albumName":"Buildings"} for image in album1_photos_data]
# print(album1_data)
album2_photos_data = get_images("album2")
album2_data = [{**image, "album": 2,"albumName":"Winter"} for image in album2_photos_data]
album3_photos_data = get_images("album3")
album3_data = [{**image, "album": 3,"albumName":"Summer"} for image in album3_photos_data]

albums_data = album1_data + album2_data + album3_data
# print(albums_data)

def get_album_images():
    albums_data = []
    albums_dir = "static/images/albums"

    # Проверяем существование директории с альбомами
    if not os.path.exists(albums_dir) or not os.path.isdir(albums_dir):
        return albums_data

    # Получаем список папок (альбомов) в директории albums
    album_folders = [folder for folder in os.listdir(albums_dir) if os.path.isdir(os.path.join(albums_dir, folder))]

    # Проходимся по каждой папке (альбому)
    for album_index, album_name in enumerate(sorted(album_folders), start=1):
        album_path = os.path.join(albums_dir, album_name)
        # Получаем список файлов в текущей папке (альбоме)
        files = os.listdir(album_path)
        # Фильтруем только файлы изображений
        image_files = [
            file for file in files if file.endswith((".jpg", ".jpeg", ".png", ".gif"))
        ]
        # Формируем данные о каждой фотографии в альбоме
        for idx, file_name in enumerate(sorted(image_files), start=1):
            image_data = {
                "id": idx,
                "src": f"images/albums/{album_name}/{file_name}",  # Формируем путь к изображению
                "album": album_index,
                "albumName": album_name
            }
            albums_data.append(image_data)

    return albums_data

alb1 = get_album_images()
print(alb1)

photographer_data = {
    "name": "D4H9.ONLINE",
    "photo_src": "images/photographer.jpg",  
    "description": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?",
}
contact_data = {
    "email": "photographer@example.com",
    "phone": "+123456789",
}


@app.route("/")
def home():
    return render_template(
        "home.html",
        photographer_name=photographer_data["name"],
        photos_data=photos_data,
        home_images_data=home_images_data
    )

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html", portfolio_data=photos_data, album1_data=album1_data, album2_data=album2_data, albums_data=alb1)


@app.route("/about")
def about():
    return render_template("about.html", photographer_data=photographer_data)

@app.route("/menu")
def menu():
    return render_template("menu.html", photographer_data=photographer_data)

@app.route("/contact")
def contact():
    return render_template("contact.html", contact_data=contact_data)

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    # Получение данных из POST запроса в формате JSON
    data = request.get_json()

    # Путь к файлу, где будет сохранён JSON
    save_path = os.path.join(os.getcwd(), 'db/data.json')

    # Сохранение данных в JSON файл
    with open(save_path, 'w') as f:
        json.dump(data, f, indent=4)

    # Отправка ответа клиенту о успешном сохранении данных
    return jsonify({'status': 'success', 'message': 'Request sent'})

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/album/<int:album_id>', methods=['GET'])
def get_album(album_id):
    album_photos = [photo for photo in alb1 if photo['album'] == album_id]
    if not album_photos:
        return jsonify({'error': 'Album not found'}), 404
    return jsonify({'album_id': album_id, 'photos': album_photos})

if __name__ == "__main__":
    app.run(debug=True)
