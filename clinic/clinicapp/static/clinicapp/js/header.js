const checkBtn = document.querySelector(".checkbtn");
const check =  document.querySelector("#check");

checkBtn.addEventListener("click", (event) => {
    check.classList.toggle("checked");
})