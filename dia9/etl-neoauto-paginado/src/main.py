import time
from prefect import flow
#from tasks.task_prueba import task_prueba
from tasks.task_extract_neoauto import task_extract_neoauto
from tasks.task_transform_neoauto import task_transform_neauto
from tasks.task_load_neoauto import task_load_neoauto
from tasks.task_extract_total_pages import task_extra_total_pages

@flow(name="ETL Prueba")
def main_flow():
    #task_prueba()}
    #PASO 1 - EXTRAER DATA
    total_pages = task_extra_total_pages()
    print(f'total pages : {total_pages}')
    for page in range(1,total_pages + 1,1):
        print(f'extract page {page}...')
        autos = task_extract_neoauto(page)
        #PASO 2 - TRANSFORMAR DATA
        autos_transform = task_transform_neauto(autos)
        #PASO 3 - CARGAR DATA
        task_load_neoauto(autos_transform)
        time.sleep(1)

if __name__ == "__main__":
    main_flow()