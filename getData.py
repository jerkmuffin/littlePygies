import requests
import secrets
import json
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


client = WebClient(token=secrets.BEARER)
usersList = client.users_list()
# print(json.dumps(usersList.data, indent=2))


def isActive(userID):
    active = client.users_getPresence(user=userID)
    # print(json.dumps(active.data, indent=2))
    return active.data['presence']


for i in usersList['members']:
    print(i['name'])
    print(i['id'])
    active = isActive(i['id'])
    print("active: {}".format(active))
    info = client.users_info(user=i['id'])
    print("status text: {}".format(info.data['user']['profile']['status_text']))
    print("status emoji: {}".format(info.data['user']['profile']['status_text']))
    print("img url: {}\n".format(info.data['user']['profile']['image_512']))

# mikeInfo = client.users_info(user='U9QQAS7FS')
# print(json.dumps(mikeInfo.data))
