from prefect import flow
from tasks.task_prueba import task_prueba
from tasks.task_extract_neoauto import task_extract_neoauto
from tasks.task_transform_neoauto import task_transform_neauto

@flow(name="ETL Prueba")
def main_flow():
    #task_prueba()
    autos = task_extract_neoauto()
    autos_transform = task_transform_neauto(autos)
    print(autos_transform)

if __name__ == "__main__":
    main_flow()