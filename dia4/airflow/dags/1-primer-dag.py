from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(
    dag_id='1-primer-dag',
    description='Mi primer DAG',
    start_date=datetime(2025, 1, 1),
    schedule_interval='@once',
) as dag:
    
    t1 = EmptyOperator(task_id='t1')
