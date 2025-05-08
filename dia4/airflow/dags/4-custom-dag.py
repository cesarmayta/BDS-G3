from airflow import DAG
from request_operator import RequestOperator
from datetime import datetime

with DAG(
    dag_id='4-custom-dag',
    description='Mi cuarto DAG con RequestOperator',
    start_date=datetime(2025, 1, 1),
    schedule_interval='@once',
) as dag:
    
    t1 = RequestOperator(
        task_id='t1',
        url='https://randomuser.me/api/?results=10',
    )