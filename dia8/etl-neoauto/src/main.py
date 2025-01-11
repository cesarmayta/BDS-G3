from prefect import flow
from tasks.task_prueba import task_prueba
from tasks.task_extract_neoauto import task_extract_neoauto

@flow(name="ETL Prueba")
def main_flow():
    #task_prueba()
    autos = task_extract_neoauto()
    print(autos)

if __name__ == "__main__":
    main_flow()