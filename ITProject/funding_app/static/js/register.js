document.addEventListener("DOMContentLoaded", function () {
    let inputs = document.querySelectorAll(".input-box input");

    inputs.forEach((input) => {
        input.addEventListener("focus", function () {
            this.parentNode.classList.add("focused");
        });

        input.addEventListener("blur", function () {
            if (!this.value) {
                this.parentNode.classList.remove("focused");
            }
        });
    });
});
