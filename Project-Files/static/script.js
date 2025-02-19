// Get form and input elements
const form = document.querySelector('form');
const username = document.getElementById('username');
const password = document.getElementById('password');

// Add event listener for form submission
form.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form from submitting normally

    // Validate inputs
    if (validateInputs()) {
        alert('Form submitted successfully!');
        form.submit(); 
    }
});

function validateInputs() {
    let valid = true;
    if (username.value.trim() === '') {
        alert('Username is required');
        valid = false;
    }

    if (password.value.trim() === '') {
        alert('Password is required');
        valid = false;
    }

    return valid;
}
