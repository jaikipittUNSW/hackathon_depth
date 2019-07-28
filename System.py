import User
import Post
import Comment


class System():

    def __init__(self):
        self.posts = []
        self.users = []
        self.categories = {"Books": [], "Films": [], "News": [], "Sports": [],
        "Arts": [], "History": []}
        self.postID = 0
        self.addNewUser("test", "test")

    def makeNewPost(self, title, post, user):
        post = Post.Post(self.postID, title, post, user)
        self.postID +=1
        return post

    def addNewUser(self, name, password):
        self.users.append(User.User(name, password))

    def addNewPost(self, title,  post, user, categories):
        nPost = self.makeNewPost(title, post, user)
        self.posts.append(nPost)
        for category in categories:
            if category in self.categories:
                self.categories[category].append(nPost)
        return self.postID - 1

    def commentOnPost(self, postID, comment, user):
        self.commentOnComment(postID, 0, comment, user)

    def commentOnComment(self, postID, commentID, comment, user):
        for post in self.posts:
            if (post.isPost(postID)):
                post.addComments(commentID, comment, user)
                break

    def getComments(self, postID):
        post = self.getPost(postID)
        if post != None:
            return post.getComments()
        return None

    def getPost(self, id):
        id = int(id)
        post = None
        if (id < self.postID):
            for posts in self.posts:
                if posts.isPost(id):
                    post = posts
                    break
        return post

    def showCategoryPosts(self, categories):
        return self.categories[categories] if categories in self.categories else None

    def getAllPosts(self):
        posts = []
        for post in self.posts:
            posts.append(post.getPostVal())
        return posts

    def login(self, name, password):
        user = None
        for users in self.users:
            if (users.login(name, password)):
                user = users
                break
        return user