function updateStyle(element, removeStyle, addStyle) {
  element.classList.remove(removeStyle);
  element.classList.add(addStyle);
}

const menuButton = document.getElementById("menuButton");
const body = document.body;
const menuOverlay = document.getElementById("menuOverlay");
const brand = document.getElementById("brand");
const menuContent = document.getElementById("menuContent");
const menuTimeout = 500;

menuButton.addEventListener("click", () => {
  if (menuOverlay.classList.contains("translate-y-0")) {
    // Если оверлей открыт
    menuContent.style.opacity = "0";
    updateStyle(menuButton, "text-white", "text-blue-500");
    updateStyle(brand, "text-white", "text-blue-500");

    setTimeout(() => {
      updateStyle(menuOverlay, "translate-y-0", "-translate-y-full");
      updateStyle(body, "overflow-hidden", "overflow-auto");
    }, menuTimeout); // = duration анимации скрытия содержимого
  } else {
    // Если оверлей закрыт
    menuOverlay.classList.add("translate-y-0");
    menuContent.style.opacity = "0";

    updateStyle(menuButton, "text-blue-500", "text-white");
    updateStyle(brand, "text-blue-500", "text-white");
    setTimeout(() => {
      menuContent.style.opacity = "1";
      updateStyle(body, "overflow-auto", "overflow-hidden");
    }, menuTimeout); // Синхронизируем появление содержимого с окончанием анимации спуска оверлея
  }
});
