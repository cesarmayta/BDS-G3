from airflow import DAG
import pendulum
from linkedin_operators.extract_operator import LinkedinExtractOperator
from linkedin_operators.load_operator import LoadOffersOperator


with DAG(
    dag_id="6-linkedin-etl-dag",
    schedule_interval="@daily",
    description="ETL de ofertas de trabajo de LinkedIn",
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    catchup=False,
    tags=['etl linkedin']
) as dag:

    extract_task = LinkedinExtractOperator(
        task_id='extract',
        skill='python'
    )
    
    load_task = LoadOffersOperator(
        task_id='load',
        offers_key='linkedin_offers',
        mode='baseline'
    )
    
    extract_task >> load_task
