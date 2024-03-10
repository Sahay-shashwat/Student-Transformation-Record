const form = document.getElementById("form");
form.addEventListener('submit', function(event) {
    event.preventDefault();
    var flash_message = '{{ flash() }}';
    if (flash_message) {
        console.log(flash_message);
        alert(flash_message);
    }
});