const instFooter = document.querySelector("#inst-footer");
const facebookFooter = document.querySelector("#facebook-footer");

instFooter.addEventListener("mouseover", (event) => {
    instFooter.style.backgroundColor = "#faf5f5";
    instFooter.style.color = "#4e574b";
    instFooter.style.cursor = "pointer";
});

instFooter.addEventListener("mouseout", (event) => {
    instFooter.style.color = "#faf5f5";
    instFooter.style.backgroundColor = "#4e574b";
});

instFooter.addEventListener("click", (event) => {
    window.location.replace("https://www.instagram.com/yaroslava_timchenko?igsh=MTNiOXR2cndtejQ3cA==");
})

facebookFooter.addEventListener("mouseover", (event) => {
    facebookFooter.style.backgroundColor = "#faf5f5";
    facebookFooter.style.color = "#4e574b";
    facebookFooter.style.cursor = "pointer";
});

facebookFooter.addEventListener("mouseout", (event) => {
    facebookFooter.style.color = "#faf5f5";
    facebookFooter.style.backgroundColor = "#4e574b";
});

facebookFooter.addEventListener("click", (event) => {
    window.location.replace("https://www.facebook.com/Yaroslava.Tymchenko5");
})