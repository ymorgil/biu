# Rúbricas — Supuesto Práctico 04: Observabilidad y Monitorización

---

### Apartado 1: Estructura del proyecto en Docker
- La estructura de carpetas del proyecto está correctamente definida y organizada, diferenciando claramente los directorios destinados a Spark, monitorización y configuración.
- Se aporta una captura de pantalla o listado del árbol de directorios (`tree` o equivalente) que muestra todos los archivos y carpetas del proyecto con su disposición correcta.
- Cada carpeta y archivo del proyecto tiene una función justificada, explicando qué contiene y por qué está ubicado en ese lugar dentro de la estructura.
- Se incluye una descripción de la arquitectura general del sistema, relacionando los componentes del stack (Spark, Prometheus, Grafana, Alertmanager, Node Exporter) con los archivos y carpetas que los configuran.

---

### Apartado 2: Despliegue del clúster Spark con Docker Compose
- El archivo `docker-compose.spark.yml` está correctamente definido e incluye 1 nodo master y 3 nodos worker Spark con los puertos correctamente mapeados.
- Los contenedores arrancan sin errores y los 4 nodos (master + 3 workers) aparecen en estado `running` al ejecutar `docker ps`.
- Se aporta una captura de pantalla de la interfaz web del Spark Master (http://localhost:8080) donde se visualizan los 3 workers registrados y en estado `ALIVE`.
- Se incluye una explicación técnica sobre el rol de cada parámetro relevante del `docker-compose.spark.yml`, justificando las decisiones de configuración adoptadas (red, volúmenes, variables de entorno, etc.).

---

### Apartado 3: Añadir Prometheus para recolectar métricas del clúster
- El archivo `prometheus.yml` está correctamente definido con los targets de scraping apuntando al clúster Spark y al Node Exporter, con intervalos de recolección apropiados.
- El archivo `grafana.ini` contiene una configuración básica válida (puerto, acceso, credenciales por defecto u otros parámetros relevantes).
- El archivo `docker-compose.monitoring.yml` levanta correctamente los tres servicios requeridos (Prometheus, Grafana y Node Exporter) sin errores, y los contenedores aparecen en estado `running`.
- Se aporta una captura de pantalla de la interfaz de Prometheus (http://localhost:9090/targets) donde se muestra que todos los targets configurados están en estado `UP`.

---

### Apartado 4: Configurar Grafana y conectar con Prometheus
- Grafana está conectado correctamente a Prometheus como datasource, verificado mediante la prueba de conexión exitosa desde la interfaz de Grafana.
- El dashboard **Spark Cluster Monitoring** incluye una primera fila dedicada al nodo master con 5 paneles, entre los cuales figuran obligatoriamente el uso de CPU y el uso de memoria.
- El dashboard incluye una segunda fila dedicada a los workers con 5 paneles basados en métricas obtenidas desde Prometheus que permiten analizar el estado y comportamiento de los nodos worker.
- Se aporta una captura de pantalla del dashboard completo con datos en tiempo real visibles en todos los paneles, demostrando que las visualizaciones funcionan correctamente.

---

### Apartado 5: Reinicio del sistema de monitorización y análisis de incidencias
- Se documenta el proceso completo de parada y reinicio del sistema de monitorización con los comandos utilizados y el resultado obtenido tras el arranque.
- Se identifica claramente la incidencia detectada tras el reinicio (pérdida de datos del dashboard, configuración no persistente, etc.) y se explica la causa técnica que la origina.
- Se propone e implementa una solución técnica concreta con los cambios realizados en los archivos de configuración.
- Se valida la solución mediante un nuevo reinicio del sistema, aportando capturas de pantalla que demuestren que la incidencia ha quedado resuelta y los datos persisten correctamente.

---

### Apartado 6: Ejecución del job de Spark SQL
- El dataset de Netflix está correctamente descargado desde Kaggle y ubicado en la carpeta accesible por el contenedor Spark, y el archivo `job.py` está disponible en el nodo master.
- El job se ejecuta correctamente desde el nodo master sin errores y se aporta una captura de la salida por terminal con los resultados obtenidos
- Se responden correctamente las 5 preguntas planteadas (número de Movies y TV Shows, país con más producciones, año con más lanzamientos, director con más títulos y categoría más frecuente) con los valores exactos que devuelve el job sin logs.
- Se incluye el código del archivo `job.py` con una explicación de las transformaciones y consultas Spark SQL utilizadas para obtener cada uno de los resultados.

---

### Apartado 7: Observación de métricas en Grafana durante el job
- Se aporta una captura de pantalla del dashboard **Spark Cluster Monitoring** tomada durante la ejecución del job, donde se aprecia un cambio visible en al menos uno de los paneles respecto al estado en reposo.
- Se responde de forma justificada a la pregunta sobre el comportamiento del uso de CPU durante la ejecución, describiendo la variación observada y relacionándola con la actividad del job.
- Se responde con datos concretos a la pregunta sobre el consumo máximo de memoria del clúster en el momento de mayor carga, identificando el panel y el valor registrado.
- Se responde razonadamente a la pregunta sobre la participación de los workers, indicando si los tres nodos procesaron datos de forma equitativa o si hubo diferencias, y explicando por qué.

---

### Apartado 8: Alerta de uso de CPU
- El archivo `rules.yml` está correctamente modificado con una regla de alerta que se dispara cuando el uso de CPU supera el 60% durante más de 10 segundos, con la expresión PromQL y los labels adecuados.
- Se ejecuta una prueba de estrés desde el nodo master que genera carga suficiente para superar el umbral configurado, documentando el comando utilizado.
- Se aportan capturas de pantalla de la interfaz de Prometheus (http://localhost:9090/alerts) que muestran la alerta pasando por los estados `PENDING` y `FIRING` de forma secuencial.
- Se aporta una captura de pantalla de la interfaz de Alertmanager (http://localhost:9093) donde se confirma que la alerta aparece correctamente recibida y agrupada.

---

### Apartado 9: Alerta de worker caído con notificación a Telegram
- Los archivos `rules.yml` y `alertmanager.yml` están correctamente modificados para detectar la caída de un worker y enrutar la notificación hacia un bot de Telegram con el token y chat ID configurados.
- Se ejecuta la parada manual del worker con `docker stop spark-worker-2` y se aporta una captura que muestra la alerta en estado `FIRING` en la interfaz de Prometheus.
- Se aporta una captura de pantalla de la interfaz de Alertmanager confirmando que la alerta del worker caído aparece correctamente recibida.
- Se aporta una captura de pantalla del chat de Telegram donde se visualiza el mensaje de notificación recibido correctamente desde Alertmanager, con el contenido de la alerta legible.

---

### Apartado 10: Visualización del clúster con Ganglia
- El archivo `docker-compose.ganglia.yml` está correctamente definido e integrado con la infraestructura del clúster Spark, y el contenedor arranca sin errores con la interfaz web accesible.
- Se aporta una captura de pantalla de la interfaz web de Ganglia mostrando métricas activas del clúster (CPU, memoria u otras disponibles).
- Se realiza una comparativa estructurada entre Ganglia y Grafana, identificando qué métricas están disponibles en cada herramienta y cuáles son las diferencias en la forma de visualización.
- Se incluye una reflexión razonada sobre los escenarios de uso más adecuados para cada herramienta, argumentando en qué contextos resultaría más conveniente emplear una u otra.

### Rubricas de la entrega
* Por cada pauta del curso incumplida restamos 0.5 en cualquiera de los apartados anteriores.