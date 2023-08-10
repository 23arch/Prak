import pandas as pd
import requests

def get_location_from_coordinates(lat, lng, access_token):
    lat = str(lat).replace(",", ".")
    lng = str(lng).replace(",", ".")
    
    url = f"https://api.geoapify.com/v1/geocode/reverse?lat={lat}&lon={lng}&apiKey={access_token}"
    response = requests.get(url)
    json_data = response.json()
    
    if "features" in json_data and json_data["features"]:
        feature = json_data["features"][0]
        properties = feature.get("properties", {})
        
        address = properties.get("formatted")
        village = properties.get("city")
        municipality = properties.get("county")
        district = properties.get("state")
        state_district = properties.get("state_district")
        state = properties.get("region")
        country = properties.get("country")
        road = properties.get("street")
        house_number = properties.get("housenumber")
        mountain_rescue = properties.get("mountain_rescue")
        isolated_dwelling = properties.get("isolated_dwelling")
        
        return address, village, municipality, district, state_district, state, country, road, house_number, mountain_rescue, isolated_dwelling
    else:
        raise Exception("Adresse nicht gefunden")

# Lade das Excel-Blatt und lese die Koordinaten aus den Spalten "lat" und "lng"
excel_file = "Test.xlsx"
df = pd.read_excel(excel_file)

# Listen zum Speichern der Adressen und anderen Informationen
addresses = []
villages = []
municipalities = []
districts = []
state_districts = []
states = []
countries = []
roads = []
house_numbers = []
mountain_rescues = []
isolated_dwellings = []
eids = []  # Neue Liste für die eindeutige ID (eid)

# API-Schlüssel für Geoapify
API_KEY = "9b26613546d04570ace24317af2f1b2d"

# Loop über die Koordinaten und API-Aufrufe
for row in df.itertuples():
    eid = row.eid  # Eindeutige ID aus der Spalte "eid" lesen
    lat = row.lat
    lng = row.lng
    
    # Zeige Fortschrittsnachricht an
    print(f"Verarbeite Zeile {row.Index}/{len(df)} - Lat: {lat}, Lng: {lng}")
    
    try:
        address, village, municipality, district, state_district, state, country, road, house_number, mountain_rescue, isolated_dwelling = get_location_from_coordinates(lat, lng, API_KEY)
        addresses.append(address)
        villages.append(village)
        municipalities.append(municipality)
        districts.append(district)
        state_districts.append(state_district)
        states.append(state)
        countries.append(country)
        roads.append(road)
        house_numbers.append(house_number)
        mountain_rescues.append(mountain_rescue)
        isolated_dwellings.append(isolated_dwelling)
        eids.append(eid)  # Füge die eindeutige ID der Liste hinzu
    except Exception as e:
        print(f"Fehler beim Verarbeiten von Zeile {row.Index}: {e}")
        addresses.append("Fehler: " + str(e))
        villages.append("")
        municipalities.append("")
        districts.append("")
        state_districts.append("")
        states.append("")
        countries.append("")
        roads.append("")
        house_numbers.append("")
        mountain_rescues.append("")
        isolated_dwellings.append("")
        eids.append(eid)  # Wenn ein Fehler auftritt, füge trotzdem die eindeutige ID der Liste hinzu

# Füge die Informationen in das DataFrame ein
df["Adresse"] = addresses
df["Dorf"] = villages
df["City"] = municipalities
df["County"] = districts
df["StateDistrict"] = state_districts
df["State"] = states
df["Country"] = countries
df["Road"] = roads
df["House Number"] = house_numbers
df["Mountain Rescue"] = mountain_rescues
df["Isolated Dwelling"] = isolated_dwellings
df["eid"] = eids  # Füge die eindeutige ID als neue Spalte hinzu

# Speichern des DataFrames in einer separaten Excel-Datei
output_excel_file = "Ortschaften.xlsx"
df.to_excel(output_excel_file, index=False)
print(f"Adressen, Dorf, Gemeinde, Bezirk, Bund, Staat, Land, Road, House Number, Mountain Rescue, Isolated Dwelling und eid erfolgreich in '{output_excel_file}' gespeichert.")
