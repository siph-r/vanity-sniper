from httpx import patch, get
from threading import Thread
from time import sleep
from json import loads

config = loads(open("config.json", "r").read())
token = config['token'] # User account token
proxy = config['proxy'] # Rotating proxy
server = config['server'] # Server ID to add vanity too
def check_invite(vanity):
    url = "https://discord.com/api/v9/invites/" + vanity
    src = get(url, proxies={
        "all://": "http://" + config['proxy']
    })
    if src.status_code == 404:
        print("Vanity found!")
        headers = {'authorization': token}
        url = f'https://discord.com/api/v9/guilds/{server}/vanity-url'
        src = patch(url, headers=headers, json={'code': vanity})
        print(src.text)
        exit()
    else:
        print("Vanity not found!")
        sleep(0.2)
while True:
    Thread(target=check_invite, args=["celeb"]).start() 
    #time.sleep(0.1)# Change vanity to your vanity      