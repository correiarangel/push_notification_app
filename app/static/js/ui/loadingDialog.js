export function showLoadingDialog() {
    const loadingDialog = document.getElementById("loading-dialog");

        loadingDialog.style.display = "flex";

}

export function hideLoadingDialog() {
    const loadingDialog = document.getElementById("loading-dialog");
        loadingDialog.style.display = "none";
}
