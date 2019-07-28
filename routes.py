from server import app, System
from flask import render_template, request, redirect, url_for, abort
import System

system = System.System()

@app.route('/', methods=["GET", "POST"])
def home():
    categories = ["Sports", "Arts", "History", "Yoghurts"]
    bestOfCategories = ["Films", "Books", "News"]
    return render_template('home.html', categories=categories, bestOfCategories=bestOfCategories)


@app.route('/best/<subject>', methods=["GET", "POST"])
def BestOfDetail(subject):
    bestOfs = ["yeet", "ya", "yip"]
    bestOfs = system.showCategoryPosts(subject)

    return render_template("bestOfDetail.html", category=subject, bestOfs=bestOfs)

@app.route('/conversations/<category>', methods=["GET", "POST"])
def ConversationDetail(category):
    # conversations=showCategoryPosts(category)
    conversations=["1","2","3"]
    return render_template("conversationDetail.html", category=category, conversations=conversations)

@app.route('/conversations/<category>/<conversationID>', methods=["GET", "POST"])
def CommentDetail(category, conversationID):
    comments = system.getComments(conversationID)
    return render_template("commentDetail.html", comments=comments)

@app.route('/post', methods=['GET', 'POST'])
def postForm():
    title = ""
    if request.method == 'POST':
        title = request.form.get('title')
        post = request.form.get('postContent')
        categories = request.form.getlist("Categories")
        user = system.login("test", "test")
        id = system.addNewPost(title, post, user, categories)
        # Redirect to the actual conversation
        return redirect("/conversations/", code=302)


    return render_template("postForm.html")