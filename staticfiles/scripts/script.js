document.addEventListener("DOMContentLoaded", function() {
  const showPasswordCheckbox = document.getElementById("showPassword");
  const passwordField = document.getElementById("password");

  showPasswordCheckbox.addEventListener("change", function() {
    if (this.checked) {
      passwordField.setAttribute("type", "text");
    } else {
      passwordField.setAttribute("type", "password");
    }
  });
});
