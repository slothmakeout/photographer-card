const overlays = document.querySelectorAll("#imageOverlay");
// overlays.forEach((overlay) => {
//   const img = overlay.previousElementSibling;
//   const albumName = img.getAttribute("data-albumName");
//   overlay.textContent = albumName;
// });

overlays.forEach((overlay) => {
  overlay.addEventListener("mouseenter", () => {
    overlay.querySelector("p").classList.add("opacity-100");
    console.log("mouseenter");
  });

  overlay.addEventListener("mouseleave", () => {
    overlay.querySelector("p").classList.remove("opacity-100");
    overlay.querySelector("p").classList.add("opacity-0");
    console.log("mouse leave");
  });

  overlay.addEventListener("click", function () {
    const img = overlay.previousElementSibling;
    const albumId = img.getAttribute("data-album");
    fetch(`/album/${albumId}`)
      .then((response) => response.json())
      .then((data) => {
        const viewContainer = document.getElementById("viewContainer");
        // Убираем все содержимое контейнера
        viewContainer.innerHTML = "";

        // Добавляем новые изображения в контейнер
        data.photos.forEach((photo) => {
          const img = document.createElement("img");
          img.src = `/static/${photo.src}`;
          img.alt = `Album ${photo.album} Photo`;
          img.className =
            "w-auto h-full object-contain bg-blue-900 cursor-pointer";
          img.onclick = function () {
            console.log("click-view");
            openModal(this.src, this.alt);
          };
          viewContainer.appendChild(img);
        });
      })
      .catch((error) => console.error("Error fetching album data:", error));
  });
});
