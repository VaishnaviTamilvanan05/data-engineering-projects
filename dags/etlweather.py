from airflow import DAG
from airflow.providers.http.hooks.http import HttpHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.decorators import task
from airflow.utils.dates import days_ago
import requests
import json

# Locations for the desired U.S. states
LOCATIONS = [
    {"name": "Albany", "state": "New York", "latitude": "42.6526", "longitude": "-73.7562"},
    {"name": "Austin", "state": "Texas", "latitude": "30.2672", "longitude": "-97.7431"}
]

POSTGRES_CONN_ID = 'postgres_default'
API_CONN_ID = 'open_meteo_api'

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1)
}

# DAG definition
with DAG(dag_id='weather_etl_pipeline',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:
    
    @task()
    def extract_weather_data(location):
        """Extract weather data for a specific location."""
        http_hook = HttpHook(http_conn_id=API_CONN_ID, method='GET')

        # Build the API endpoint
        endpoint = f"/v1/forecast?latitude={location['latitude']}&longitude={location['longitude']}&current_weather=true"

        # Make the request via the HTTP Hook
        response = http_hook.run(endpoint)

        if response.status_code == 200:
            weather_data = response.json()
            weather_data['location'] = location['name']
            weather_data['state'] = location['state']
            weather_data['latitude'] = location['latitude']
            weather_data['longitude'] = location['longitude']
            return weather_data
        else:
            raise Exception(f"Failed to fetch weather data for {location['name']}: {response.status_code}")

    @task()
    def transform_weather_data(weather_data):
        """Transform the extracted weather data."""
        current_weather = weather_data['current_weather']
        transformed_data = {
            'location': weather_data['location'],
            'state': weather_data['state'],
            'latitude': weather_data['latitude'],
            'longitude': weather_data['longitude'],
            'temperature': current_weather['temperature'],
            'windspeed': current_weather['windspeed'],
            'winddirection': current_weather['winddirection'],
            'weathercode': current_weather['weathercode']
        }
        return transformed_data

from airflow import DAG
from airflow.providers.http.hooks.http import HttpHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.decorators import task
from airflow.utils.dates import days_ago
import json
import time

# Locations for the desired U.S. states
LOCATIONS = [
    {"name": "Albany", "state": "New York", "latitude": "42.6526", "longitude": "-73.7562"},
    {"name": "Austin", "state": "Texas", "latitude": "30.2672", "longitude": "-97.7431"}
]

POSTGRES_CONN_ID = 'postgres_default'
API_CONN_ID = 'open_meteo_api'

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1)
}

with DAG(dag_id='weather_etl_pipeline',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    @task()
    def extract_weather_data(location):
        """Extract weather data for a specific location."""
        http_hook = HttpHook(http_conn_id=API_CONN_ID, method='GET')

        # Build the API endpoint
        endpoint = f"/v1/forecast?latitude={location['latitude']}&longitude={location['longitude']}&current_weather=true"

        # Make the request via the HTTP Hook
        response = http_hook.run(endpoint)

        if response.status_code == 200:
            weather_data = response.json()
            weather_data['location'] = location['name']
            weather_data['state'] = location['state']
            weather_data['latitude'] = location['latitude']
            weather_data['longitude'] = location['longitude']
            return weather_data
        else:
            raise Exception(f"Failed to fetch weather data for {location['name']}: {response.status_code}")

    @task()
    def transform_weather_data(weather_data):
        """Transform the extracted weather data."""
        current_weather = weather_data['current_weather']
        transformed_data = {
            'location': weather_data['location'],
            'state': weather_data['state'],
            'latitude': weather_data['latitude'],
            'longitude': weather_data['longitude'],
            'temperature': current_weather['temperature'],
            'windspeed': current_weather['windspeed'],
            'winddirection': current_weather['winddirection'],
            'weathercode': current_weather['weathercode']
        }
        return transformed_data

    @task()
    def load_weather_data(transformed_data):
        """Load transformed data into PostgreSQL."""
        pg_hook = PostgresHook(postgres_conn_id=POSTGRES_CONN_ID)
        conn = pg_hook.get_conn()
        cursor = conn.cursor()

        # Create table with the correct schema
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_data (
            location VARCHAR(50),
            state VARCHAR(50),
            latitude FLOAT,
            longitude FLOAT,
            temperature FLOAT,
            windspeed FLOAT,
            winddirection FLOAT,
            weathercode INT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

        # Insert transformed data into the table
        cursor.execute("""
        INSERT INTO weather_data (location, state, latitude, longitude, temperature, windspeed, winddirection, weathercode)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            transformed_data['location'],
            transformed_data['state'],
            transformed_data['latitude'],
            transformed_data['longitude'],
            transformed_data['temperature'],
            transformed_data['windspeed'],
            transformed_data['winddirection'],
            transformed_data['weathercode']
        ))

        conn.commit()
        cursor.close()

    # DAG Workflow - ETL Pipeline for multiple locations
    for location in LOCATIONS:
        weather_data = extract_weather_data(location=location)
        transformed_data = transform_weather_data(weather_data=weather_data)
        load_weather_data(transformed_data=transformed_data)
