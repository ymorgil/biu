### Plantilla mínima para DAG de Airflow ###

# Importaciones mínimas (solo lo esencial)
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

# PASO 1: DEFINIR EL DAG (el grafo)
# ========================================
dag = DAG(
    dag_id='MI_PRIMER_DAG',           # NOMBRE ÚNICO DEL GRAFO
    start_date=datetime(2026, 3, 24),  # FECHA DE INICIO (cualquier día pasado)
    schedule_interval='@hourly',       # CUÁNDO EJECUTAR: @hourly, @daily, '0 2 * * *' (cron)
    catchup=False,                     # NO EJECUTAR PASADOS
    tags=['aprendizaje'],              # ETIQUETAS PARA BUSCAR EN UI
)

# PASO 2: FUNCIÓN PARA PRIMERA TAREA
# ========================================
def tarea_uno():
    """Función que hace algo simple (task 1)"""
    print("¡Hola desde la primera tarea!")
    resultado = "datos de tarea 1"
    return resultado  # Airflow lo guarda automáticamente en XCom

# PASO 3: FUNCIÓN PARA SEGUNDA TAREA
# ========================================
def tarea_dos(**context):
    """Función que recibe datos de la primera tarea (task 2)"""
    # RECOGER DATOS DE LA TAREA ANTERIOR
    datos_anteriores = context['ti'].xcom_pull(task_ids='tarea_simple_1')
    print(f"Recibí: {datos_anteriores}")
    print("¡Segunda tarea terminada!")

# PASO 4: CREAR LAS TAREAS (nodos del grafo)
# ========================================
task1 = PythonOperator(
    task_id='tarea_simple_1',    # ID ÚNICO (sin espacios)
    python_callable=tarea_uno,   # FUNCIÓN QUE EJECUTA
    dag=dag                     # PERTENECE A ESTE DAG
)

task2 = PythonOperator(
    task_id='tarea_simple_2',
    python_callable=tarea_dos,
    dag=dag
)

# PASO 5: DEFINIR DEPENDENCIAS (flechas del grafo)
# ========================================
task1 >> task2  # task1 PRIMERO, luego task2
