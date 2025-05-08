from airflow import DAG
from airflow.decorators import dag
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='2-bash-dag',
    description='Mi segundo DAG',
    start_date=datetime(2025, 1, 1),
    schedule_interval='@once',
) as dag:
    
    t1 = BashOperator(
        task_id='t1',
        bash_command='echo "Hola desde el DAG"'
    )