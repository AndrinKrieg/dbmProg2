from flask import Flask, render_template, redirect, request, url_for
from libs import erfassen_reiter

app = Flask(__name__)

@app.route("/")
def startseite():
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)