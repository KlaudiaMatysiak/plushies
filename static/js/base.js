/* jshint esversion: 11 */
// toasts
Array.from(document.querySelectorAll('.toast')).map(toastEl => {
    const option = {
        animation: true,
        autohide: false,
        delay: 5000,
    }
    const bsToast = new bootstrap.Toast(toastEl, option)
    bsToast.show();
});
