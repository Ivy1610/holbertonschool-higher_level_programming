document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('red_header').addEventListener("click", function () {
        const header = document.querySelector('header');
        if (header.classList.contains('red')) {
            header.classList.remove('red');
            header.classList.add('green');
        } else {
            header.classList.add('red');
            header.classList.remove('green');
        }
    });
});
