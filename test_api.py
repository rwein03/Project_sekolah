import atexit
from time import sleep, time
import requests
import socket
from getmac import get_mac_address
import subprocess
import login_services
from threading import Thread
import time
import json
import os

isChecking = False

FOLDER = os.path.dirname(os.path.realpath(__file__))
JSON_SETTINGS = os.path.join(FOLDER, 'api_settings.json')


URL = 'http://localhost:8000/api/class'
URL_COMPUTER_PUT = 'http://localhost:8000/api/class/'
URL_COMPUTER_FILTER = 'http://localhost:8000/api/userfilter'
URL_ACTION = 'http://localhost:8000/api/actionfilter'
URL_ACTION_PUT = 'http://localhost:8000/api/action/'

HEADERS = {
    'Authorization' : 'Token 348e69ca8482769f2f63b57f009ac6b37825b76d'
}

ACTION_DATA = {
    'ip_addr': 'IP',
    'action': 'ACTION',
    'isStatus': False,
    'macaddr': 'MAC'
}

BODY = {
        'mac_addr' : 'MAC',
        'ip_addr':'IP',
        'isAlive':False,
        'isBlocked' : False,
        'note' : ''
    }

IP = ''
MAC = ''

def get_ip_mac():
    host = socket.gethostname()
    ip = socket.gethostbyname_ex(host)
    load_ip = load_json()
    local_ip = []
    for check in ip[2]:
        for load in load_ip['ip_range']:
            if check.startswith(load):
                local_ip.append(check)
    ip_mac = get_mac_address(ip=local_ip[0])
    return local_ip[0], ip_mac

def get_filter(mac):
    filter = requests.get(URL_COMPUTER_FILTER,params={'mac_addr': mac}, headers=HEADERS)
    return filter.json()

def post(DATAS):
    post = requests.post(URL, data=DATAS, headers=HEADERS)
    return post

def put(DATAS,mac):
    put = requests.put(URL_COMPUTER_PUT+mac, data=DATAS, headers=HEADERS)
    return put

def put_action(pk, DATAS):
    full = URL_ACTION_PUT + f'{pk}'
    print(full)
    put_action = requests.put(full, data=DATAS, headers=HEADERS)
    return put_action

def get_action(macaddr, status):
    action = requests.get(URL_ACTION, params={'macaddr':macaddr, 'isStatus': status}, headers=HEADERS)
    return action.json()

def check_save(IP, MAC):
    check = get_filter(MAC)
    if len(check) == 0:
        BODY['mac_addr'] = MAC
        BODY['ip_addr'] = IP
        BODY['isAlive'] = True
        BODY['isBlocked'] = False
        BODY['note'] = ''
        post_data = post(BODY)
        print(post_data)
    else:
        check_ip = check[0]['ip_addr']
        if IP != check_ip:
            print('Ganti IP')
            BODY['mac_addr'] = MAC
            BODY['ip_addr'] = IP
            BODY['isAlive'] = True
            BODY['isBlocked'] = False
            BODY['note'] = ''
            new_ip = put(BODY, MAC)
            print(new_ip)
        else:
            BODY['mac_addr'] = MAC
            BODY['ip_addr'] = IP
            BODY['isAlive'] = True
            BODY['isBlocked'] = False
            BODY['note'] = ''
            change_status = put(BODY, MAC)
            print('{} status has changed'.format(IP))

@atexit.register
def run_exit():
    BODY['mac_addr'] = MAC
    BODY['ip_addr'] = IP
    BODY['isAlive'] = False
    BODY['isBlocked'] = False
    BODY['note'] = ''
    new_ip = put(BODY, MAC)

def main():
    try:
        IP, MAC = get_ip_mac()
        check_save(IP, MAC)
        data = load_json()
        while True:
        # print(check_save(IP, MAC))
            checkin = get_action(MAC, False)
            if len(checkin) != 0:
                if checkin[0]['macaddr'] == MAC:
                    print('proccess. . . . .')
                    if checkin[0]['action'] == 'restart':
                        ACTION_DATA['ip_addr'] = IP
                        ACTION_DATA['macaddr'] = MAC
                        ACTION_DATA['action'] = checkin[0]['action']
                        ACTION_DATA['isStatus'] = True
                        proceed = put_action(checkin[0]['id'], ACTION_DATA)
                        subprocess.Popen('shutdown -r -f -t 00')
        
                    if checkin[0]['action'] == 'shutdown':
                        ACTION_DATA['ip_addr'] = IP
                        ACTION_DATA['macaddr'] = MAC
                        ACTION_DATA['action'] = checkin[0]['action']
                        ACTION_DATA['isStatus'] = True
                        proceed = put_action(checkin[0]['id'], ACTION_DATA)
                        subprocess.Popen('shutdown -s -f -t 00')
                        
                    if checkin[0]['action'] == 'wifi':
                        ACTION_DATA['ip_addr'] = IP
                        ACTION_DATA['macaddr'] = MAC
                        ACTION_DATA['action'] = checkin[0]['action']
                        ACTION_DATA['isStatus'] = True
                        proceed = put_action(checkin[0]['id'], ACTION_DATA)
                        login_services.run_service()
                else:
                    print('mac tidak sama')
            else:
                print('no action')
                
            time.sleep(data['delay'])
    except:
        print('Host is Died')
        

def save_json():
    data_json = {
        'host_ip' : '192.168.1.3',
        'delay' : 2,
        'ip_range' :['192.168.1.', '192.168.0.'] 
    }
    with open(JSON_SETTINGS, 'w') as fp :
        json.dump(data_json, fp)

def load_json():
    f = open(JSON_SETTINGS)
    data = json.load(f)
    return data

if __name__=='__main__':
    save_json()
    data = load_json()
    URL = f'http://{data["host_ip"]}:8000/api/class'
    URL_COMPUTER_PUT = f'http://{data["host_ip"]}:8000/api/class/'
    URL_COMPUTER_FILTER = f'http://{data["host_ip"]}:8000/api/userfilter'
    URL_ACTION = f'http://{data["host_ip"]}:8000/api/actionfilter'
    URL_ACTION_PUT = f'http://{data["host_ip"]}:8000/api/action/'
    th1 = Thread(target=main)
    th1.start()
    th1.join()
        
    