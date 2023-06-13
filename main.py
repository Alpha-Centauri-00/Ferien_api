from flask import Flask

import json

app = Flask(__name__)


def reading_file(year):
    file_name = f"new_ferien_{year}.json"
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def configure_json(_data):
    formatted_data = json.dumps(_data, ensure_ascii=False,indent=4)
    return '<pre>' + formatted_data + '</pre>'

@app.route("/<year>",methods=['GET'])
def data_(year):
    data = reading_file(year)
    return configure_json(data)

@app.route("/",methods=["GET"])
def home_():
    Infos = {
    "1. info": "All German Holidays for all States",
    "2. to get ferien_2023": "/2023",
    "3. to get ferien_2024": "/2024",
    "4. to get ferien_2025": "/2025",
    "LWE means: ": "Langes Wochenende moeglich",
    "BT means: ": "Brueckentag moeglich",
    
    }
    
    return Infos


if __name__ == "__main__":
    app.run(debug=True)

