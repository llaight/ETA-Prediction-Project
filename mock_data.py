import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from geopy.distance import geodesic
import random

#Settings
NUM_SAMPLE = 1000
MIN_LAT, MAX_LAT = 12.0, 18.5
MIN_LNG, MAX_LNG = 118.0, 122.0
START_DATE = datetime(2023, 7, 1)
END_DATE = datetime(2023, 8, 1)
DRIVER_IDS = [f"driver_{i}" for i in range(1, 21)] 

def random_point():
    return(np.random.uniform(MIN_LAT, MAX_LAT), np.random.uniform(MIN_LNG, MAX_LNG))

def random_date(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

rows= []

for i in range(NUM_SAMPLE):
    pickup_lat, pickup_lng = random_point()
    dropoff_lat, dropoff_lng = random_point()
    pickup_time = random_date(START_DATE, END_DATE)

    distance = geodesic((pickup_lat, pickup_lng), (dropoff_lat, dropoff_lng)).km
    base_speed_kmh = 40
    travel_time_hours = distance/ base_speed_kmh

    noise_factor= np.random.uniform(0.5, 1.5)
    travel_time_hours *= noise_factor

    dropoff_time = pickup_time + timedelta(hours=travel_time_hours)

    driver_id = random.choice(DRIVER_IDS)

    print(f"Generating order {i+1}/{NUM_SAMPLE}: Pickup({pickup_lat}, {pickup_lng}), Dropoff({dropoff_lat}, {dropoff_lng}), Pickup Time: {pickup_time}, Dropoff Time: {dropoff_time}, Driver ID: {driver_id}")

    rows.append({
        "order_id": f"order_{i+1}",
        "pickup_lat": pickup_lat,
        "pickup_lng": pickup_lng,
        "dropoff_lat": dropoff_lat,
        "dropoff_lng": dropoff_lng,
        "pickup_time": pickup_time,
        "dropoff_time": dropoff_time,
        "driver_id": driver_id
    })

df = pd.DataFrame(rows)
df.to_csv("Team_task/data/historical_deliveries.csv", index=False)
print("Simulated data saved as historical_deliveries.csv")