#!/usr/bin/python2
import requests,json
mm = {}
mm['host'] = 'http://localhost:8065/api/v4/'
mm['users'] = mm['host']+'users'
mm['teams'] = mm['host']+'teams'
def js_r():
    with open("/home/mint/.api/mattermost.json",'r') as file:
        return(json.load(file))
mm['key'] = js_r()['Access Token']
print mm['key']
mm['headers'] = "Authorization: Bearer "+mm['key']

user = {
  "email": "",
  "username": "",
  "password": "password",
  "notify_props": {
    "email": "false",
    "push": "false",
    "desktop": "false",
    "desktop_sound": "false",
    "mention_keys": "false",
    "channel": "false",
    "first_name": "false"
  }
}

def push_user(uname):
    user['email'] = uname+'@subdomain.domain'
    user['username'] = uname
    new_user = requests.post(
            mm['host'],
            headers=mm['headers'],
            json=user)
    return new_user
    
def push_user_2_team(uname):
    return requests.get(mm['teams'],
            headers=mm['headers'])
    
for u_thing in sys.argv():
    print push_user(u_thing)
    print push_user_2_team(u_thing)
    
