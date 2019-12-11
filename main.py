from flask import Flask, render_template, redirect, request, url_for
from libs import erfassen_reiter

app = Flask(__name__)

@app.route("/")
def startseite():
    return render_template('index.html')

@app.route("/btgstuff", methods=['GET', 'POST'])
def btgstuff():
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
        namepf = request.form['namepf']
        passnummer = request.form['passnummer']
        geschlecht = request.form['geschlecht']
        farbe = request.form['farbe']
        alter = request.form['alter']
        rasse = request.form['rasse']
        gwp = request.form['gwp']
        preufung1 = request.form['preufung1']
        preufung2 = request.form['preufung2']
        preufung3 = request.form['preufung3']
        preufung4 = request.form['preufung4']
        preufung5 = request.form['preufung5']
        preufung6 = request.form['preufung6']
        preufung7 = request.form['preufung7']
        preufung8 = request.form['preufung8']
        preufung9 = request.form['preufung9']
        preufung10 = request.form['preufung10']
        preufung11 = request.form['preufung11']
        preufung12 = request.form['preufung12']
        namepf2 = request.form['namepf2']
        passnummer2 = request.form['passnummer2']
        geschlecht2 = request.form['geschlecht2']
        farbe2 = request.form['farbe2']
        alter2 = request.form['alter2']
        rasse2 = request.form['rasse2']
        gwp2 = request.form['gwp2']
        preufung1pf2 = request.form['preufung1pf2']
        preufung2pf2 = request.form['preufung2pf2']
        preufung3pf2 = request.form['preufung3pf2']
        preufung4pf2 = request.form['preufung4pf2']
        preufung5pf2 = request.form['preufung5pf2']
        preufung6pf2 = request.form['preufung6pf2']
        preufung7pf2 = request.form['preufung7pf2']
        preufung8pf2 = request.form['preufung8pf2']
        preufung9pf2 = request.form['preufung9pf2']
        preufung10pf2 = request.form['preufung10pf2']
        preufung11pf2 = request.form['preufung11pf2']
        preufung12pf2 = request.form['preufung12pf2']
        returned_data = erfassen_reiter.reiter_erfassen(grad, name, vorname, jahrgang, adresse, plz, ort, tel, liz_brev, namepf, passnummer, geschlecht, farbe, alter, rasse, gwp, pruefung1, pruefung2, pruefung3, pruefung4, pruefung5, pruefung6, pruefung7, pruefung8, pruefung9, pruefung10, pruefung11, pruefung12, namepf2, passnummer2, geschlecht2, farbe2, alter2, rasse2, gwp2, pruefung1pf2, pruefung2pf2, pruefung3pf2, pruefung4pf2, pruefung5pf2, pruefung6pf2, pruefung7pf2, pruefung8pf2, pruefung9pf2, pruefung10pf2, pruefung11pf2, pruefung12pf2)
    return render_template("index.html")


@app.route("/btgstuff")
def reiter_anmeldung_def():
    reiter_daten = erfassen_reiter.load_json()
    return render_template("index.html", daten=reiter_daten)
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)