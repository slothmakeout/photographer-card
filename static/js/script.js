function updateStyle(element, removeStyle, addStyle) {
  element.classList.remove(removeStyle);
  element.classList.add(addStyle);
}

const menuButton = document.getElementById("menuButton");
const menuOverlay = document.getElementById("menuOverlay");
const brand = document.getElementById("brand");
const menuContent = document.getElementById("menuContent");
const menuTimeout = 500;

menuButton.addEventListener("click", () => {
  if (menuOverlay.classList.contains("translate-y-0")) {
    // Если оверлей открыт
    menuContent.style.opacity = "0";

    setTimeout(() => {
      updateStyle(menuOverlay, "translate-y-0", "-translate-y-full");
      updateStyle(menuButton, "text-white", "text-blue-300");
      updateStyle(brand, "hover:text-green-300", "hover:text-green-500");

      brand.classList.remove("text-white");
      brand.classList.add("text-blue-500");
      // Меняем цвет текста кнопки на синий после закрытия оверлея
    }, menuTimeout); // Это значение должно совпадать с duration анимации скрытия содержимого
  } else {
    // Если оверлей закрыт
    menuOverlay.classList.add("translate-y-0");
    menuContent.style.opacity = "0";

    menuButton.classList.remove("text-blue-300");
    menuButton.classList.add("text-white");

    brand.classList.remove("text-blue-500");
    brand.classList.add("text-white");
    updateStyle(brand, "hover:text-green-500", "hover:text-green-300");
    setTimeout(() => {
      menuContent.style.opacity = "1";
      // Меняем цвет текста кнопки на белый после открытия оверлея
    }, menuTimeout); // Синхронизируем появление содержимого с окончанием анимации спуска оверлея
  }
});
