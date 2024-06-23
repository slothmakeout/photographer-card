// Получаем все изображения внутри контейнера
const images = document.querySelectorAll("#imageContainer img");
let currentImageIndex = 0;

setInterval(() => {
  // Текущая и следующая фотографии
  const currentImage = images[currentImageIndex];
  const nextImageIndex = (currentImageIndex + 1) % images.length;
  const nextImage = images[nextImageIndex];

  // Переключение классов для анимации
  currentImage.classList.toggle("opacity-0");
  currentImage.classList.toggle("opacity-100");
  nextImage.classList.toggle("opacity-0");
  nextImage.classList.toggle("opacity-100");

  // Обновление текущего индекса
  currentImageIndex = nextImageIndex;
}, 1000);
