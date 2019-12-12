from flask import Flask, render_template, redirect, request, url_for
from libs import erfassen_reiter
from libs import erfassen_pferdeins

app = Flask(__name__)

@app.route("/")
def startseite():
    return render_template('index.html')

@app.route("/reitererfassen", methods=['GET', 'POST'])
def reitererfassen():
    if request.method == 'POST':
        print(request.form)
        grad = request.form['grad']
        name = request.form['name']
        vorname = request.form['vorname']
        jahrgang = request.form['jahrgang']
        adresse = request.form['adresse']
        plz = request.form['plz']
        ort = request.form['ort']
        tel = request.form['tel']
        liz_brev = request.form['liz_brev']
        returned_data = erfassen_reiter.reiter_erfassen(grad, name, vorname, jahrgang, adresse, plz, ort, tel, liz_brev)
    return render_template("reitererfassen.html")

@app.route("/pferdeinserfassen", methods=['GET', 'POST'])
def pferdeinserfassen():
    if request.method == 'POST':
        print(request.form)
        namepf = request.form['namepf']
        passnummer = request.form['passnummer']
        geschlecht = request.form['geschlecht']
        farbe = request.form['farbe']
        alter = request.form['alter']
        rasse = request.form['rasse']
        gwp = request.form['gwp']
        pruefung1 = request.form['pruefung1']
        pruefung2 = request.form['pruefung2']
        pruefung3 = request.form['pruefung3']
        pruefung4 = request.form['pruefung4']
        pruefung5 = request.form['pruefung5']
        pruefung6 = request.form['pruefung6']
        pruefung7 = request.form['pruefung7']
        pruefung8 = request.form['pruefung8']
        pruefung9 = request.form['pruefung9']
        pruefung10 = request.form['pruefung10']
        pruefung11 = request.form['pruefung11']
        pruefung12 = request.form['pruefung12']
        returned_data = erfassen_pferdeins.pferdeins_erfassen(namepf, passnummer, geschlecht, farbe, alter, rasse, gwp, pruefung1, pruefung2, pruefung3, pruefung4, pruefung5, pruefung6, pruefung7, pruefung8, pruefung9, pruefung10, pruefung11, pruefung12)
    return render_template("pferdeinserfassen.html")


@app.route("/pferdzweiserfassen", methods=['GET', 'POST'])
def pferdzweiserfassen():
    if request.method == 'POST':
        print(request.form)
        namepf2 = request.form['namepf2']
        passnummer2 = request.form['passnummer2']
        geschlecht2 = request.form['geschlecht2']
        farbe2 = request.form['farbe2']
        alter2 = request.form['alter2']
        rasse2 = request.form['rasse2']
        gwp2 = request.form['gwp2']
        pruefung1pf2 = request.form['pruefung1pf2']
        pruefung2pf2 = request.form['pruefung2pf2']
        pruefung3pf2 = request.form['pruefung3pf2']
        pruefung4pf2 = request.form['pruefung4pf2']
        pruefung5pf2 = request.form['pruefung5pf2']
        pruefung6pf2 = request.form['pruefung6pf2']
        pruefung7pf2 = request.form['pruefung7pf2']
        pruefung8pf2 = request.form['pruefung8pf2']
        pruefung9pf2 = request.form['pruefung9pf2']
        pruefung10pf2 = request.form['pruefung10pf2']
        pruefung11pf2 = request.form['pruefung11pf2']
        pruefung12pf2 = request.form['pruefung12pf2']
        returned_data = erfassen_pferdzwei.pferdzwei_erfassen(namepf2, passnummer2, geschlecht2, farbe2, alter2, rasse2, gwp2, pruefung1pf2, pruefung2pf2, pruefung3pf2, pruefung4pf2, pruefung5pf2, pruefung6pf2, pruefung7pf2, pruefung8pf2, pruefung9pf2, pruefung10pf2, pruefung11pf2, pruefung12pf2)
    return render_template("pferdzweierfassen.html")

@app.route("/reitererfassen")
def reiter_anmeldung_def():
    reiter_daten = erfassen_reiter.load_json()
    return render_template("index.html", daten=reiter_daten)
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)