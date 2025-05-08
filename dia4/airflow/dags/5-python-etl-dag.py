import json
import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator


with DAG(
    dag_id="python_etl_dag",
    schedule_interval="@daily",
    description="ETL simple con python operator",
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    catchup=False,
    tags=['etl dag example']
) as dag:
    
    def extract(**kwargs):
        ti = kwargs['ti']
        print("Extracting data...")
        data_string = '{"1001": 301.27, "1002": 433.21, "1003": 502.22}'
        print(data_string)
        ti.xcom_push(key='order_data', value=data_string)
        
    def transform(**kwargs):
        ti = kwargs['ti']
        print("Transforming data...")
        extract_data_string = ti.xcom_pull(key='order_data', task_ids='extract')
        print(extract_data_string)
        order_data = json.loads(extract_data_string)
        
        total_order_value = 0
        for value in order_data.values():
            total_order_value += value
        print(f'Total order value: {total_order_value}')
        total_value = {"total_order_value": total_order_value}
        ti.xcom_push(key='total_order_value', value=json.dumps(total_value))
        
    def load(**kwargs):
        ti = kwargs['ti']
        print("Loading data...")
        load_data_string = ti.xcom_pull(key='total_order_value', task_ids='transform')
        print(load_data_string)
        load_data = json.loads(load_data_string)
        
        with open('total_order_value.json', 'w') as f:
            json.dump(load_data, f)
        print("Data loaded successfully!")
        
    extract_task = PythonOperator(
        task_id='extract',
        python_callable=extract,
        provide_context=True,
    )
    
    transform_task = PythonOperator(
        task_id='transform',
        python_callable=transform,
        provide_context=True,
    )
    
    load_task = PythonOperator(
        task_id='load',
        python_callable=load,
        provide_context=True,
    )
    
    extract_task >> transform_task >> load_task