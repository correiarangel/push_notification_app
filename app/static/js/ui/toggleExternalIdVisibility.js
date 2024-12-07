export function toggleExternalIdVisibility() {
    const externalIdField = document.getElementById('external_id');
    const externalIdLabel = document.getElementById('external_id_label');
    const isChecked = document.getElementById('check_all_users').checked;

    externalIdLabel.style.display = isChecked ? 'none' : 'block';
    externalIdField.style.display = isChecked ? 'none' : 'block';
}
