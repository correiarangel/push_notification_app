from flask import Blueprint,render_template, session

page_bp = Blueprint('page',__name__)

@page_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@page_bp.route('/form', methods=['GET'])
def form():
    session['log_output'] = "" # clean logs
    return render_template('form.html', log_output=session.get('log_output'))

@page_bp.route('/about', methods=['GET'])
def about():
   return render_template('about.html')

@page_bp.route('/messages', methods=['GET'])
def messages():
   return render_template('messages.html')