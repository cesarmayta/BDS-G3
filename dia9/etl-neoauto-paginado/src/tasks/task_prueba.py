from prefect import task

@task(name="Tarea de Prueba")
def task_prueba():
    print("Esta es mi primera tarea con prefect...")