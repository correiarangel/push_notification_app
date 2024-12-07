from flask import Blueprint, session,make_response,flash

utility_bp = Blueprint('utility',__name__)

@utility_bp.route('/download_log',methods=['GET'])
def download_log():
    
    log_output = session.get('log_output', 'Sem logs disponíveis.')
    response = make_response(log_output)
    response.headers['Content-Disposition'] = 'attachment; filename=log_output.txt'
    response.headers['Content-Type'] = 'text/plain'
    return response

@utility_bp.route('/clear_session',methods=['GET','POST'])
def clear_session():
    session.clear()
    flash('Todos os dados da sessão foram apagados.', 'success')
    return '',204