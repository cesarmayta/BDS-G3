from prefect import flow
from tasks.task import (task_primera_tarea)
from tasks.task_extract_linkedin import (
    task_extract_linkedin)
from tasks.task_load_offers import (
    task_load_offers_baseline,
    task_load_offers_update
)

TYPE_TASK = 'baseline'

@flow(name="ETL DE OFERTAS LABORALES")
def main_flow():
    #task_primera_tarea()
    search = ['python']
    for s in search:
        offers = task_extract_linkedin(s)
        if offers:
            print(f"se encontraron {offers.__len__()} ofertas de {s}")
            if TYPE_TASK == 'baseline':
                task_load_offers_baseline(offers)
            else:
                task_load_offers_update(offers)
        else:
            print(f'No se encontraron ofertas para {s}')
    
if __name__ == "__main__":
    main_flow()