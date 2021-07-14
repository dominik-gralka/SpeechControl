from os import error
import requests, json
import time
from listener import webhook
import requests
import socket

from pynput import keyboard
from pynput.keyboard import Key, Controller

keyboard = Controller()


apiSecret = 'cat'
webhook_url = 'http://api.constellate.de:3000/webhook'
ip = socket.gethostbyname(socket.gethostname())

def request():
    try:
        url = requests.get('http://api.constellate.de/sessions/'+ apiSecret + '.json')
        text = url.text

        obj = json.loads(text)
        data = obj['data']

        print('Recieved data: ' + data)

        if (data == 'right'):
            commandRight()
            terminate()
    
    except:
        print('Pending...')

def terminate():
    data = {
        'data': 'terminate',
        'apiSecret': apiSecret,
        'timestamp': time.asctime( time.localtime(time.time()) ),
        'ip': ip
        }

    r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

def commandRight():
    print('Trigger: right')
    keyboard.press(Key.right)
    keyboard.release(Key.right)

def commandLeft():
    print('Trigger: left')
    keyboard.press(Key.left)
    keyboard.release(Key.left)

#while True:
#    request()
#    time.sleep(1)