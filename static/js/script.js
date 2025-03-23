document.addEventListener("DOMContentLoaded", function () {
    const hamburger = document.getElementById("hamburger");
    const navlist = document.getElementById("navlist");

    hamburger.addEventListener("click", function () {
        navlist.classList.toggle("active"); // Toggle the 'active' class on the navlist
    });
});