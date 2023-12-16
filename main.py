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
else:
    print(f"{colors.FAIL}Run with GitHub Actions: No{colors.ENDC}")
print(f"{colors.WHITE}Codename: Sandy{colors.ENDC}")
print(f"{colors.WHITE}Config folder:", os.path.join(os.getcwd(), f"{colors.WHITE}Config{colors.ENDC}"))
print(f"{colors.WARNING}---------------------------------------{colors.ENDC}")
print(f"{colors.WHITE}Starting DuoXPy{colors.ENDC}")
print(f"{colors.WHITE}Collecting information...{colors.ENDC}")

def create_config(cfg: ConfigParser) -> None:
    cfg.add_section('User')
    cfg.set('User', 'TOKEN', "")
    if os.getenv('GITHUB_ACTIONS') == 'true':
        token = os.getenv('JWT_TOKEN')
        cfg.set('User', 'TOKEN', f"{token}")
        lessons = os.getenv('LESSONS')
        cfg.set('User', 'LESSONS', f"{lessons}")
    else:
        token = getpass(f"{colors.WHITE}Token: {colors.ENDC}")
        cfg.set('User', 'TOKEN', f"{token}")
        lessons = getpass(f"{colors.WHITE}Lesson: {colors.ENDC}")
        cfg.set('User', 'LESSONS', f"{lessons}")
    with open(config_path, 'w', encoding='utf-8') as configfile:
        configfile.truncate(0)
        configfile.seek(0)
        cfg.write(configfile)

def check_config_integrity(cfg: ConfigParser) -> None:
    if not os.path.exists(config_folder):
        print(f"{colors.WARNING}Creating new config folder at:", os.path.join(os.getcwd()))
        os.mkdir(config_folder)
    
    if not os.path.isfile(config_path) or os.stat(config_path).st_size == 0:
        create_config(cfg)
        return
    
    cfg.read(config_path)
    
    if not cfg.has_section('User') or not cfg.has_option('User', 'TOKEN') or not cfg.has_option('User', 'LESSONS'):
        create_config(cfg)

check_config_integrity(config)
config.read(config_path)


def get_login(cfg: ConfigParser) -> dict[str, str]:
    user: dict[str, str] = {}
    try:
        token = cfg.get('User', 'TOKEN')
        user: dict[str, str] = {'TOKEN': token}
    except:
        create_config(cfg)
    return user
    
def decode_base64(data):
    missing_padding = len(data) % 4
    if missing_padding:
        data += '='* (4 - missing_padding)
    return base64.b64decode(data).decode('utf-8')

token = get_login(config)['TOKEN']
lessons = config.get('User', 'LESSONS')

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token,
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

jwt_payload = token.split('.')[1]
decoded_payload = decode_base64(jwt_payload)
jwt_data = json.loads(decoded_payload)
sub = jwt_data['sub']

response = requests.get(f'https://www.duolingo.com/2017-06-30/users/{sub}?fields=fromLanguage,learningLanguage,xpGains', headers=headers)
data = response.json()
fromLanguage = data['fromLanguage']
learningLanguage = data['learningLanguage']
xpGains = data['xpGains']

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
        'skillId': next((xpGain['skillId'] for xpGain in xpGains if 'skillId' in xpGain), None),
        'smartTipsVersion': 2,
        'type': 'SPEAKING_PRACTICE'
    }

    session_response = requests.post('https://www.duolingo.com/2017-06-30/sessions', data=json.dumps(session_data), headers=headers)
    if session_response.status_code != 200:
        print(f"{colors.FAIL}Error: {session_response.status_code}, {session_response.text}{colors.ENDC}")
        continue

    session = session_response.json()

    update_data = {
        **session,
        'heartsLeft': 0,
        'startTime': (time.time() - 60),
        'enableBonusPoints': False,
        'endTime': time.time(),
        'failed': False,
        'maxInLessonStreak': 9,
        'shouldLearnThings': True,
    }

    response = requests.put(f'https://www.duolingo.com/2017-06-30/sessions/{session["id"]}', data=json.dumps(update_data), headers=headers)
    if response.status_code != 200:
        print(f"{colors.FAIL}Error: {response.status_code}, {response.text}{colors.ENDC}")
        continue

    response_data = response.json()
    print(f"{colors.OKGREEN}Gained: {response_data['xpGain']} XP (✓){colors.ENDC}")
