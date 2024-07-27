const btnAbout = document.querySelector("#find-about");
const btnService = document.querySelector("#find-service");

btnAbout.addEventListener("click", () => {
    window.location.replace("/about");
});

btnService.addEventListener("click", () => {
    window.location.replace("/form");
})

