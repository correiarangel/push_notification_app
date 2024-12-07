// Função para atualizar o console log
export function updateConsoleLog(message) {
    const consoleLogElement = document.getElementById('console-log');
    consoleLogElement.textContent += message + '\n';
    consoleLogElement.scrollTop = consoleLogElement.scrollHeight;
}
