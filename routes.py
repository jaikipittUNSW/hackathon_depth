from server import app, system
from flask import render_template, request, redirect, url_for, abort

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
    conversations = ["yeet", "ya"]
    categories = ["Sports", "Arts", "History", "Yoghurts"]
    return render_template("conversationDetail.html", category=category, conversations=conversations)

@app.route('/conversations/<category>/<conversation>', methods=["GET", "POST"])
def CommentDetail(category, conversation):
    comments = ["yeet", "ya"]
    return render_template("commentDetail.html", comments=comments)