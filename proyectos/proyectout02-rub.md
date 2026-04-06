Rúbrica de Evaluación: Proyecto Ecosistema Hadoop y EMR

Apartado 1: Creación del clúster de procesamiento

    Configuración correcta del clúster EMR (instancias Master y Core) según las especificaciones.

    Captura de pantalla del dashboard de AWS donde el clúster aparezca en estado "Waiting" o "Running".

    Identificación correcta de los IDs de las instancias y el tipo de hardware seleccionado.

    Explicación del rol de los nodos (Maestro y Trabajo) dentro del entorno desplegado.

Apartado 2: Conexión al nodo maestro del clúster

    Conexión exitosa mediante protocolo SSH utilizando la clave .pem o .ppk correspondiente.

    Captura de la terminal donde se visualice el banner de Amazon Linux y el prompt del sistema.

    Ejecución de un comando de prueba (ej. ls o whoami) que confirme el acceso.

    Descripción de los directorios iniciales encontrados al acceder al nodo maestro.

Apartado 3: Exploración del entorno del clúster

    Identificación de al menos tres herramientas instaladas (ej. Hadoop, Hive, Spark).

    Verificación de la versión de Hadoop mediante línea de comandos (hadoop version).

    Captura de pantalla listando los binarios o servicios activos en el sistema.

    Breve descripción de la utilidad detectada para el comando hadoop fs.

Apartado 4: Acceso a las interfaces de administración

    Acceso correcto a la interfaz web de HDFS o de HUE desde el navegador.

    Captura de pantalla de la interfaz mostrando el estado del "NameNode" o el editor de consultas.

    Identificación de los recursos disponibles (capacidad de almacenamiento y nodos activos).

    Breve análisis sobre la utilidad de estas interfaces para la monitorización del sistema.

Apartado 5: Primer contacto con el sistema de archivos distribuido

    Creación correcta del directorio /input dentro de HDFS.

    Captura de pantalla de la terminal ejecutando el comando de listado (ls -R /).

    Verificación de que los permisos del directorio permiten la escritura de datos.

    Confirmación por consola de que el directorio está vacío y listo para recibir el dataset.

Apartado 6: Preparación del conjunto de datos

    Creación manual del archivo turismo_canarias.csv con el contenido íntegro de 50 registros.

    Ejecución correcta del comando wc -l mostrando exactamente 51 líneas.

    Captura de pantalla del comando head mostrando las primeras filas y la cabecera del archivo.

    Verificación de que el formato (delimitador por comas) es consistente en todo el fichero.

Apartado 7: Importación de datos hacia el sistema distribuido

    Uso correcto del comando put o copyFromLocal para subir el archivo a HDFS.

    Captura de pantalla que demuestre que el archivo reside ahora en el directorio /input de HDFS.

    Verificación del tamaño del archivo en HDFS y su factor de replicación (si aplica).

    Explicación de la diferencia entre tener el archivo en el disco local frente a tenerlo en HDFS.

Apartado 8: Creación de una base de datos analítica

    Declaración correcta de la tabla externa en Hive con los tipos de datos asignados (int, string, float).

    Definición adecuada de los delimitadores de campo (ROW FORMAT DELIMITED FIELDS TERMINATED BY ',').

    Captura de pantalla del comando DESCRIBE o SHOW TABLES confirmando la estructura.

    Confirmación de que la tabla apunta correctamente a la ruta de HDFS donde está el CSV.

Apartado 9: Exploración de los datos mediante consultas

    Ejecución de las tres consultas solicitadas (suma de turistas, gasto máximo y promedios).

    Captura de los resultados obtenidos por consola o a través de la interfaz HUE.

    Identificación del tiempo de respuesta o de la generación de tareas MapReduce/Tez.

    Veracidad de los resultados obtenidos según el dataset de turismo proporcionado.

Apartado 10: Interpretación del proceso realizado

    Redacción clara que demuestre la comprensión del flujo "Ingesta -> Almacenamiento -> Consulta".

    Explicación coherente sobre la importancia de la escalabilidad en el contexto canario (sector turístico).

    Reflexión técnica sobre el papel del nodo maestro como coordinador del clúster.

    Justificación del uso de arquitecturas distribuidas frente a sistemas tradicionales para grandes volúmenes.