from listener import webhook
import requests
import json
import time
import socket

#webhook_url = 'https://webhook.site/82d007f9-75b2-4dd6-8e2d-c63db20d85ad'
apiSecret = 'cat'
webhook_url = 'http://api.constellate.de:3000/webhook'
ip = socket.gethostbyname(socket.gethostname()) 

def create():
    data = {
        'data': 'right',
        'apiSecret': apiSecret,
        'timestamp': time.asctime( time.localtime(time.time()) ),
        'ip': ip
        }

    time.sleep(2)
    r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

create()
