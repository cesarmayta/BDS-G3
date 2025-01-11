from prefect import flow
from tasks.task_prueba import task_prueba

@flow(name="ETL Prueba")
def main_flow():
    task_prueba()
    

if __name__ == "__main__":
    main_flow()