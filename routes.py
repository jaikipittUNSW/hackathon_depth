from server import app, System
from flask import render_template, request, redirect, url_for, abort
from Comment import Comment
from User import User

@app.route('/', methods=["GET", "POST"])
def home():
    categories = ["Sports", "Arts", "History", "Yoghurts"]
    bestOfCategories = ["Films", "Books", "News"]
    return render_template('home.html', categories=categories, bestOfCategories=bestOfCategories)


@app.route('/best/<subject>', methods=["GET", "POST"])
def BestOfDetail(subject):
    bestOfs = ["yeet", "ya", "yip"]

    return render_template("bestOfDetail.html", category=subject, bestOfs=bestOfs)

@app.route('/conversations/<category>', methods=["GET", "POST"])
def ConversationDetail(category):
    # conversations=showCategoryPosts(category)
    conversations=["1","2","3"]
    return render_template("conversationDetail.html", category=category, conversations=conversations)

@app.route('/conversations/<category>/<conversation>', methods=["GET", "POST"])
def CommentDetail(category, conversation):
#    comments = System.getComments(conversation)
    comments = list()
    u = User("Jaiki", "password")
    comments.append(Comment(0, u, "yeet"))
    temp = Comment(1, u, "ya")
    print(temp.addChildComment(1,Comment(2,u,"Hello World")))
    temp.addChildComment(1,Comment(3,u,"Yep"))
    comments.append(temp)
    print(temp.getChildrenComments())
    return render_template("commentDetail.html", comments=comments)