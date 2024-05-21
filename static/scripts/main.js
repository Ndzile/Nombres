// Alert message on document load
document.addEventListener("DOMContentLoaded", function() {
    alert("Welcome to the website!");
  });
  
  // Example function to manipulate the DOM
  function changeHeadingText() {
    const heading = document.querySelector("h1");
    heading.textContent = "This heading text is changed from JavaScript!";
  }
  
  // Call the function on a button click (assuming you have a button with id="change-heading")
  const changeButton = document.getElementById("change-heading");
  if (changeButton) {
    changeButton.addEventListener("click", changeHeadingText);
  }
  