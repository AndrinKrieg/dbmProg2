"""Attributes: app (flask.app.Flask): Der Name meiner entwickelten Applikation"""

from flask import Flask, render_template, redirect, request, url_for
from libs import erfassen_reiter

app = Flask("anmeldeplattform SPSTA")


@app.route("/", methods=['GET', 'POST'])
def reitererfassen():
    """
    Summary:
        Daten werden hier eingegeben (diese Daten müssen Vorhanden sein um beim Event starten zu können)

    Returns:
        template: HTML 'anmeldelsite' wird gerendert, wo das Formular ausgefüllt werden kann.
        redirect: Nach dem Ausfüllen kann der User auf 'Absenden' clicken und wird auf eine
        Bestätigungsseite weitergeleitet.
    """
    if request.method == 'POST': 
        returned_data = erfassen_reiter.reiter_erfassen(request.form)
        return redirect(url_for('danke'))
    return render_template("reitererfassen.html")

@app.route("/anmeldeliste")
def anmeldeliste():
    """
    Summary:
        Hier werden alle Anmeldungen angezeigt. Ideal für den Organisator, welche diese alle kopieren kann.
    
    Returns:
        template: Das HTML 'anmeldeliste.html' wird erstellt.
    """
    reiter_daten = erfassen_reiter.load_json()
    return render_template("anmeldeliste.html", daten=reiter_daten)

@app.route("/danke")
def danke():
    """
    Summary:
        Hier werden die User nach dem ausfüllen hingeschickt. Sie können von da aus nochmals eine Anmledung
        tätigen (manchmal reiter ein Reiter mehrere Pferde an einem Turnier) oder auf die Hauptseite zurück
        gelangen und Informationen zu finden.

    Returns:
        template: Das HTML 'danke.html' wird erstellt. 
    """
    return render_template("danke.html")
    
if __name__== "__main__":
    app.run(debug=True, port=5000)