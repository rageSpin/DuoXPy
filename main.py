import os
import requests
import json
import base64
import time
from configparser import ConfigParser
from getpass import getpass

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WHITE = '\033[97m'

config_folder: str = 'Config'
config_path: str = f'{config_folder}/DuoXPyConfig.txt'

config: ConfigParser = ConfigParser()
config.read(config_path)

print(f"{colors.WARNING}------- Welcome to DuoXPy -------{colors.ENDC}")
print(f"{colors.OKBLUE}Made by GFx{colors.ENDC}")
if os.getenv('GITHUB_ACTIONS') == 'true':
    print(f"{colors.OKBLUE}Powered by GitHub Actions V3 and Python{colors.ENDC}")
    print(f"{colors.OKGREEN}Run with GitHub Actions: Yes{colors.ENDC}")
    print(f"{colors.WHITE}Current repo: {os.getenv('GITHUB_REPOSITORY')}{colors.ENDC}")
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
            print(f"{colors.OKGREEN}Your repo is up-to-date with the original repo{colors.ENDC}")
        else:
            print(f"{colors.WARNING}Your repo is not up-to-date with the original repo{colors.ENDC}")
            print(f"{colors.FAIL}Please update your repo to the latest commit{colors.ENDC}{colors.FAIL}to get new updates and bug fixes{colors.ENDC}")
    else:
        print(f"{colors.WARNING}--------- Traceback log ---------{colors.ENDC}\n{colors.FAIL}❌ Error code 4: Failed to fetch commit information\nPlease refer to: https://github.com/gorouflex/HoneygainPot/blob/main/Docs/Debug.md for more information\nOr create an Issue on GitHub if it still doesn't work for you.{colors.ENDC}")
        exit(-1)
    print(f"{colors.WARNING}Lessons: {os.getenv('LESSONS')}{colors.ENDC}")
else:
    print(f"{colors.FAIL}Run with GitHub Actions: No{colors.ENDC}")
    try:
      lessons = config.get('User', 'LESSONS')
      print(f"{colors.WARNING}Lessons: {lessons}{colors.ENDC}")
    except:
      print(f"{colors.WARNING}Lessons: N/A{colors.ENDC}")
print(f"{colors.WHITE}Codename: Sandy{colors.ENDC}")
print(f"{colors.WHITE}Config folder:", os.path.join(os.getcwd(), f"{colors.WHITE}Config{colors.ENDC}"))
print(f"{colors.WARNING}---------------------------------{colors.ENDC}")
print(f"{colors.WHITE}Starting DuoXPy{colors.ENDC}")
print(f"{colors.WHITE}Collecting information...{colors.ENDC}")

def create_config() -> None:
    config.add_section('User')
    config.set('User', 'TOKEN', "")
    if os.getenv('GITHUB_ACTIONS') == 'true':
        token = os.getenv('JWT_TOKEN')
        config.set('User', 'TOKEN', f"{token}")
        lessons = os.getenv('LESSONS')
        config.set('User', 'LESSONS', f"{lessons}")
    else:
        token = getpass(f"{colors.WHITE}Token: {colors.ENDC}")
        config.set('User', 'TOKEN', f"{token}")
        lessons = getpass(f"{colors.WHITE}Lesson: {colors.ENDC}")
        config.set('User', 'LESSONS', f"{lessons}")
    with open(config_path, 'w', encoding='utf-8') as configfile:
        configfile.truncate(0)
        configfile.seek(0)
        config.write(configfile)

def check_config_integrity() -> None:
    if not os.path.exists(config_folder):
        print(f"{colors.WARNING}Creating new config folder at:", os.path.join(os.getcwd()))
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
  print(f"{colors.WARNING}--------- Traceback log ---------{colors.ENDC}\n{colors.FAIL}❌ Invaild token{colors.ENDC}")
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
    print(f"{colors.FAIL}No skillId found in xpGains\nPlease do at least 1 or 9 lessons{colors.ENDC}")
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
         print(f"{colors.FAIL}Session Error 500 - No skillId found in xpGains\nPlease do at least 1 or 9 lessons{colors.ENDC}")
         exit(-1)
    elif session_response.status_code != 200:
         print(f"{colors.FAIL}Session Error: {session_response.status_code}, {session_response.text}{colors.ENDC}")
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
        print(f"{colors.FAIL}Error decoding JSON: {e}{colors.ENDC}")
        print(f"Response content: {end_response.text}")
        continue

    response = requests.put(f'https://www.duolingo.com/2017-06-30/sessions/{session["id"]}', data=json.dumps(end_data), headers=headers)
    if response.status_code == 500:
         print(f"{colors.FAIL}Response Error 500 - No skillId found in xpGains\nPlease do at least 1 or 9 lessons{colors.ENDC}")
         exit(-1)
    elif response.status_code != 200:
         print(f"{colors.FAIL}Response Error: {response.status_code}, {response.text}{colors.ENDC}")
         continue
    print(f"{colors.OKGREEN}[{i+1}] - Gained: {end_data['xpGain']} XP (✓){colors.ENDC}")
