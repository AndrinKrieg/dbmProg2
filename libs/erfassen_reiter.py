import json

def reiter_erfassen(grad, name, vorname, jahrgang, adresse, plz, ort, tel, liz_brev, namepf, passnummer, geschlecht, farbe, alter, rasse, gwp, namepf2, passnummer2, geschlecht2, farbe2, alter2, rasse2, gwp2):
    
    json_daten = load_json()
    alle_anmeldungen = json_daten.get("reiter", {})
        
    einreiter = {
        "grad": grad,
        "name": name,
        "vorname": vorname,
        "jahrgang": jahrgang,
        "adresse": adresse,
        "plz": plz,
        "ort": ort,
        "tel": tel,
        "namepf": namepf,
        "passnummer": passnummer,
        "geschlecht": geschlecht, 
        "farbe": farbe, 
        "alter": alter, 
        "rasse": rasse, 
        "gwp": gwp, 
        "namepf2": namepf2,
        "passnummer2": passnummer2,
        "geschlecht2": geschlecht2, 
        "farbe2": farbe2, 
        "alter2": alter2, 
        "rasse2": rasse2, 
        "gwp2": gwp2, 
    }
        
    alle_anmeldungen[grad] = einreiter
        
    json_daten["reiter"] = alle_anmeldungen

    save_to_json(json_daten)
    return json_daten                        #Json-Datei mit neuer Eingabe wird zurückgegeben
    

def load_json():
    json_daten = {}
    try:
        with open('data/data.json') as open_file:    #Json-Datei öffnen/lesen
            json_daten = json.load(open_file)
    
    except FileNotFoundError:                       #wenn json.datei noch leer ist     
        print("File not found")

    return json_daten

def save_to_json(daten):
    with open('data/data.json', "w") as open_file:
        json.dump(daten, open_file)

"""

pruefung1, pruefung2, pruefung3, pruefung4, pruefung5, pruefung6, pruefung7, pruefung8, pruefung9, pruefung10, pruefung11, pruefung12
"""

"""
        "pruefung1": pruefung1, 
        "pruefung2": pruefung2, 
        "pruefung3": pruefung3,
        "pruefung4": pruefung4, 
        "pruefung5": pruefung5, 
        "pruefung6": pruefung6, 
        "pruefung7": pruefung7, 
        "pruefung8": pruefung8, 
        "pruefung9": pruefung9, 
        "pruefung10": pruefung10, 
        "pruefung11": pruefung11, 
        "pruefung12": pruefung12
"""
"""
pruefung1, pruefung2, pruefung3, pruefung4, pruefung5, pruefung6, pruefung7, pruefung8, pruefung9, pruefung10, pruefung11, pruefung12
"""

"""
        "pruefung1": pruefung1, 
        "pruefung2": pruefung2, 
        "pruefung3": pruefung3,
        "pruefung4": pruefung4, 
        "pruefung5": pruefung5, 
        "pruefung6": pruefung6, 
        "pruefung7": pruefung7, 
        "pruefung8": pruefung8, 
        "pruefung9": pruefung9, 
        "pruefung10": pruefung10, 
        "pruefung11": pruefung11, 
        "pruefung12": pruefung12
"""