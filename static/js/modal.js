// Получаем элементы
var modal = document.getElementById("myModal");
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");
var closeBtn = document.getElementsByClassName("close")[0];

// Функция для открытия модального окна
function openModal(src, alt) {
  modal.style.display = "block";
  modalImg.src = src;
  captionText.innerHTML = alt;
}

// Закрытие модального окна по клику на <span> (x)
closeBtn.onclick = function () {
  modal.style.display = "none";
};

// Добавляем обработчики для каждого изображения
document.querySelectorAll(".photo-item img").forEach((img) => {
  img.onclick = function () {
    openModal(this.src, this.alt);
  };
});

// Закрытие модального окна при клике вне изображения
window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};
