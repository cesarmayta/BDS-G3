from prefect import task

@task(name="Mi primera tarea")
def task_primera_tarea():
    print("Esta es mi primera tarea con prefect...")