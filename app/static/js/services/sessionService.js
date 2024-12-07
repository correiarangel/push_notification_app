import { toggleExternalIdVisibility } from '../ui/toggleExternalIdVisibility'

export function clearFields() {
    const fields = [
        'app_id',
        'api_key',
        'message_pt',
        'message_en',
        'heading_pt',
        'heading_en',
        'external_id',
        'small_icon',
        'launch_url',
    ];

    fields.forEach(fieldId => {
        const field = document.getElementById(fieldId);
        if (field) field.value = '';
    });

    const checkAllUsers = document.getElementById('check_all_users');
    if (checkAllUsers) checkAllUsers.checked = false;

    toggleExternalIdVisibility();
}

export function clearSession(method) {

    fetch('/clear_session', { method: method })
        .then(response => {
            if (response.ok) {
                alert('Session data cleared!');
            } else {
                alert('Failed to clear session data.');
            }
        })
        .catch(error => console.error('Error:', error));
}
