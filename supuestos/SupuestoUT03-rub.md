### Apartado 1: Configuración del entorno WSL
* El alumnado exporta la imagen base de Ubuntu 24.04 e importa la nueva instancia con el nombre exacto `UbuntuKafka`, verificando su disponibilidad mediante el comando `wsl -l -v`.
* Se incluye una captura de pantalla clara donde se visualiza la instancia `UbuntuKafka` en estado "Running" o integrada en el listado oficial de WSL.
* Se documentan de forma secuencial y correcta los comandos `wsl --export`, `wsl --import` y el comando final `wsl --unregister` (o `terminate`) para la limpieza del entorno.
* La estructura de directorios `pipelinenombre` se crea fielmente a lo solicitado, demostrando la organización jerárquica de carpetas para Airflow, Kafka, Spark y la aplicación.

### Apartado 2: Creación y configuración del entorno virtual Python
* Se crea y activa un entorno virtual de Python dentro del directorio del proyecto, asegurando el aislamiento de las dependencias.
* La instalación de los paquetes `apache-airflow`, `confluent-kafka` y `pyspark` se realiza satisfactoriamente mediante el gestor de paquetes pip.
* El archivo `requirements.txt` se genera mediante el comando `pip freeze`, conteniendo todas las versiones específicas de las librerías necesarias para la replicabilidad del proyecto.
* Se entrega el archivo `requirements.txt` como evidencia técnica del entorno configurado, sin errores de dependencias cruzadas.

### Apartado 3: Puesta en marcha de Apache Airflow
* El servicio de Apache Airflow se inicializa correctamente en modo `standalone` dentro de la instancia WSL asignada.
* El fichero `airflow.cfg` presenta la modificación `load_examples = False` y la ruta `dags_folder` apunta correctamente al subdirectorio `dags/` creado en el Apartado 1.
* Se aporta una captura de pantalla de la interfaz web (UI) que demuestra la ausencia de DAGs de ejemplo y la operatividad del servidor.
* Se incluye una explicación técnica precisa sobre el procedimiento de recuperación o regeneración del archivo `standalone_admin_password.txt`.

### Apartado 4: Instalación y arranque de Apache Kafka
* Se confirma la instalación de Java 17 y la descarga de los binarios de Kafka, documentando cada paso del despliegue en el informe.
* La configuración de Kafka se realiza íntegramente en modo KRaft, incluyendo la generación del ID de clúster y el formateo de los logs de almacenamiento.
* Se evidencia el arranque del servidor Kafka mediante la ejecución del comando de listado de topics (`kafka-topics.sh --list`).
* Cada comando utilizado en el proceso de despliegue está acompañado de una descripción técnica que justifica su función dentro del ecosistema de mensajería.

### Apartado 5: Prueba de funcionamiento de Kafka
* Se demuestra la interacción síncrona entre un productor y un consumidor de consola utilizando el topic específico `pruebaname`.
* La captura de pantalla muestra simultáneamente ambas terminales, evidenciando que el flujo de mensajes es fluido y en tiempo real.
* Se verifica el envío de al menos tres mensajes de texto distintos que son recibidos íntegramente por el consumidor.
* La prueba confirma la correcta conectividad del broker Kafka y la capacidad de gestionar eventos antes de la integración con Spark.

### Apartado 6: Instalación y arranque de Apache Spark
* Se realiza la descarga e instalación de la versión de Spark con soporte para Hadoop dentro del directorio `spark/` definido en la estructura.
* El clúster se despliega exitosamente en modo standalone, iniciando primero el proceso Master y posteriormente los Workers.
* La captura de pantalla de la Web UI (`localhost:9090`) muestra claramente que existen 2 workers registrados y en estado "ALIVE".
* Se documentan los comandos de ejecución de los scripts de inicio (`start-master.sh` y `start-worker.sh`) con sus parámetros de red correspondientes.

### Apartado 7: Creación del DAG en Python
* El archivo `dag_1.py` implementa las tres tareas requeridas (`obtener_datos`, `print_json`, `json_serialization`) utilizando el `PythonOperator`.
* El código está adaptado estrictamente a Airflow 3.x, empleando el parámetro `schedule` y manejando correctamente los XComs para el paso de datos entre tareas.
* Se integra de forma funcional la API Key de OpenWeatherMap, permitiendo la extracción de datos reales de clima en formato JSON.
* La tarea de serialización utiliza la librería `confluent-kafka` para publicar el mensaje en el topic `airflow-spark` de forma asíncrona.

### Apartado 8: Comprobación del DAG en Airflow
* Se visualiza en la interfaz de Airflow la vista de grafo (Graph View) con la jerarquía correcta de dependencias entre las tres tareas.
* La evidencia muestra una ejecución exitosa (estado "success" en verde) del flujo completo sin errores de ejecución en el scheduler.
* Se incluye una captura del log específico de la tarea `obtener_datos` donde se puede leer el JSON crudo recibido de la API de clima.
* Se demuestra la activación manual del DAG y la monitorización de su progreso a través de las diferentes vistas de la UI de Airflow.

### Apartado 9: Implementación del consumidor Spark Structured Streaming
* El script `app.py` define correctamente un `StructType` para mapear los campos anidados del JSON (`main.temp`, `humidity`, etc.) a un esquema de Spark.
* Se utiliza `readStream` con el formato "kafka" especificando el servidor, el topic de origen y el tratamiento de los mensajes binarios a string/JSON.
* La aplicación se lanza mediante `spark-submit` incluyendo el parámetro `--packages` necesario para la conexión Spark-Kafka y configurando `local[2]`.
* La captura de pantalla final muestra el flujo de datos de extremo a extremo, con los resultados procesados por Spark apareciendo en la consola tras la ejecución del DAG.

### Apartado 10: Análisis del flujo de datos y esquema del mensaje
* Se realiza una comparación técnica detallada entre la respuesta JSON de la API y el esquema de datos implementado, explicando el proceso de aplanado (flattening).
* Se proponen y justifican dos campos adicionales (ej. visibilidad, coordenadas o descripción del clima) basados en su valor para un análisis de datos real.
* El código final de `app.py` integra los nuevos campos y se entrega como versión definitiva del consumidor de streaming.
* Se aporta una evidencia visual en la que se comprueba que las nuevas columnas aparecen correctamente en el DataFrame de Spark durante el procesamiento.