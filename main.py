from flask import Flask, render_template, redirect, request, url_for
from libs import erfassen_reiter

app = Flask(__name__)

@app.route("/")
def startseite():
    return render_template('index.html')
0
@app.route("/reitererfassen", methods=['GET', 'POST'])
def reitererfassen():
    if request.method == 'POST': 
        returned_data = erfassen_reiter.reiter_erfassen(request.form)
        return redirect(url_for('danke'))
    return render_template("reitererfassen.html")

@app.route("/anmeldeliste")
def anmeldeliste():
    reiter_daten = erfassen_reiter.load_json()
    return render_template("anmeldeliste.html", daten=reiter_daten)

@app.route("/danke")
def danke():
    return render_template("danke.html")
    
if __name__== "__main__":
    app.run(debug=True, port=5000)