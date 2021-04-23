import requests
import secrets
import json
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class getSlacky():
    def __init__(self):
        self.slackData = {}
        self.client = WebClient(token=secrets.BEARER)
        self.usersList = self.client.users_list()
        self.check_avatar_dir()

    def check_avatar_dir(self):
        if not os.path.exists('./avatars'):
            os.mkdir('./avatars')

    def fetch_avatar(self, url, id):
        image = requests.get(url)
        if image.status_code == 200:
            with open(os.path.join('./avatars', id + '.' + url.split('.')[-1]), 'wb') as f:
                f.write(image.content)

    def isActive(self, userID):
        active = self.client.users_getPresence(user=userID)
        # print(json.dumps(active.data, indent=2))
        return active.data['presence']

    def getUserInfo(self):
        for i in self.usersList['members']:
            print(i['name'])
            print(i['id'])
            active = self.isActive(i['id'])
            print("status_active: {}".format(active))
            i['profile']['isActive'] = active
            info = self.client.users_info(user=i['id'])
            print("status text: {}".format(info.data['user']['profile']['status_text']))
            print("status emoji: {}".format(info.data['user']['profile']['status_text']))
            print("img url: {}\n".format(info.data['user']['profile']['image_512']))
            self.fetch_avatar(info.data['user']['profile']['image_512'], i['id'])
        return self.usersList.data


if __name__ == "__main__":
    g = getSlacky()
    userList = g.getUserInfo()
    print(json.dumps(userList, indent=2))
# mikeInfo = client.users_info(user='U9QQAS7FS')
# print(json.dumps(mikeInfo.data))
