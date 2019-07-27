import Comment

class post():

    def __init__(self, id):
        self.id = id
        self.commentID = 1
        self.categories = []
        self.posts = ""
        self.comments = []
        self.changeList = []
        self.usefulList = []

    def __init__(self, id, title, post, user):
        self.__init__(id)
        self.title = title
        self.post = post
        self.user = user

    def addCategories(self, categories):
        pass

    def addPost(self, post):
        self.post = post

    def addUser(self, user):
        self.user = user

    def addComments(self, id, comment, user):
        flag = false
        if (id < self.commentID):
            for child in self.comments:
                flag = child.addChildComments(id, comment)
                if (flag):
                    break;
        return flag

    def getText(self):
        return self.post

    def getUser(self):
        return self.user

    def addChange(self, user):
        self.changeList.append(user)

    def addUseful(self, user):
        self.usefulList.append(user)

    def getPostVal(self):
        return {"id": self.id, "ChangeMyMind": len(self.changeList), "FoundThisUseful": len(self.useful)}

    def isPost(self, id):
        return self.id == id
