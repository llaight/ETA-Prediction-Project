from flask import Flask, request, jsonify, render_template
import joblib
from util import get_eta_minutes, harvesine_km
import psycopg2
import pytz
from datetime import datetime
from dotenv import load_dotenv
import os
from geopy.geocoders import OpenCage

from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})
model = joblib.load("model/delivery_eta_lr.pkl")


load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

api_key = os.getenv("API_KEY")
geolocator = OpenCage(api_key=api_key)

def get_lat_lng_from_address(address):
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

@app.route("/predict_eta", methods=["POST"])
def predict_eta():
    data = request.get_json()

    # ✅ Correctly access by string key
    order_id = data.get("order_id")
    driver_id = data.get("driver_id")
    current_lat, current_lng = get_lat_lng_from_address(data.get("current_location"))
    dropoff_lat, dropoff_lng = get_lat_lng_from_address(data.get("dropoff_location"))

    # ✅ Validate all fields are present
    if None in (current_lat, current_lng, dropoff_lat, dropoff_lng):
        return jsonify({"error": "Missing required location fields"}), 400

    # ✅ Calculate ETA
    eta = get_eta_minutes(current_lat, current_lng, dropoff_lat, dropoff_lng, model)

    if eta <= 0.5:
        message = "Arrived"
    elif eta < 5:
        message = "Arriving Soon!"
    elif eta < 15:
        message = "On the way."
    else:
        message = "En route."

    # db connection
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
                INSERT INTO eta_logs(order_id, driver_id, current_lat, current_lng, dropoff_lat, dropoff_lng, eta_minutes, status_message)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, (order_id, driver_id, current_lat, current_lng, dropoff_lat, dropoff_lng, round(eta, 2), message))
    
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"eta_minutes": round(eta, 2), "message": message, "status": "saved in db"})


@app.route("/eta_logs", methods=["GET"])
def eta_logs():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM eta_logs")
    logs = cur.fetchall()
    manila_tz = pytz.timezone("Asia/Manila")
    formatted_logs = []
    for row in logs:
        row = list(row)
        # If last column is datetime
        if isinstance(row[-1], datetime):
            row[-1] = row[-1].astimezone(manila_tz).strftime("%Y-%m-%d %H:%M:%S")
        formatted_logs.append(row)

    cur.close()
    conn.close()
    return jsonify(formatted_logs)



if __name__ == "__main__":
    app.run(debug=True, port=5001)