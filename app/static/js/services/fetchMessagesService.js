import { updateConsoleLog } from '../ui/updateConsoleLog.js';
import { showLoadingDialog, hideLoadingDialog } from '../ui/loadingDialog.js';


export async function fetchMessages(event) {
    event.preventDefault();

    const appId = document.getElementById("app_id").value;
    const apiKey = document.getElementById("api_key").value;
    const messagesContainer = document.getElementById("messages-container");
    const listHeader = document.getElementById("list-header");

    showLoadingDialog();

    listHeader.style.display = "none";
    messagesContainer.innerHTML = "";

    try {
        const response = await fetch(`/api/messages?app_id=${appId}`, {
            headers: {
                "Authorization": `Basic ${apiKey}`
            }
        });

        if (!response.ok) throw new Error('Failed to fetch messages');

        const data = await response.json();
        const messages = data.messages || [];

        if (messages.length > 0) {
            listHeader.style.display = "block";

            messages.forEach(message => {
                updateConsoleLog(message.text || "Mensagem sem conteúdo");

                const messageCard = document.createElement("div");
                messageCard.classList.add("message-card");
                messageCard.textContent = message.text || "Mensagem sem conteúdo";
                messagesContainer.appendChild(messageCard);
            });
        }
    } catch (error) {
        updateConsoleLog("Erro ao buscar mensagens: " + error.message);
    } finally {
        hideLoadingDialog();
    }
}
