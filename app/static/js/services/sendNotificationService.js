// Função para enviar a notificação ao servidor
export function sendNotificationService(formData) {
    return fetch('/send_notification', {
        method: 'POST',
        body: formData,
    })
        .then(response => {
            if (response.ok && response.headers.get("Content-Type").includes("application/json")) {
                return response.json();
            } else {
                throw new Error('Resposta não é JSON');
            }
        });
}
