document.addEventListener("DOMContentLoaded", function () {
    const numerateElements = document.querySelectorAll(".item__numerate");

    numerateElements.forEach((element, index) => {
        element.textContent = (index + 1).toString();
    });
});
