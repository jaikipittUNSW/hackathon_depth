from routes import app

if __name__ == '__main__':
    # SIGINT to stop (Ctrl + C)
    app.run(debug=True, host="0.0.0.0", port=5002)
