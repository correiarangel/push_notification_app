#Contem todas as rotas relacionadas a notificações
from flask import Blueprint, request, session, jsonify
from services.notification_service import send_push_notification, get_messages_from_api

notification_bp = Blueprint('notification', __name__)

@notification_bp.route('/send_notification', methods=['POST'])
def send_notification():
    # Atualiza a sessão com dados do formulário
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

    # Envia a notificação
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
        launch_url=session['launch_url']
    )

    if status_code == 200:
        return jsonify({'status': 'success', 'log': session.get('log_output')}), 200
    else:
        return jsonify({'status': 'error', 'log': session.get('log_output'), 'errors': response.get("errors", "Unknown error")}), status_code


@notification_bp.route('/api/messages', methods=['GET'])
def get_messages():
    api_key = request.headers.get('Authorization').replace("Basic ", "")
    app_id = request.args.get('app_id')
    return get_messages_from_api(api_key, app_id)
