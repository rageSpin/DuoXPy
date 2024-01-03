import os
import requests
import json
import base64
import time
import shutil
from configparser import ConfigParser
from getpass import getpass

config_folder: str = 'Config'
config_path: str = f'{config_folder}/DuoXPyConfig.txt'

config: ConfigParser = ConfigParser()
config.read(config_path)

print("------- Welcome to DuoXPy -------")
print("Made by GFx")
if os.getenv('GITHUB_ACTIONS') == 'true':
    print("Powered by GitHub Actions V3 and Python")
    print("Run with GitHub Actions: Yes")
    print(f"Current repo: {os.getenv('GITHUB_REPOSITORY')}")
    user_repo = os.getenv('GITHUB_REPOSITORY')
    ORIGINAL_REPO = 'gorouflex/DuoXPy'
    user_url = f'https://api.github.com/repos/{user_repo}/commits/main'
    original_url = f'https://api.github.com/repos/{ORIGINAL_REPO}/commits/main'
    user_response = requests.get(user_url, timeout=10000)
    original_response = requests.get(original_url, timeout=10000)
    if user_response.status_code == 200 and original_response.status_code == 200:
        user_commit = user_response.json()['sha']
        original_commit = original_response.json()['sha']
        if user_commit == original_commit:
            print("Your repo is up-to-date with the original repo")
        else:
            print("Your repo is not up-to-date with the original repo")
            print("Please update your repo to the latest commit to get new updates and bug fixes")
    else:
        print("--------- Traceback log ---------\n❌ Error code 4: Failed to fetch commit information\n"
              "Please refer to: https://github.com/gorouflex/HoneygainPot/blob/main/Docs/Debug.md "
              "for more information\nOr create an Issue on GitHub if it still doesn't work for you.")
        exit(-1)
    print(f"Lessons: {os.getenv('LESSONS')}")
else:
    print("Run with GitHub Actions: No")
    try:
        lessons = config.get('User', 'LESSONS')
        print(f"Lessons: {lessons}")
    except:
        print("Lessons: N/A")
print("Codename: Sandy")
print(f"Config folder: {os.path.join(os.getcwd(), 'Config')}")
print("---------------------------------")
print("Starting DuoXPy")
print("Collecting information...")

def create_config() -> None:
    config.add_section('User')
    config.set('User', 'TOKEN', "")
    if os.getenv('GITHUB_ACTIONS') == 'true':
        token = os.getenv('JWT_TOKEN')
        config.set('User', 'TOKEN', f"{token}")
        lessons = os.getenv('LESSONS')
        config.set('User', 'LESSONS', f"{lessons}")
    else:
        token = getpass("Token: ")
        config.set('User', 'TOKEN', f"{token}")
        lessons = getpass("Lesson: ")
        config.set('User', 'LESSONS', f"{lessons}")
    with open(config_path, 'w', encoding='utf-8') as configfile:
        configfile.truncate(0)
        configfile.seek(0)
        config.write(configfile)

def check_config_integrity() -> None:
    if not os.path.exists(config_folder):
        print("Creating new config folder at:", os.path.join(os.getcwd()))
        os.mkdir(config_folder)

    if not os.path.isfile(config_path) or os.stat(config_path).st_size == 0:
        create_config()
        return

    config.read(config_path)

    if not config.has_section('User') or not config.has_option('User', 'TOKEN') or not config.has_option('User', 'LESSONS'):
        create_config()

check_config_integrity()
config.read(config_path)

try:
    token = config.get('User', 'TOKEN')
    lessons = config.get('User', 'LESSONS')
except:
    create_config()

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token,
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

try:
    jwt_token = token.split('.')[1]
except:
    print("--------- Traceback log ---------\n❌ Invalid token")
    exit(-1)

padding = '=' * (4 - len(jwt_token) % 4)
sub = json.loads(base64.b64decode(jwt_token + padding).decode())

response = requests.get(
    f"https://www.duolingo.com/2017-06-30/users/{sub['sub']}?fields=fromLanguage,learningLanguage,xpGains",
    headers=headers,
)
data = response.json()
fromLanguage = data['fromLanguage']
learningLanguage = data['learningLanguage']
xpGains = data['xpGains']

xpGain = xpGains[-1]
skillId = xpGain['skillId']

if skillId is None:
    print("No skillId found in xpGains\nPlease do at least 1 or 9 lessons")
    exit(1)

for i in range(int(lessons)):
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
        'skillId': skillId,
        'smartTipsVersion': 2,
        'type': 'SPEAKING_PRACTICE',
    }

    session_response = requests.post('https://www.duolingo.com/2017-06-30/sessions', json=session_data, headers=headers)
    if session_response.status_code == 500:
        print("Session Error 500 - No skillId found in xpGains\nPlease do at least 1 or 9 lessons")
        exit(-1)
    elif session_response.status_code != 200:
        print(f"Session Error: {session_response.status_code}, {session_response.text}")
        continue
    session = session_response.json()

    end_response = requests.put(
        f"https://www.duolingo.com/2017-06-30/sessions/{session['id']}",
        headers=headers,
        json={
            **session,
            'heartsLeft': 0,
            'startTime': (time.time() - 60),
            'enableBonusPoints': False,
            'endTime': time.time(),
            'failed': False,
            'maxInLessonStreak': 9,
            'shouldLearnThings': True,
        },
    )

    try:
        end_data = end_response.json()
    except json.decoder.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        print(f"Response content: {end_response.text}")
        continue

    response = requests.put(f'https://www.duolingo.com/2017-06-30/sessions/{session["id"]}', data=json.dumps(end_data), headers=headers)
    if response.status_code == 500:
        print("Response Error 500 - No skillId found in xpGains\nPlease do at least 1 or 9 lessons")
        exit(-1)
    elif response.status_code != 200:
        print(f"Response Error: {response.status_code}, {response.text}")
        continue
    print(f"[{i+1}] - Gained: {end_data['xpGain']} XP (✓)")

if os.getenv('GITHUB_ACTIONS') == 'true':
    try:
        shutil.rmtree(config_folder)
        print("Cleaning up..")
    except Exception as e:
        print(f"Error deleting config folder: {e}")
        exit(-1)

print("Closing DuoXPy ✅")
