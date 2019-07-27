
class User():

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def changePassword(self, old, new):
        if self.login(old):
            self.password = new

    def login(self, name, password):
        return self.password == password and self.name == name

    def setname(self, name):
        self.name = name

    def getName(self):
        return self.name