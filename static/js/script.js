// static/js/script.js

console.log("script.js загружен");

var slideIndex = 0;

function openModal(src) {
  console.log("openModal");
  var modal = document.getElementById("modal");
  var modalImg = document.getElementById("modal-image");
  console.log(modalImg);
  modal.style.display = "block";
  modalImg.src = src;

  // Обновляем индекс текущего изображения
  var photos = document.querySelectorAll(".photo-item img");
  slideIndex = Array.from(photos).findIndex((photo) => photo.src.includes(src));
}

function closeModal() {
  var modal = document.getElementById("modal");
  modal.style.display = "none";
}

function changeSlide(n) {
  var photos = document.querySelectorAll(".photo-item img");
  slideIndex += n;

  if (slideIndex >= photos.length) {
    slideIndex = 0;
  } else if (slideIndex < 0) {
    slideIndex = photos.length - 1;
  }

  var modalImg = document.getElementById("modal-image");
  modalImg.src = photos[slideIndex].src;
}
