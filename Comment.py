import Post
import User

class Comment():

    def __init__(self, id, user, comment):
        self.child = []
        self.id = id
        self.user = user
        self.comment = comment
        self.child = []

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
            self.child.append(comment)
        else:
            for comment in self.child:
                flag = comment.addChildComment(id, comment)
                if (flag):
                    break
        return flag

    def getComment(self, id):
        comment = None
        if id == self.id:
            comment = self
        else:
            for comments in self.child:
                comment = comments.getComment(id)
                if comment != None:
                    break
        return comment

    def getChildrenComments(self):
        return self.child

    def getText(self):
        return self.comment

    def getUser(self):
        return self.user

    def getUserName(self):
        return self.user.getName()