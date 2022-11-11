/* jshint esversion: 11 */
// toasts
let toastElList = [].slice.call(document.querySelectorAll('.toast'));
let toastList = toastElList.map(function (toastEl) {
    let option = {
        animation: true,
        autohide: false,
        delay: 5000,
    };
    let bsToast = toastList(toastEl, option);
    bsToast.show();
});
