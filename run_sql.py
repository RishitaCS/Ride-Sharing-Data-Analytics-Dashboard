import sqlite3
import pandas as pd

DB_PATH = "data/rides.db"

def run_query(query):
    with sqlite3.connect(DB_PATH) as conn:
        return pd.read_sql_query(query, conn)

if __name__ == "__main__":
    # Total rides and cancellations
    q1 = """
    SELECT COUNT(*) AS total_rides,
           SUM(CASE WHEN trip_status='completed' THEN 1 ELSE 0 END) AS completed_rides,
           SUM(CASE WHEN trip_status!='completed' THEN 1 ELSE 0 END) AS cancelled_rides
    FROM trips;
    """
    print(run_query(q1))

    # Peak ride hours
    q2 = """
    SELECT CAST(strftime('%H', trip_start_time) AS INTEGER) AS hour, COUNT(*) AS rides
    FROM trips
    GROUP BY hour
    ORDER BY rides DESC;
    """
    print(run_query(q2).head())

    # Average fare per km
    q3 = """
    SELECT AVG(price_usd / NULLIF(distance_kms,0)) AS avg_fare_per_km
    FROM trips
    WHERE distance_kms > 0;
    """
    print(run_query(q3))
