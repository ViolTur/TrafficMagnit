import psycopg2
import os

try:
    conn = psycopg2.connect(
        dbname="traffic_magnit_db",
        user="TrafficMagnit",
        password="TrafficMagnitPass",
        host="localhost",
        port="5432"
    )
    print("Connected to TrafficMagni")
    conn.close()
except Exception as e:
    print(f" Error connecting to TrafficMagni: {e}")