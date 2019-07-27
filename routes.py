from server import app, system

@app.route('/', methods=["GET", "POST"])
def home():
    return "Hello World"