const inst = document.querySelector("#inst");
const facebook = document.querySelector("#facebook");



inst.addEventListener("mouseover", (event) => {
    inst.style.color = "#faf5f5";
    inst.style.backgroundColor = "#4e574b";
    inst.style.cursor = "pointer";
});

inst.addEventListener("mouseout", (event) => {
    inst.style.backgroundColor = "#faf5f5";
    inst.style.color = "#4e574b";
});

inst.addEventListener("click", (event) => {
    window.location.replace("https://www.instagram.com/yaroslava_timchenko?igsh=MTNiOXR2cndtejQ3cA==");
})

facebook.addEventListener("mouseover", (event) => {
    facebook.style.color = "#faf5f5";
    facebook.style.backgroundColor = "#4e574b";
    facebook.style.cursor = "pointer";
});

facebook.addEventListener("mouseout", (event) => {
    facebook.style.backgroundColor = "#faf5f5";
    facebook.style.color = "#4e574b";
});

facebook.addEventListener("click", (event) => {
    window.location.replace("https://www.facebook.com/Yaroslava.Tymchenko5");
})



