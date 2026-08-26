// Login form
const loginForm = document.getElementById("loginForm");

if (loginForm) {
    loginForm.addEventListener("submit", function(event) {
        event.preventDefault();

        alert("Login submitted.");
    });
}


// Registration form
const registerForm = document.getElementById("registerForm");

if (registerForm) {
    registerForm.addEventListener("submit", function(event) {
        event.preventDefault();

        const password = document.getElementById("password").value;
        const confirmPassword =
            document.getElementById("confirmPassword").value;

        if (password !== confirmPassword) {
            alert("Passwords do not match.");
            return;
        }

        alert("Registration submitted.");
    });
}


// Crop analysis form
const cropForm = document.getElementById("cropForm");

if (cropForm) {
    cropForm.addEventListener("submit", function(event) {
        event.preventDefault();

        window.location.href = "results.html";
    });
}