"""Stores value objects related to the project"""
from pages.utils import random_num, random_str


class User:

    def __init__(self, username='', email='', password='', phone='', town='', delivery_address=''):
        self.username = username
        self.email = email
        self.password = password
        self.phone = phone
        self.town = town
        self.delivery_address = delivery_address

    def fill_data(self):
        """Fill data using provided values or by random generated text"""
        self.username = f"testuser{random_str()}"
        self.email = f"{self.username}@user.com"
        self.password = f"pass{random_num()}"
        self.phone = f"67{random_num()}"
        self.delivery_address = "вул. Перемоги УкраЇни, 1"
        self.town = "'Київ'"

    def __repr__(self):
        return f"User:(username={self.username}, email={self.email}, password={self.password}, phone = {self.phone} ," \
               f"town = {self.town}, delivery address = {self.delivery_address}"
