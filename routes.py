from server import app, system
from flask import render_template, request, redirect, url_for, abort

from Comment import Comment
from User import User
import System

system = System.System()

@app.route('/auth', methods=["GET"])
def landing():
    return "yeet"

@app.route('/', methods=["GET", "POST"])
def home():
    categories = system.getCategories()
    bestOfCategories = system.getBestOfCategories()
    return render_template('home.html', categories=categories, bestOfCategories=bestOfCategories)


@app.route('/best/<subject>', methods=["GET", "POST"])
def BestOfDetail(subject):
    bestOfs = system.showCategoryPosts(subject)
    # system = system.updateSystem()
#    bestOfs= system.showCategoryPosts("_"+subject)

    return render_template("bestOfDetail.html", category=subject, bestOfs=bestOfs)

@app.route('/conversations/<category>', methods=["GET", "POST"])
def ConversationDetail(category):
    # system = system.updateSystem()

    conversations= system.showCategoryPosts(category)
    return render_template("conversationDetail.html", category=category, conversations=conversations)

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
        return redirect("/", code=302)


    return render_template("postForm.html")

@app.route('/conversations/<category>/<conversation>', methods=["GET", "POST"])
def CommentDetail(category, conversation):
    # system = system.updateSystem()

    comments = system.getComments(conversation)
    return render_template("commentDetail.html", comments=comments)
