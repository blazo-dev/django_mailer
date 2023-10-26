const modal = document.getElementById("modal");
const cancelButton = document.getElementById("closeButton");

cancelButton.addEventListener("click", () => {
  modal.close();
});
