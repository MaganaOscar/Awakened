from flask_app import app
from flask import request, jsonify
from flask_app.models import save
from flask_app.models import user
from flask_app.models import room

@app.route('/decision_interpreter', methods=['POST'])
def decision_interpreter():
    # print(request.form)
    decision = request.form['decision']
    return jsonify({'test': 'hello'})