# Actividad: Implementación de un Pipeline de Datos en Tiempo Real

    API del clima → Airflow → Kafka → Spark

## 1. Configuración del entorno WSL (1 punto)

Crea una nueva instancia de WSL a partir de tu instalación de Ubuntu 24.04 actual. Exporta la imagen base, importa una copia con el nombre `UbuntuKafka` y verifica que aparece correctamente en el listado de instancias. Documenta cada comando utilizado y adjunta una captura de pantalla donde se muestre la nueva instancia activa. Al finalizar la actividad, registra también el comando necesario para eliminarla.

Crear un directorio ``pipelinenombre`` con la siguiente estrucura: 
```
pipelinenombre/
├── .venv/                 # Entorno virtual de Python (creado en el punto 2)
├── requirements.txt       # Listado de dependencias (generado en el punto 2)
├── airflow.cfg            # Fichero de configuración de Airflow (punto 3)
│   └── dags/                  # Carpeta de DAGs (configurada en el punto 3)
│       └── dag_1.py           # Tu DAG con las 3 tareas (punto 7)
├── app/                   # Para organizar mejor tus códigos
│   └── app.py                  # Consumidor de Spark (punto 6 y 10)
├── kafka/                 # Instalación de Kafka (punto 4)
└── spark/                 # Instalación de Apache Spark (punto 6)

```

## 2. Creación y configuración del entorno virtual Python (1 punto)

Dentro de la instancia WSL, en el directorio de trabajo llamado configura un entorno virtual de Python en su interior. Activa el entorno e instala las dependencias necesarias para el proyecto: `apache-airflow`, `confluent-kafka` y `Spark`.

Una vez instaladas todas las dependencias, genera el archivo `requirements.txt` ejecutando `pip freeze > requirements.txt`. Este archivo debe incluirse en la entrega ya que permite reproducir el entorno en cualquier otra máquina mediante `pip install -r requirements.txt`.

 Adjunta el archivo `requirements.txt` generado como parte de la entrega.

## 3. Puesta en marcha de Apache Airflow (1 punto)

Configura y arranca Apache Airflow en modo `standalone`. Antes de lanzarlo, realiza los siguientes ajustes en el fichero `airflow.cfg`:

- **Desactiva los DAGs de ejemplo** estableciendo `load_examples = False`, para que la interfaz no muestre los flujos de demostración predeterminados.
- **Crea la carpeta `dags/`** dentro del directorio de Airflow y verifica que la ruta `dags_folder` apunta correctamente a ella. Aquí es donde se alojarán los DAGs del proyecto.

Accede a la interfaz web, inicia sesión con las credenciales generadas automáticamente y adjunta una captura de la pantalla principal mostrando que no hay DAGs de ejemplo cargados. Explica brevemente cómo regenerar la contraseña en caso de necesitarlo.

## 4. Instalación y arranque de Apache Kafka (1 punto)

