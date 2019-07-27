import User
import Post
import Comment
import pickle


class System():

    def __init__(self):
        self.posts = []
        self.users = []
        self.categories = {"Books": [], "Films": [], "News": [], "Sports": [],
        "Arts": [], "History": []}
        self.postID = 0

    def makeNewPost(self, title, post, user):
        self = updateYoAss()
        post = Post.Post(self.postID, title, post, user)
        self.postID +=1
        self.save()
        return post

    def addNewUser(self, name, password):
        self = updateYoAss()
        self.users.append(User.User(name, password))
        self.save()

    def addNewPost(self, title,  post, user, categories):
        self = updateYoAss()
        nPost = self.makeNewPost(title, post, user)
        self.posts.append(nPost)
        for category in categories:
            if category in self.categories:
                self.categories[category].append(nPost)
        self.save()
        return self.postID - 1

    def commentOnPost(self, postID, comment, user):
        self = updateYoAss()
        self.commentOnComment(postID, 0, comment, user)
        self.save()

    def commentOnComment(self, postID, commentID, comment, user):
        self = updateYoAss()
        for post in self.posts:
            if (post.isPost(postID)):
                post.addComments(commentID, comment, user)
                self.save()
                break
        self.save()

    def getComments(self, postID):
        self = updateYoAss()
        post = getPost(postID)
        return post.getComments()
        self.save()

    def getPost(self, id):
        self = updateYoAss()
        post = None
        if (id < self.postID):
            for posts in self.posts:
                if posts.isPost(id):
                    post = posts
                    self.save()
                    break
        self.save()
        return post

    def showCategoryPosts(self, categories):
        return self.categories[categories] if categories in self.categories else None

    def getAllPosts(self):
        self = updateYoAss()
        posts = []
        for post in self.posts:
            posts.append(post.getPostVal())
        self.save()
        return posts

    def login(self, name, password):
        self = updateYoAss()
        user = None
        for users in self.users:
            if (users.login(name, password)):
                user = users
                break
        self.save()
        return user

    def save(self):
        f = open("system.pickle", "wb")
        pickle.dump(self, f)
        f.close()

def updateYoAss():
    f = open("system.pickle", "rb")
    try:
        sys = pickle.load(f)
    except EOFError:
        sys = System()
    f.close()
    return sys



