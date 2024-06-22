# 21.05.2024 19:17
# Разобрался с тем, как повесить обработчик на элемент фотографии, следующая задача: праивльно расположить модальное окно
# Еще надо разобраться с адаптивной вёрсткой, как-то она странно работает

from flask import Flask, render_template, request, redirect, url_for
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


# Пример использования функции
photos_data = get_photos_data()
print(photos_data)

photographer_data = {
    "name": "D4H9.ONLINE",
    "photo_src": "images/photographer.jpg",  # Изменили путь к изображению
    "description": "Описание фотографа...",
}

# Данные для страницы контактов
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
    )


@app.route("/submit_contact", methods=["POST"])
def submit_contact():
    if request.method == "POST":
        full_name = request.form["full_name"]
        email = request.form["email"]
        phone = request.form.get("phone")  # Получаем необязательное поле телефона
        subject = request.form["subject"]
        message = request.form["message"]

        # Здесь можно добавить логику для обработки данных формы, например, отправку электронной почты

        # После обработки формы перенаправляем пользователя на страницу "Спасибо" или на главную
        return redirect(url_for("home"))


@app.route("/portfolio")
def portfolio():
    # Здесь можно загрузить данные для страницы портфолио, если они нужны
    return render_template("portfolio.html", portfolio_data=photos_data)


@app.route("/about")
def about():
    return render_template("about.html", photographer_data=photographer_data)

@app.route("/menu")
def menu():
    return render_template("menu.html", photographer_data=photographer_data)

@app.route("/contact")
def contact():
    return render_template("contact.html", contact_data=contact_data)


if __name__ == "__main__":
    app.run(debug=True)
