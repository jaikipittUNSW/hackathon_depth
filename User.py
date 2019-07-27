
class User():

    def __init__(self):
        self.name = ""
        self.password = None

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def changePassword(self, old, new):
        if self.login(old):
            self.password = new

    def login(self, password):
        return self.password == password

    def setname(self, name):
        self.name = name

    def getName(self):
        return self.name