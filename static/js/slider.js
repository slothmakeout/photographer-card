const image1 = document.getElementById("image1");
const image2 = document.getElementById("image2");
console.log(image1, image2);
setInterval(() => {
  console.log(image1, image2);
  //   console.log(image1.classList.entries);
  // Переключение классов для анимации
  image1.classList.toggle("opacity-100");
  image1.classList.toggle("opacity-0");
  image2.classList.toggle("opacity-100");
  image2.classList.toggle("opacity-0");
}, 1000); // Через каждые 5 секунд
