import Comment

class Post():
    def __init__(self, id, title, post, user):
        self.id = id
        self.commentID = 1
        self.categories = []
        self.posts = ""
        self.comments = []
        self.changeList = []
        self.usefulList = []
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
        flag = False
        if (id < self.commentID):
            newComment = Comment.Comment(self.commentID, user, comment)
            if (id == 0):
                self.comments.append(newComment)
                self.commentID += 1
            else:
                for child in self.comments:
                    flag = child.addChildComment(id, newComment)
                    if (flag):
                        self.commentID += 1
                        break;
        return flag

    def getComment(self, id):
        comment = None
        if id < self.commentID:
            for comments in self.comments:
                comment = comments.getComment(id)
                if comment != None:
                    break
        return comment

    def getComments(self):
        return self.comments

    def getTitle(self):
        return self.title

    def getText(self):
        return self.post

    def getUser(self):
        return self.user

    def getUserName(self):
        return self.user.getName()

    def addChange(self, user):
        if user not in self.changeList:
            self.changeList.append(user)

    def removeChange(self, user):
        self.changeList.remove(user)

    def changedUser(self, user):
        return user in self.changeList

    def addUseful(self, user):
        if user not in self.usefulList:
            self.usefulList.append(user)

    def removeUseful(self, user):
        self.usefulList.remove(user)

    def usefulUser(self, user):
        return user in self.usefulList

    def getPostVal(self):
        return {"id": self.id, "ChangeMyMind": len(self.changeList), "FoundThisUseful": len(self.usefulList)}

    def isPost(self, id):
        return self.id == id
