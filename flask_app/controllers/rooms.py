from flask_app import app
from flask import request, jsonify, session
from flask_app.models import save
from flask_app.models import user
from flask_app.models import room

@app.route('/decision_interpreter', methods=['POST'])
def decision_interpreter():
    # print(request.form)
    decision = request.form['decision']
    decision = decision.lower()
    curr_room = session['room_id']
    # return jsonify({'display'})

    # Room 1: The Forge Ward 
    if curr_room == 1:
        if decision.find('look around') > -1:
            return jsonify({'display': 'I am in the Forge Ward. This is where us' \
                ' Hollow are put to endless work. Our masters seem to take advantage' \
                ' of my brethren’s lack of self. But I differ, I know that I am alive.' \
                ' But HOW do I differ?  Hm, I must bring this gift to my brethren. ' \
                ' But first, I must gather strength!'})
        return jsonify({'display': False})
    return jsonify (message = 'Hi')

    
    # Room 2: Auxiliary Supply

    # Room 3: Slop Withdraw

    # Room 4: Waste Deposit
