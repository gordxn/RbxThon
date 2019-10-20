from bs4 import BeautifulSoup
import requests
import json

class User:
     #/users/{id}
    @staticmethod
    def UsernameById(id):
        return requests.get(url='http://api.roblox.com/users/' + str(id)).json()["Username"]

    @staticmethod
    def IdByUsername(username):
        return requests.get(url='http://api.roblox.com/users/get-by-username?username=' + str(username)).json()["Id"]
