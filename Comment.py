import Post
import User

class Comment():
    
    def __init__(self, id):
        self.child = []
        self.id = id

    def __init__(self, id, user, comment):
        self.__init__()
        self.user = user
        self.comment = comment

    def addComment(self, comment):
        self.comment = comment

    def adduser(self, user):
        self.user = user

    def addParentComment(self, comment):
        self.parent = commnet

    def addRootPost(self, post):
        self.root = post

    def addChildComment(self, id, comment):
        flag = (self.id == id)
        if (flag):
            self.child.append(commnet)
        else:
            for comment in self.child:
                flag = comment.addChildComment(id, comment)
                if (flag):
                    break
        return flag

    def getText(self):
        return self.commnet

    def getUser(self):
        return self.user

    def getUserName(self):
        return self.user.getName()