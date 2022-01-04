import os
from flask import Flask, render_template, request, session
from .marvin import Marvin

def create_app():
    app = Flask(__name__)
    
    app.secret_key = os.urandom(12).hex()

    marvin = Marvin()
    
    @app.route('/')
    def root():
        return render_template('base.html')

    @app.route("/get")
    def get_bot_response():    
        msg = request.args.get('msg')
        chat_log = session.get('chat_log')
        answer = str(marvin.ask(msg, chat_log))

        session['chat_log'] = marvin.append_interaction_to_chat_log(msg, answer, chat_log)
        return str(answer) 
    
    return app
