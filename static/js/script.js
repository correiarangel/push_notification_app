document.getElementById('notification-form')?.addEventListener('submit', function (event) {
    event.preventDefault();
    showLoadingDialog();  // Exibe o loading

    const formData = new FormData(this);

    // Captura o valor do checkbox para enviar ao servidor
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
});

// Função para ocultar o campo external_id quando o checkbox está marcado
document.getElementById('check_all_users').addEventListener('change', toggleExternalIdVisibility);

function toggleExternalIdVisibility() {
    const externalIdField = document.getElementById('external_id');
    const externalIdLabel = document.getElementById('external_id_label');
    externalIdLabel.style.display = document.getElementById('check_all_users').checked ? 'none' : 'block';
    externalIdField.style.display = document.getElementById('check_all_users').checked ? 'none' : 'block';
}


// Outras funções existentes
function updateConsoleLog(message) {
    const consoleLogElement = document.getElementById('console-log');
    consoleLogElement.textContent += message + '\n';
    consoleLogElement.scrollTop = consoleLogElement.scrollHeight;
}

function clearField(fieldId) {
    document.getElementById(fieldId).value = '';
    document.getElementById('check_all_users').checked = false;
    toggleExternalIdVisibility();

}

function clearAll() {
    document.getElementById('check_all_users').checked = false;
    const fields = ['app_id', 'api_key', 'message_pt', 'message_en', 'heading_pt', 'heading_en', 'external_id', 'small_icon'];
    fields.forEach(clearField);
}

function clearSession() {
    fetch('/clear_session', { method: 'POST' })
        .then(response => {
            if (response.ok) {
                alert('Session data cleared!');
                clearAll();
            } else {
                alert('Failed to clear session data.');
            }
        })
        .catch(error => console.error('Error:', error));
}

function downloadLog() {
    window.location.href = "/download_log";
}

// Função para rolar para o topo da página
function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Função para buscar mensagens usando app_id e api_key
async function fetchMessages(event) {
    event.preventDefault();  // Evita o recarregamento da página

    const appId = document.getElementById("app_id").value;
    const apiKey = document.getElementById("api_key").value;
    const messagesContainer = document.getElementById("messages-container");
    const listHeader = document.getElementById("list-header");

    // Inicializa o diálogo de carregamento
    showLoadingDialog();

    // Limpa o cabeçalho e o container de mensagens
    listHeader.style.display = "none";
    messagesContainer.innerHTML = "";  // Limpa o conteúdo anterior

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
            // Exibe o cabeçalho e o container apenas se houver mensagens
            listHeader.style.display = "block";

            messages.forEach(message => {
                // Atualiza o log original
                updateConsoleLog(message.text || "Mensagem sem conteúdo");

                // Cria um card para cada mensagem
                const messageCard = document.createElement("div");
                messageCard.classList.add("message-card");
                messageCard.textContent = message.text || "Mensagem sem conteúdo";
                messagesContainer.appendChild(messageCard);
            });
        }
    } catch (error) {
        updateConsoleLog("Erro ao buscar mensagens: " + error.message);
    } finally {
        // Oculta o diálogo de carregamento após a resposta da API
        hideLoadingDialog();
    }
}

// Função para mostrar o diálogo de carregamento
function showLoadingDialog() {
    document.getElementById("loading-dialog").style.display = "flex";
}

// Função para esconder o diálogo de carregamento
function hideLoadingDialog() {
    document.getElementById("loading-dialog").style.display = "none";
}


