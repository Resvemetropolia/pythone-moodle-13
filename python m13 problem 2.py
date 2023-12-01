from flask import Flask, jsonify
app = Flask(__name__)
airport_database = {
    "EFHK": {"Name": "Helsinki-Vantaa Airport", "Location": "Helsinki"},
    "EDDF": {"Name": "Frankfurt Airport", "Location": "Frankfurt"},
}
@app.route('/airport/<icao>', methods=['GET'])
def get_airport_info(icao):
    airport_info = airport_database.get(icao.upper(), None)
    if airport_info:
        airport_info["ICAO"] = icao.upper()
        return jsonify(airport_info)
    else:
        return jsonify({"error": "Airport not found"}), 404
if __name__ == '__main__':
    app.run(debug=True)