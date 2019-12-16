from flask import Flask, render_template, redirect, request, url_for
from libs import erfassen_reiter

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
        namepf = request.form['namepf']
        passnummer = request.form['passnummer']
        geschlecht = request.form['geschlecht']
        farbe = request.form['farbe']
        alter = request.form['alter']
        rasse = request.form['rasse']
        gwp = request.form['gwp']
        pruefung1 = "ja" if len(request.form.getlist("pruefung1")) > 0 else "nein"
        pruefung2 = "ja" if len(request.form.getlist("pruefung2")) > 0 else "nein"
        pruefung3 = "ja" if len(request.form.getlist("pruefung3")) > 0 else "nein"
        pruefung4 = "ja" if len(request.form.getlist("pruefung4")) > 0 else "nein"
        pruefung5 = "ja" if len(request.form.getlist("pruefung5")) > 0 else "nein"
        pruefung6 = "ja" if len(request.form.getlist("pruefung6")) > 0 else "nein"
        pruefung7 = "ja" if len(request.form.getlist("pruefung7")) > 0 else "nein"
        pruefung8 = "ja" if len(request.form.getlist("pruefung8")) > 0 else "nein"
        pruefung9 = "ja" if len(request.form.getlist("pruefung9")) > 0 else "nein"
        pruefung10 = "ja" if len(request.form.getlist("pruefung10")) > 0 else "nein"
        pruefung11 = "ja" if len(request.form.getlist("pruefung11")) > 0 else "nein"
        pruefung12 = "ja" if len(request.form.getlist("pruefung12")) > 0 else "nein"
        namepf2 = request.form['namepf2']
        passnummer2 = request.form['passnummer2']
        geschlecht2 = request.form['geschlecht2']
        farbe2 = request.form['farbe2']
        alter2 = request.form['alter2']
        rasse2 = request.form['rasse2']
        gwp2 = request.form['gwp2']
        pruefung1pf2 = "ja" if len(request.form.getlist("pruefung1pf2")) > 0 else "nein"
        pruefung2pf2 = "ja" if len(request.form.getlist("pruefung2pf2")) > 0 else "nein"
        pruefung3pf2 = "ja" if len(request.form.getlist("pruefung3pf2")) > 0 else "nein"
        pruefung4pf2 = "ja" if len(request.form.getlist("pruefung4pf2")) > 0 else "nein"
        pruefung5pf2 = "ja" if len(request.form.getlist("pruefung5pf2")) > 0 else "nein"
        pruefung6pf2 = "ja" if len(request.form.getlist("pruefung6pf2")) > 0 else "nein"
        pruefung7pf2 = "ja" if len(request.form.getlist("pruefung7pf2")) > 0 else "nein"
        pruefung8pf2 = "ja" if len(request.form.getlist("pruefung8pf2")) > 0 else "nein"
        pruefung9pf2 = "ja" if len(request.form.getlist("pruefung9pf2")) > 0 else "nein"
        pruefung10pf2 = "ja" if len(request.form.getlist("pruefung10pf2")) > 0 else "nein"
        pruefung11pf2 = "ja" if len(request.form.getlist("pruefung11pf2")) > 0 else "nein"
        pruefung12pf2 = "ja" if len(request.form.getlist("pruefung12pf2")) > 0 else "nein"

        returned_data = erfassen_reiter.reiter_erfassen(grad, name, vorname, jahrgang, adresse, plz, ort, tel, liz_brev, namepf, passnummer, geschlecht, farbe, alter, rasse, gwp, namepf2, passnummer2, geschlecht2, farbe2, alter2, rasse2, gwp2)
    return render_template("reitererfassen.html")

@app.route("/anmeldeliste")
def anmeldeliste():
    reiter_daten = erfassen_reiter.load_json()
    return render_template("anmeldeliste.html", daten=reiter_daten)
    
if __name__== "__main__":
    app.run(debug=True, port=5000)