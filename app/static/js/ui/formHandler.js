import { showLoadingDialog, hideLoadingDialog } from '../loadingDialog.js';
import { updateConsoleLog } from './updateConsoleLog.js';

export function submitNotificationForm(event) {
    event.preventDefault();
    showLoadingDialog();

    const formData = new FormData(event.target);

    formData.append('all_users', document.getElementById('check_all_users').checked);
    formData.append('launch_url', document.getElementById('launch_url').value);

    fetch('/send_notification', {
        method: 'POST',
        body: formData,
    })
        .then(response => {
            if (response.ok && response.headers.get("Content-Type").includes("application/json")) {
                return response.json();
            } else {
                throw new Error('Resposta não é JSON');
            }
        })
        .then(data => {
            if (data.log) {
                updateConsoleLog(data.log);
            } else {
                throw new Error('Formato inesperado de resposta');
            }
        })
        .catch(error => updateConsoleLog('Error: ' + error.message))
        .finally(() => hideLoadingDialog());
}
