""" erfassen_reiter.py ist meine Libary für das lesen sowie auch schreiben der jsonfile"""

import json

def reiter_erfassen(form_data):
    """
    diese def lädt die daten der Anmeldungen aus der json file.
    Arugmente:  File befindet sich in dbmProg2/data/data.json
    Returns:    Dicitionary mit Daten aus reitererfassen.html wird zurückgegeben.
    """
    json_daten = load_json()
    alle_anmeldungen = json_daten.get("reiter", {})

    einreiter = {
        "grad": form_data['grad'],
        "name": form_data['name'],
        "vorname": form_data['vorname'],
        "jahrgang": form_data['jahrgang'],
        "adresse": form_data['adresse'],
        "plz": form_data['plz'],
        "ort": form_data['ort'],
        "tel": form_data['tel'],
        "liz_brev": form_data['liz_brev'],
        "namepf": form_data['namepf'],
        "passnummer": form_data['passnummer'],
        "geschlecht": form_data['geschlecht'],
        "farbe": form_data['farbe'],
        "alter": form_data['alter'],
        "rasse": form_data['rasse'],
        "gwp": form_data['gwp'],
        "pruefungen": form_data.getlist("pruefungen")
    }


    alle_anmeldungen[form_data['passnummer']] = einreiter
    json_daten["reiter"] = alle_anmeldungen

    save_to_json(json_daten)
    return json_daten

#Jsonfile mit Daten wird geladen
def load_json():
    json_daten = {}
    try:
        with open('data/data.json') as open_file:
            json_daten = json.load(open_file)

    except FileNotFoundError:
        print("File not found")

    return json_daten
#Dictionary mit allen Daten aus Json wird geladen

def save_to_json(daten):
    with open('data/data.json', "w") as open_file:
        json.dump(daten, open_file)
#Alle Daten werden ins Jsonfile geschrieben