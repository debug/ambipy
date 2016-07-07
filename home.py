import os
import json
import requests
from requests.auth import HTTPDigestAuth
from rooms import Room

REST_URL = "https://rest.ambiclimate.com"
DEBUG = False

def log(msg):
    if DEBUG:
        print(msg)

class Home(object):

    def __init__(self, userObj):
        self.__userObj = userObj
        self.__setup()

    def __setup(self):
        queryStr =  '{0}/UserCredential?email={1}&pwd={2}'.format(REST_URL, self.__userObj.email, self.__userObj.password)
        log(queryStr)
        response = requests.get(queryStr, verify=False)
        if response.json() != {}:
            pass
            self.__userObj.userId = response.json()['user_id']
            self.__userObj.tokenId = response.json()['token_id']
            self.__userObj.createdOn = response.json()['created_on']

            self.__headers = {"Authorization":"Bearer {0}".format(response.json()['token_id'])}
        else:
            # TODO throw error
            pass

    @property
    def rooms(self):
        roomsList = []
        queryStr = "{0}/User?expand=appliance%2Cdevice&user_id={1}".format(REST_URL, self.__userObj.userId)
        log(queryStr)
        response = requests.get(queryStr, headers=self.__headers, verify=False)
        for device in response.json()['devices']:
            roomObj = Room(device)
            roomsList.append(roomObj)
        return roomsList


class User(object):

    AUTH_JSON = "auth.json"

    def __init__(self):
        self.__password = None
        self.__email = None
        self.__tokenId = None
        self.__userId = None
        self.__createdOn = None

        self.__setup()

    def __setup(self):
        authFile = os.path.join(os.path.split(__file__)[0], self.AUTH_JSON)
        if os.path.exists(authFile):
            fh = open(authFile, 'r')
            data = json.loads(fh.read())
            if data != {}:
                log("Loading Auth file")
                self.__email = data['email']
                self.__password = data['password']
            fh.close()

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, emailIn):
        self.__email = emailIn

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, passwordIn):
        self.__password = passwordIn

    @property
    def createdOn(self):
        return self.__createdOn

    @createdOn.setter
    def createdOn(self, createdOnIn):
        self.__createdOn = createdOnIn

    @property
    def userId(self):
        return self.__userId

    @userId.setter
    def userId(self, userIdIn):
        self.__userId = userIdIn

    @property
    def tokenId(self):
        return self.__tokenId

    @tokenId.setter
    def tokenId(self, tokenIdIn):
        self.__tokenId = tokenIdIn
