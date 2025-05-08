from airflow import DAG
import pendulum
from linkedin_operators import LinkedinExtractOperator


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
        skill='python',
        provide_context=True,
    )