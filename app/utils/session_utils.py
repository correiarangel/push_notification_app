from flask import session

def log_to_session(message):
    if 'log_output' not in session:
        session['log_output'] = "" 
    session['log_output'] += message + "\n"