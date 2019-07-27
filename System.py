import User
import Post
import Comment


class System():

    def __init__(self):
        self.posts = None
        self.users = None
        self.categories = {"Books": []}
        self.postID = 0

    def makeNewPost(self, title, post, user):
        post = Post(self.postID, titel, post, user)
        self.postID++
        return post

    def addNewUser(self, name, password):
        self.users.append(User(name, password))

    def addNewPost(self, title,  post, user, categories):
        nPost = self.makeNewPost(title, post, user)
        for category in categories:
            self.categories[categories].append(nPost)

    def commentOnPost(self, postID, comment, user):
        self.commentOnPost(postID, 0, comment, user)

    def commentOnCommnet(self, postID, commentID comment, user):
        for post in self.posts:
            if (post.isPost(postID)):
                post.addNewCommnets(commentID, comment, user)
                break

    def getPost(self, id):
        post = None
        if (id < self.postID):
            for posts in self.posts:
                if posts.isPost(id):
                    post = posts
                    break
        return post

    def showPost(self, id):
        for post in self.posts:
            if post.isPost(id):
                return post

    def showCategoryPosts(self, categories):
        return self.categories[categories]

    def getAllPosts(self):
        posts = []
        for post in self.post:
            posts.append(post.getPostval())
        return posts