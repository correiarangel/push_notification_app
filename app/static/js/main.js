// Outras funções permanecem inalteradas
document.getElementById('notification-form')?.addEventListener('submit', function (event) {
    event.preventDefault();
    showLoadingDialog();

    const formData = new FormData(this);

    // Captura o valor do checkbox
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
document.addEventListener('DOMContentLoaded', () => {
    const checkAllUsers = document.getElementById('check_all_users');
    if (checkAllUsers) {
        checkAllUsers.addEventListener('change', toggleExternalIdVisibility);
    }
});


function toggleExternalIdVisibility() {
    const externalIdField = document.getElementById('external_id');
    const externalIdLabel = document.getElementById('external_id_label');
    const isChecked = document.getElementById('check_all_users').checked;
    externalIdField.style.display = isChecked ? 'none' : 'block';
    externalIdLabel.style.display = isChecked ? 'none' : 'block';
}


// Outras funções existentes
function updateConsoleLog(message) {
    const consoleLogElement = document.getElementById('console-log');
    consoleLogElement.textContent += message + '\n';
    consoleLogElement.scrollTop = consoleLogElement.scrollHeight;
}

function clearFields() {
    const fields = ['app_id', 'api_key', 'message_pt', 'message_en', 'heading_pt', 'heading_en', 'external_id', 'small_icon'];
    console.log('click clearFields................')
    // Limpar os campos se eles existirem no DOM
    fields.forEach(fieldId => {
        const field = document.getElementById(fieldId);
        if (field) {
            field.value = ''; // Limpa o valor do input
        }
    });

    // Desmarcar o checkbox, se ele existir
    const checkAllUsers = document.getElementById('check_all_users');
    if (checkAllUsers) {
        checkAllUsers.checked = false; // Desmarca o checkbox
        toggleExternalIdVisibility(); // Atualiza a visibilidade do campo "external_id"
    }
}


function clearAll() {
    // Limpa todos os campos de input e checkboxes
    console.log('click clearAll................')
    clearFields();

    // Limpa o console log
    const consoleLogElement = document.getElementById('console-log');
    if (consoleLogElement) {
        consoleLogElement.textContent = ''; // Reseta o conteúdo do log
    }

    // Remove os cards de mensagens
    const messagesContainer = document.getElementById('messages-container');
    if (messagesContainer) {
        messagesContainer.innerHTML = ''; // Remove todos os elementos dentro do container
    }

    // Esconde o cabeçalho de lista de mensagens, se existir
    const listHeader = document.getElementById('list-header');
    if (listHeader) {
        listHeader.style.display = 'none'; // Esconde o cabeçalho
    }
}


function clearSession(method) {

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