from datetime import datetime
import requests
import json
from airflow.operators.python import PythonOperator
from airflow import DAG


def getWeeks():
    response = requests.get(
        "https://api.sportsdata.io/v3/nfl/stats/json/ScoresFinal/2023?key=1455ced235a74c71862688fb1a38dc7f")
    data = json.loads(response.text)
    with open('/opt/airflow/data/weeks_output.txt', 'w') as f:
        for item in data:
            f.write(str(item) + '\n')
    return data


def getSeasons():
    response = requests.get(
        "https://api.sportsdata.io/v3/nfl/scores/json/Standings/2023?key=1455ced235a74c71862688fb1a38dc7f")
    data = json.loads(response.text)
    with open('/opt/airflow/data/seasons_output.txt', 'w') as f:
        for item in data:
            f.write(str(item) + '\n')
    return data


with DAG("my_dag",
         start_date=datetime(2025, 2, 4),
         schedule_interval='@daily',
         catchup=False):

    getWeeks = PythonOperator(
        task_id="getWeeks",
        python_callable=getWeeks
    )

    getSeasons = PythonOperator(
        task_id="getSeasons",
        python_callable=getSeasons
    )

getWeeks >> getSeasons