# Apache Airflow - DAGs y Menú Principal

## ¿Qué es un DAG en Airflow?

**DAG** (Directed Acyclic Graph, o *grafo dirigido acíclico*) es el componente principal en Apache Airflow. Representa un flujo de trabajo: una colección de tareas ordenadas con dependencias lógicas, sin ciclos.

### Características de un DAG:
- **Dirigido**: las tareas tienen un orden específico.
- **Acíclico**: no puede haber ciclos; es decir, una tarea no puede depender de sí misma directa o indirectamente.
- **Definido en Python**: los DAGs se escriben como scripts Python.
- **Ejecutado por el Scheduler**: el planificador de Airflow los detecta y ejecuta según su programación (`schedule_interval`).

### Elementos clave en un DAG:
- `dag_id`: identificador único del DAG.
- `schedule_interval`: frecuencia de ejecución (e.g., `"@daily"`, `"0 12 * * *"`, `None`).
- `default_args`: diccionario con parámetros comunes (como `owner`, `start_date`, `retries`).
- `tasks`: tareas individuales que se conectan mediante dependencias (`task_1 >> task_2`).

---

## Opciones del Menú Principal de la Interfaz Web de Airflow

La interfaz web de Airflow proporciona un dashboard muy útil. Las principales secciones del menú son:

### 1. **DAGs**
- Lista de todos los DAGs registrados.
- Puedes activar/desactivar, ejecutar manualmente o pausar DAGs.
- También puedes acceder a vistas específicas del DAG (como Tree View, Graph View, etc.).

### 2. **Browse**
- **DAG Runs**: historial de ejecuciones por DAG.
- **Task Instances**: registros detallados de tareas ejecutadas.
- **Jobs**: muestra los procesos en segundo plano (scheduler, triggerer, etc.).
- **Logs**: acceso a logs históricos.
- **XComs**: muestra los datos intercambiados entre tareas.

### 3. **Admin**
- **Connections**: gestiona conexiones a bases de datos, APIs, S3, etc.
- **Variables**: define variables globales para usarlas en los DAGs.
- **Pools**: limita el número de tareas concurrentes por grupo.
- **Configuration**: muestra el archivo de configuración actual (`airflow.cfg`).
- **Users** (si está activado el control de acceso): gestión de usuarios y permisos.

### 4. **Docs**
- Accesos rápidos a la documentación oficial de Airflow.

### 5. **Security** (si RBAC está habilitado)
- Permite gestionar roles y
