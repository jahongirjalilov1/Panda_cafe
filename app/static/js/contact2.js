const contactForm = document.getElementById("contactForm");

contactForm.addEventListener("submit", function (event) {
    event.preventDefault();

    // Get form values
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const message = document.getElementById("message").value;

    // Do something with the form data (e.g., send it to a server using fetch or XMLHttpRequest)
    // For this example, we'll just log the data to the console
    console.log("Name: ", name);
    console.log("Email: ", email);
    console.log("Message: ", message);

    // Optionally, you can clear the form after submission
    contactForm.reset();
});
