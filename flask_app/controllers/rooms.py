from flask_app import app
from flask import json, request, jsonify, session
from flask_app.models import save
from flask_app.models import user
from flask_app.models import room

@app.route('/decision_interpreter', methods=['POST'])
def decision_interpreter():
    decision = request.form['decision']
    decision = decision.lower()
    curr_room = session['room_id']

    # Lighthearted profanity filter
    if decision.find('ass') > -1 and not decision.find('assembly') > -1:
            if decision.find('ass') > -1:
                return jsonify({'display': 'Naughty, naughty!'})
    # Room 1: The Forge Ward 
    elif curr_room == 1:
        if decision.find('look around') > -1:
            return jsonify({'display': 'I am in the Forge Ward. This is where us' \
                ' Hollow are put to endless work. Our masters seem to take advantage' \
                ' of my brethren’s lack of self. But I differ, I know that I am alive.' \
                ' But HOW do I differ?  Hm, I must bring this gift to my brethren. ' \
                ' But first, I must gather strength! Maybe I can find something ' \
                ' useful here...<br></br> I am at the assembly line, with one of ' \
                ' my fellow Hollow on my left and right, continuing to work as I devise my plans.' \
                ' I have access to the supply room, Nutrio, and the Innervation Ward' \
                ''})
        elif decision.find('examine') > -1:
            if decision.find('assembly') > -1 or decision.find('line') > -1:
                return jsonify({'display': 'I see a partially assembled Vital Cube.'})
            elif decision.find('left') > -1 or decision.find('right') > -1 or decision.find('hollow') > -1:
                if decision.find('left') > -1 and decision.find('hollow') > -1:
                    return jsonify({'display' : "A fellow Hollow, this one is noticeably " \
                        "short in stature. They have a greenish-blueish hue to their " \
                        "dark grey skin. Their eyes are large and oval as mine are, heavily  " \
                        "encased in dried mucus. Their hair is long and very wild, " \
                        "wholly white in color. Their shoulders are narrow, slumped over, and " \
                        " belly round and emaciated at the same time. It would take a handful of Hollow like them " \
                        "to match the dominating build and presence of any one Gerent."})
                elif decision.find('right') > -1 and decision.find('hollow') > -1:
                    return jsonify({'display': "This Hollow is similar in height to me. " \
                        "This one seems remarkably healthy when compared to the Hollow " \
                        "on my right. "
                        })
                else:
                    return jsonify({'display': "The Hollow to my left and right continue " \
                        "to slave away without any sense of self."})
            elif decision.find('plans') > -1 :
                return jsonify({'display': "I need to find out how my mind came to be. " \
                    "I must look around this place with a fresh view. After, I should " \
                    "have what I need to free my kin. But I must also consider " \
                    "protecting them once they awaken. Of course, I also have to " \
                    "deal with Gerent. Something tells me they have no reason to " \
                    "ever expect a sudden awakening of the Hollow."})
            elif decision.find('cube') > -1 or decision.find('vital cube') > -1 :
                return jsonify({'display': "I've realized I have absolutely no " \
                    "idea what this cube even does. All I know is that it must " \
                    "be extremely valuable in some way to the Gerent. At this " \
                    "in the assembly, it is far from complete, though most of " \
                    "its primary components are at least present in some way " \
                    "from what I can remember during my prior placements."})
            else:
                return jsonify({'display': 'Unknown "Examine" target!'})
        elif decision.find('speak') > -1 or decision.find('talk') > -1:
            if decision.find('left') > -1:
                return jsonify({'display': "Urgglhhsthgh..."})
            elif decision.find('right') > -1 :
                return jsonify({'display': "Uhhhhhghhghh"})
            else:
                return jsonify({'display': 'Unknown "Speak/Talk" target!'})
        return jsonify({'display': False})
    return jsonify (message = 'Hi')

    
    # Room 2: Auxiliary Supply

    # Room 3: Slop Withdraw

    # Room 4: Waste Deposit
