import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions
import json

JSON_FILE = 'settings.json'
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
    
def run():
    path_file = load_json()
    try:
        if os.path.exists(JSON_FILE):
            if os.path.exists(path_file):
                launch = login('erwinprasetya', 'melvagera', path_file)
                save_driver = ChromeDriverManager(path=os.getcwd()).install()
                save_json(save_driver)
                launch.quit()
        else:
            b = ChromeDriverManager(path=os.getcwd()).install()
            save_json(b)
            launch = login('erwinprasetya', 'melvagera', b)
            launch.quit()
    except:
        pass

if __name__ == '__main__':
    run()