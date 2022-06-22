import random
import string
import json

class Account:
    def __init__(self, name, balance):
        characters = string.ascii_letters + string.digits
        self.name = name
        self.account_id = ""
        for i in range(10):
            self.account_id += str(random.choice(characters))
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount

    def teglene(self,amount):
        self.balance -=  amount

    def print_all(self):
        print("Name: {}, Account: {}, Balance: {}".format(self.name, self.account_id, self.balance))
        
    def to_json (self):
        to_json = json.dumps(self.__dict__,  indent=2)
        print(to_json)
        
    def from_json (self):
        from_json = json.loads(json.dumps(self.__dict__, indent=2))
        print(from_json)
        
acc = Account("Ivona", 150)
print(acc.balance)
acc.deposit(200)
acc.print_all()
acc.teglene (50)
acc.print_all()
acc.to_json()
acc.from_json()
