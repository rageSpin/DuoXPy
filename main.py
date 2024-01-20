import requests
import json
import base64
import time
import os

headers = {
    'Content-Type': 'application/json',
    'Authorization': f"Bearer {os.environ['DUOLINGO_JWT']}",
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

jwt_payload = os.environ['JWT_TOKEN'].split('.')[1]
decoded_jwt = base64.b64decode(jwt_payload).decode('utf-8')
jwt_data = json.loads(decoded_jwt)
sub = jwt_data['sub']

response = requests.get(f"https://www.duolingo.com/2017-06-30/users/{sub}?fields=fromLanguage,learningLanguage,xpGains", headers=headers)
data = response.json()
fromLanguage = data['fromLanguage']
learningLanguage = data['learningLanguage']
xpGains = data['xpGains']

for i in range(int(os.environ['LESSONS'])):
    session_data = {
        'challengeTypes': [
            'assist',
            'characterIntro',
            'characterMatch',
            'characterPuzzle',
            'characterSelect',
            'characterTrace',
            'completeReverseTranslation',
            'definition',
            'dialogue',
            'form',
            'freeResponse',
            'gapFill',
            'judge',
            'listen',
            'listenComplete',
            'listenMatch',
            'match',
            'name',
            'listenComprehension',
            'listenIsolation',
            'listenTap',
            'partialListen',
            'partialReverseTranslate',
            'readComprehension',
            'select',
            'selectPronunciation',
            'selectTranscription',
            'syllableTap',
            'syllableListenTap',
            'speak',
            'tapCloze',
            'tapClozeTable',
            'tapComplete',
            'tapCompleteTable',
            'tapDescribe',
            'translate',
            'typeCloze',
            'typeClozeTable',
            'typeCompleteTable',
        ],
        'fromLanguage': fromLanguage,
        'isFinalLevel': False,
        'isV2': True,
        'juicy': True,
        'learningLanguage': learningLanguage,
        'skillId': next((xpGain['skillId'] for xpGain in xpGains if 'skillId' in xpGain), None),
        'smartTipsVersion': 2,
        'type': 'SPEAKING_PRACTICE'
    }

    session_response = requests.post('https://www.duolingo.com/2017-06-30/sessions', json=session_data, headers=headers)
    session = session_response.json()

    session['heartsLeft'] = 0
    session['startTime'] = (int(time.time()) - 60) / 1000
    session['enableBonusPoints'] = False
    session['endTime'] = int(time.time()) / 1000
    session['failed'] = False
    session['maxInLessonStreak'] = 9
    session['shouldLearnThings'] = True

    response = requests.put(f"https://www.duolingo.com/2017-06-30/sessions/{session['id']}", json=session, headers=headers)
    response_data = response.json()

    print({'xp': response_data['xpGain']})


