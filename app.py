import streamlit as st
import pandas as pd
import sqlite3

DB_PATH = "data/rides.db"

# Load data
with sqlite3.connect(DB_PATH) as conn:
    df = pd.read_sql_query("SELECT * FROM trips", conn)

# Convert datetime
df['trip_start_time'] = pd.to_datetime(df['trip_start_time'], errors='coerce')

# Sidebar filters
cities = df['city'].dropna().unique().tolist()
selected_city = st.sidebar.selectbox("Select City", ["All"] + list(cities))

start_date = st.sidebar.date_input("Start Date", df['trip_start_time'].min().date())
end_date = st.sidebar.date_input("End Date", df['trip_start_time'].max().date())

# Apply filters
filtered = df.copy()
if selected_city != "All":
    filtered = filtered[filtered['city'] == selected_city]
filtered = filtered[(filtered['trip_start_time'].dt.date >= start_date) & 
                    (filtered['trip_start_time'].dt.date <= end_date)]

# KPIs
total_rides = len(filtered)
completed_rides = (filtered['trip_status'] == 'completed').sum()
cancelled_rides = total_rides - completed_rides
avg_distance = filtered['distance_kms'].mean()
avg_fare = filtered['price_usd'].mean()
avg_wait = filtered['wait_time'].mean()

st.title("Ride-Sharing Analytics Dashboard")
st.metric("Total Rides", total_rides)
st.metric("Completed Rides", completed_rides)
st.metric("Cancelled Rides", cancelled_rides)
st.metric("Avg Distance (kms)", f"{avg_distance:.2f}")
st.metric("Avg Fare (USD)", f"{avg_fare:.2f}")
st.metric("Avg Wait Time (mins)", f"{avg_wait:.2f}")

# Peak hours chart
filtered['hour'] = filtered['trip_start_time'].dt.hour
hourly = filtered.groupby('hour').size().reset_index(name='rides')
st.subheader("Rides by Hour")
st.bar_chart(hourly.set_index('hour')['rides'])
