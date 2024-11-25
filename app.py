from flask import Flask, render_template, request, session, flash, make_response, jsonify

import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Rota principal
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Rota do formulário
@app.route('/form', methods=['GET'])
def form():
    session['log_output'] = ""  # Limpa log ao carregar a página
    return render_template('form.html', log_output=session.get('log_output'))

# Sessão e registro de logs
def log_to_session(message):
    if 'log_output' not in session:
        session['log_output'] = "..."
    session['log_output'] += message + "\n"
    
# Função para configurar dados de notificação para um usuário específico
def get_single_user_data(external_id):
    return {"include_aliases": {"external_id": [external_id]}}

# Função para configurar dados de notificação para todos os usuários
def get_all_users_data():
    return {"included_segments": ["All"]} 

# Função para processar a resposta do envio de notificação
def process_response(response):
    response_data = response.json()
    status_code = response.status_code
    log_to_session(f"{status_code} {response_data}")

    if status_code == 200:
        return jsonify({'status': 'success', 'log': session.get('log_output')}), 200
    else:
        return jsonify({'status': 'error', 'log': session.get('log_output'), 'errors': response_data.get('errors')}), status_code

def send_push_notification(api_key, app_id, message_pt, message_en, heading_en, heading_pt, all_users, external_id, small_icon, launch_url):
    url = "https://api.onesignal.com/notifications"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Basic {api_key}"
    }

    # Configura a notificação com base no checkbox all_users
    if all_users == 'on':
        data = get_all_users_data()
    else:
        data = {"include_aliases": {"external_id": [external_id]}} if external_id else {}

    data.update({
        "app_id": app_id,
        "contents": {"en": message_en, "pt": message_pt},
        "headings": {"en": heading_en, "pt": heading_pt},
        "small_icon": small_icon,
        "url": launch_url,  
        "target_channel": "push"
    })

    try:
        response = requests.post(url, headers=headers, json=data)
        response_data = response.json() if response.status_code == 200 else {"errors": response.text}
    except requests.exceptions.RequestException as e:
        response_data = {"errors": str(e)}
        response.status_code = 500

    log_to_session(f"{response.status_code} {response_data}")
    return response.status_code, response_data


@app.route('/send_notification', methods=['POST'])
def send_notification():
    session.update(
        app_id=request.form.get('app_id'),
        api_key=request.form.get('api_key'),
        message_pt=request.form.get('message_pt'),
        message_en=request.form.get('message_en'),
        heading_pt=request.form.get('heading_pt'),
        heading_en=request.form.get('heading_en'),
        small_icon=request.form.get('small_icon'),
        all_users=request.form.get('all_users'),
        external_id=request.form.get('external_id'),
        launch_url=request.form.get('launch_url') 
    )

    status_code, response = send_push_notification(
        api_key=session['api_key'],
        app_id=session['app_id'],
        message_pt=session['message_pt'],
        message_en=session['message_en'],
        heading_en=session['heading_en'],
        heading_pt=session['heading_pt'],
        all_users=session['all_users'],
        external_id=session['external_id'],
        small_icon=session['small_icon'],
        launch_url=session['launch_url']  # Passa o Launch URL para a função
    )

    if status_code == 200:
        return jsonify({'status': 'success', 'log': session.get('log_output')}), 200
    else:
        errors = response.get("errors", "Unknown error")
        return jsonify({'status': 'error', 'log': session.get('log_output'), 'errors': errors}), status_code




@app.route('/send_notification_to_all', methods=['POST'])
def send_notification_to_all():
    session.update(
        app_id=request.form.get('app_id'),
        api_key=request.form.get('api_key'),
        message_pt=request.form.get('message_pt'),
        message_en=request.form.get('message_en'),
        heading_pt=request.form.get('heading_pt'),
        heading_en=request.form.get('heading_en'),
        small_icon=request.form.get('small_icon'),
        all_users=request.form.get('all_users'),  # Adiciona o parâmetro all_users na sessão
         
    )

    # Chama a função de envio com o parâmetro `all_users=True`
    return send_push_notification(
     api_key=session['api_key'],
        app_id=session['app_id'],
        message_pt=session['message_pt'],
        message_en=session['message_en'],
        heading_en=session['heading_en'],
        heading_pt=session['heading_pt'],
        all_users=session['all_users'],
        external_id=session['external_id'],
        small_icon=session['small_icon']
    )


# Rota para página Sobre
@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


# Baixar logs
@app.route('/download_log', methods=['GET'])
def download_log():
    log_output = session.get('log_output', 'Sem logs disponíveis.')
    response = make_response(log_output)
    response.headers['Content-Disposition'] = 'attachment; filename=log_output.txt'
    response.headers['Content-Type'] = 'text/plain'
    return response


# Limpar sessão
@app.route('/clear_session', methods=['GET'])
def clear_session():
    session.clear()
    flash('Todos os dados da sessão foram apagados.', 'success')
    return '', 204


# Página de mensagens
@app.route('/messages', methods=['GET'])
def messages():
    return render_template('messages.html')

@app.route('/api/messages', methods=['GET'])
def get_messages():
    # Extrai o `api_key` e o `app_id` dos parâmetros e cabeçalhos da requisição
    api_key = request.headers.get('Authorization').replace("Basic ", "")
    app_id = request.args.get('app_id')
    url = f"https://onesignal.com/api/v1/notifications?app_id={app_id}"
    
    # Configura os cabeçalhos da requisição
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {api_key}"
    }
    
    # Faz a requisição para a API externa e registra o resultado na sessão
    try:
        response = requests.get(url, headers=headers)
        
        # Verifica e processa a resposta
        if response.status_code == 200:
            notifications = response.json().get('notifications', [])
            messages = [{"text": notification.get("contents", {}).get("en", "Mensagem sem conteúdo")}
                        for notification in notifications]
            
            # Log de sucesso
            log_to_session(f"{messages}")
            return {"messages": messages}, 200
        else:
            # Log de erro na resposta
            log_to_session(f"Failed to retrieve messages - Status Code: {response.status_code}")
            log_to_session(f"Response Error: {response.text}")
            return {"error": "Failed to retrieve messages."}, response.status_code
    
    except requests.exceptions.RequestException as e:
        # Log de erro na exceção
        log_to_session(f"RequestException: {str(e)}")
        return {"error": "Request failed due to an exception."}, 500


# Executar aplicativo
if __name__ == '__main__':
    app.run(debug=True)
