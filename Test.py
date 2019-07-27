import System


if __name__ == '__main__':
    system = System.System()
    system.addNewUser("Nick", "password")
    system.addNewUser("Jakkie", "notPassword")
    print(system.getPost(1))
    user = system.login("Nick", "password")
    print(user)
    print(system.addNewPost("title", "post", user, ["Books"]))
    print(system.getPost(0))
    print(system.showCategoryPosts("Books"))
    system.commentOnPost(0, "Hello", user)
    system.commentOnComment(0, 1, "Test", user)
    post = system.getPost(0)
    print(post.getText())
    print(post.getUserName())
    com1 = post.getComment(1)
    print(com1)
    print(com1.getText())
    print(com1.getUserName())
    com2 = post.getComment(2)
    print(com2)
    print(com2.getText())
    print(com2.getUserName())
    print(system.getAllPosts())