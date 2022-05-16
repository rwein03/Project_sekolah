import os
from pprint import pprint
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions
import json
import urllib
from subprocess import CREATE_NO_WINDOW
from selenium.webdriver.chrome.service import Service

FOLDER = os.path.dirname(os.path.realpath(__file__))
JSON_FILE = os.path.join(FOLDER, 'settings.json')
MAIN_SITE = 'http://login.charis.net'
LOGIN_SITE = 'http://login.charis.net/login?'


def chrome_setting(site, path):
    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument(f"--app={MAIN_SITE}")
    chrome_options.add_argument("disable-infobars")
    # service = Service()
    # service.creationflags = CREATE_NO_WINDOW
    driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
    driver.set_window_size(480, 320)
    driver.get(site)
    return driver

def login(user, password, path):
    login_site = chrome_setting(f'{LOGIN_SITE}username={user}&password={password}', path)

def logout(path):
    logout_site = chrome_setting(f'{MAIN_SITE}/logout', path)

def save_json(path):
    data_json = {
        'path' : path
    }
    with open(JSON_FILE, 'w') as fp :
        json.dump(data_json, fp)

def load_json():
    f = open(JSON_FILE)
    data = json.load(f)
    path_file = data['path']
    return path_file

def internet_check():
    try:
        urllib.request.urlopen('https://www.google.com/')
    except:
        return False
    else: 
        return True
   
def run_service():
    try:
        if os.path.exists(JSON_FILE):
            path_file = load_json()
            if os.path.exists(path_file):
                if internet_check():
                    print('[+] Connected')
                    launch = login('charislab', 'sfth2122', path_file)
                    save_driver = ChromeDriverManager(path=FOLDER).install()
                    save_json(save_driver)
                else:
                    print('[!] No Internet')
                    launch = login('charislab', 'sfth2122', path_file)
                launch.quit()
        else:
            if internet_check():
                print('[+] Connected')     
                b = ChromeDriverManager(path=FOLDER).install()
                save_json(b)
            else:
                print('[!] No Internet')
                launch = login('charislab', 'sfth2122', b)
            launch.quit()
    except:
        pass

# if __name__ == '__main__':
#     run()