Descarga e instala Apache Kafka siguiendo los pasos indicados en la documentación oficial: [https://kafka.apache.org/quickstart](https://kafka.apache.org/quickstart). Instala Java 17 como requisito previo y configura Kafka en modo KRaft (sin Zookeeper).

Sigue el proceso completo: genera un ID de clúster, formatea el almacenamiento con el archivo de propiedades correspondiente y arranca el servidor. Verifica que Kafka está operativo ejecutando el comando de listado de topics y adjunta la salida obtenida en el terminal. Documenta cada comando ejecutado indicando brevemente su propósito.

## 5. Prueba de funcionamiento de Kafka (1 punto)

Con Kafka en marcha, realiza una prueba básica de mensajería abriendo **dos terminales simultáneamente**:

- En la **primera terminal**, lanza el productor de consola de Kafka apuntando al topic `pruebaname` y escribe al menos tres mensajes de texto manualmente.
- En la **segunda terminal**, lanza el consumidor de consola de Kafka suscrito al mismo topic y verifica que los mensajes aparecen en tiempo real.

Adjunta una captura de pantalla que muestre ambas terminales abiertas a la vez, con los mensajes escritos en el productor y recibidos en el consumidor. Esta prueba confirma que el broker funciona correctamente antes de integrar el resto del pipeline.

## 6. Instalación y arranque de Apache Spark (1 punto)

Descarga e instala Apache Spark desde la página oficial: [https://spark.apache.org/downloads.html](https://spark.apache.org/downloads.html). Selecciona la versión precompilada con Hadoop incluido (*"Pre-built for Apache Hadoop"*) y extrae el contenido dentro del directorio `spark/` de tu proyecto.

Arranca el clúster en modo standalone siguiendo la documentación oficial [https://spark.apache.org/docs/latest/spark-standalone.html](https://spark.apache.org/docs/latest/spark-standalone.html): primero el Master y después los Workers. Verifica que los **2** workers aparecen registrados correctamente en la Web UI del Master en `http://localhost:9090` y adjunta una captura de pantalla como evidencia.

## 7. Creación del DAG en Python (1 punto)

Crea el archivo `dag_1.py` dentro de la carpeta `dags/` de Airflow. El DAG debe contener tres tareas encadenadas:

1. `obtener_datos` — realiza la petición a la API de OpenWeatherMap y devuelve el JSON con los datos meteorológicos.
2. `print_json` — recupera el resultado de la tarea anterior mediante XCom y lo imprime por consola.
3. `json_serialization` — toma el JSON y lo publica en el topic `airflow-spark` utilizando el productor de `confluent-kafka`.

Asegúrate de que el DAG está adaptado a **Airflow 3.x** (importaciones correctas, parámetro `schedule` en lugar de `schedule_interval`, sin `provide_context`). Entrega el archivo `dag_1.py` completo y documenta brevemente la función de cada tarea.

Para poder consumir datos meteorológicos en tiempo real, regístrate en [OpenWeatherMap](https://openweathermap.org/), obtén una API key gratuita e indica cómo se incorpora al DAG.

```python
# Importaciones mínimas (solo lo esencial)
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

# PASO 1: DEFINIR EL DAG (el grafo)
# ========================================
dag = DAG(
    dag_id='dagnombre',                # NOMBRE ÚNICO DEL GRAFO
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
```

## 8. Comprobación del DAG en Airflow (1 punto)

Activa el DAG `dagnombre` desde la interfaz web de Airflow y observa su ejecución. Verifica que las tres tareas se completan correctamente en el orden establecido y que no hay errores en los logs. Adjunta las siguientes capturas:

- Vista del grafo del DAG mostrando las tres tareas encadenadas.
- Detalle de una ejecución exitosa con las tres tareas en verde.
- Log de la tarea `obtener_datos` mostrando el JSON de OpenWeatherMap impreso por consola.

## 9. Implementación del consumidor Spark Structured Streaming (1 punto)

Crea el archivo `app.py` dentro del directorio `app/` del proyecto. Este script debe implementar un consumidor de Spark Structured Streaming que se conecte al topic `airflow-spark` del broker Kafka, deserialice los mensajes JSON recibidos según un esquema definido con `StructType` y muestre los datos por consola.

Los campos mínimos que debe contemplar el esquema son: `name`, `main.temp`, `main.humidity`, `main.pressure` y `wind.speed`, extraídos del JSON que publica el DAG del punto 7.

Lanza la aplicación con `spark-submit` configurando **2 workers** locales (`local[2]`) e incluyendo el paquete de integración con Kafka. Con los tres componentes del pipeline activos en terminales independientes —Kafka, Airflow y Spark— activa el DAG y comprueba que el flujo funciona de extremo a extremo: Airflow consume la API, publica en Kafka y Spark recibe y procesa los mensajes en tiempo real. Adjunta una captura que muestre la salida del streaming con los datos meteorológicos recibidos correctamente.


#### app.py — Consumidor Spark Structured Streaming desde Kafka
>El script sigue este flujo en 4 bloques:

1. **Crear la sesión de Spark** — punto de entrada de cualquier aplicación PySpark, donde se define el nombre de la aplicación.
2. **Definir el esquema** — con ``StructType`` y ``StructField`` se declaran los campos que se esperan del JSON: nombre de la ciudad, temperatura, humedad, presión y velocidad del viento.
3. **Conectar a Kafka y leer el stream** — se indica el servidor de Kafka (``localhost:9092``) y el topic (``airflow-spark``). Los mensajes llegan en binario, por lo que hay que castear el campo ``value`` a string y luego parsearlo como JSON usando el esquema definido.
4. **Mostrar los datos por consola** — se seleccionan las columnas del esquema y se lanza el stream en modo ``append`` escribiendo en consola, esperando a que termine con ``awaitTermination``.

## 10. Análisis del flujo de datos y esquema del mensaje (1 punto)

Examina el JSON completo devuelto por la API de OpenWeatherMap y compáralo con el esquema definido en `app.py`. Identifica qué campos se extraen y explica cómo Spark los mapea a columnas del DataFrame resultante.

Propón al menos **dos campos adicionales** presentes en la respuesta de la API que podrían incorporarse al esquema, justifica su utilidad e implementa el cambio en el código. Entrega la versión modificada de `app.py` con los nuevos campos funcionando y adjunta una captura de la salida de Spark mostrando las nuevas columnas.

## Entrega

La entrega de esta actividad constará de dos partes:

**1. Archivos del proyecto** — Se deberán entregar los siguientes archivos:
- `requirements.txt` — dependencias del entorno virtual.
- `dag_1.py` — DAG de Airflow adaptado a la versión 3.x.
- `app.py` — consumidor de Spark con el esquema ampliado del apartado 10.

**2. Informe técnico** — Se redactará un informe siguiendo las pautas generales del curso. El informe debe incluir: portada con nombre, fecha y título de la actividad; índice numerado; desarrollo de cada uno de los 10 apartados con explicación de los pasos seguidos, comandos utilizados y capturas de pantalla como evidencia; apartado de conclusiones donde se reflexione sobre el funcionamiento del pipeline y las dificultades encontradas; y bibliografía o referencias consultadas.

El informe se entregará en el formato indicado por el profesor a través de la plataforma del curso antes de la fecha límite establecida.