import json

def reiter_erfassen(grad, name, vorname, jahrgang, adresse, plz, ort, tel, liz_brev, namepf, passnummer, geschlecht, farbe, alter, rasse, gwp, pruefung1, pruefung2, pruefung3, pruefung4, pruefung5, pruefung6, pruefung7, pruefung8, pruefung9, pruefung10, pruefung11, pruefung12):
    
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
        "liz_brev": liz_brev,
        "namepf": namepf,
        "passnummer": passnummer,
        "geschlecht": geschlecht, 
        "farbe": farbe, 
        "alter": alter, 
        "rasse": rasse, 
        "gwp": gwp, 
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
        "pruefung12": pruefung12,
    }
        
    alle_anmeldungen[passnummer] = einreiter
        
    json_daten["reiter"] = alle_anmeldungen

    save_to_json(json_daten)
    return json_daten                       

def load_json():
    json_daten = {}
    try:
        with open('data/data.json') as open_file:   
            json_daten = json.load(open_file)
    
    except FileNotFoundError:                       
        print("File not found")

    return json_daten

def save_to_json(daten):
    with open('data/data.json', "w") as open_file:
        json.dump(daten, open_file)