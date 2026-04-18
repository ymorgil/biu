# SUPUESTO PRÁCTICO 04: Observabilidad y monitorización

![header](/web/img/sp04-header.png)

En este proyecto desplegarás un clúster Spark con 1 nodo master y 3 nodos worker usando Docker Compose. Añadirás monitorización con Prometheus, Grafana y Alertmanager, y luego un contenedor extra con Ganglia para comparar interfaces. Finalmente, ejecutarás pequeños jobs de Spark SQL y verás cómo cambian las métricas en las gráficas.

**``Objetivos del proyecto``**
1. Desplegar un clúster Spark con 1 master y 3 workers usando Docker Compose.
2. Añadir un Prometheus + Grafana + Alertmanager para monitorizar el clúster.
3. Visualizar métricas de CPU, memoria y uso de recursos de Spark.
4. Configurar una alerta simple con Alertmanager (por ejemplo, uso de CPU > 80%).
5. Añadir un contenedor con Ganglia para visualizar el clúster.
6. Ejecutar un pequeño job de Spark SQL y ver cómo cambian las gráficas en Grafana.

**Arquitectura**
```bash
node-exporter:9100  ──┐
                      ├──▶  Prometheus  ──▶  Grafana (visualiza)
spark-master:8080   ──┤         │
spark-worker-1:8080 ──┤         └──▶  Alertmanager (dispara alertas)
spark-worker-2:8080 ──┤
spark-worker-3:8080 ──┘
```

**📦Componentes del Stack**
| Servicio                  | Puerto | Descripción |
| :-------------------------|:-----| :--- |
| **Spark Master (UI)**     | 8080 | Interfaz web de monitoreo del clúster Spark |
| **Spark Worker (UI)**     | 8081 | Interfaz web de monitoreo del nodo de trabajo |
| **Spark Master (RPC)**    | 7077 | Comunicación interna entre Workers y Master |
| **Prometheus**            | 9090 | Recolección de métricas y alertas |
| **Grafana**               | 3000 | Visualización de métricas y alertas |
| **Alertmanager**          | 9093 | Agrupamiento y gestión de alertas |
| **Node Exporter**         | 9100 | Métricas del sistema host |

## 1. Estructura del proyecto en Docker
---
Organizaremos el proyecto en carpetas y archivos Docker Compose. 
>name es el nombre del alumnado.
**Estructura sugerida:**
![arquitectura](/web/img/sup04-arq.png)


## 2. Desplegar clúster Spark (1 master, 3 workers) con Docker
---
Vamos a crear un archivo `docker-compose.spark.yml` que levante 1 nodo master Spark y 3 nodos worker Spark. En caso de que haya que hacer cambios futuros a dicho archivo las captural del mismo y la explicación irán en este apartado con justificación

## 3. Añadir Prometheus para recolectar métricas del clúster (3 archivos)
---
En este apartado deberás preparar el sistema de monitorización del clúster utilizando Prometheus y Grafana. Para ello, dentro de la carpeta `monitoring`, tendrás que crear y configurar tres archivos necesarios para el despliegue.

En primer lugar, crea el archivo `prometheus.yaml`, donde definirás la configuración de Prometheus, incluyendo los targets que se van a monitorizar (por ejemplo, el propio clúster y el servicio de Node Exporter).

A continuación, crea el archivo `grafana.ini`, que contendrá la configuración básica de Grafana, como parámetros de acceso, puertos o ajustes iniciales.

Por último, crea el archivo `docker-compose.monitoring.yaml`, que será el encargado de levantar los contenedores necesarios para el sistema de monitorización. Este archivo deberá incluir tres servicios: un contenedor para Prometheus, otro para Grafana y otro para Node Exporter.

Una vez definidos los tres archivos, deberás verificar que el despliegue se realiza correctamente y que tanto Prometheus pueden acceder a las métricas del clúster.

## 4. Configurar Grafana y conectar con Prometheus
---
En este apartado deberás integrar Grafana con Prometheus para la visualización de métricas del clúster.

Como resultado final, deberás disponer de un dashboard en Grafana denominado **Spark Cluster Monitoring**, correctamente conectado a Prometheus y mostrando información en tiempo real.

El dashboard deberá estar estructurado en dos filas claramente diferenciadas. La primera fila estará dedicada al **nodo máster** del clúster e incluirá 5 paneles de monitorización. Entre las métricas representadas deberán aparecer, obligatoriamente, el uso de CPU y el uso de memoria, pudiendo completar el resto con otras métricas relevantes del sistema.

La segunda fila estará dedicada a los **nodos worker**. En esta sección también deberás incluir 5 paneles de monitorización basados en métricas obtenidas desde Prometheus. La selección de métricas queda a tu criterio, siempre que permita analizar el comportamiento y estado de los workers.

Se valorará que el dashboard sea claro, coherente y útil para la monitorización del clúster, así como que todas las visualizaciones muestren datos correctamente.

## 5. Reinicio del sistema de monitorización, análisis de incidencias
---
En este apartado se procederá al **reinicio** completo del sistema de monitorización previamente desplegado mediante contenedores, utilizando los mecanismos trabajados en clase para la parada y posterior arranque del entorno. Una vez restaurado el sistema, el alumnado deberá acceder nuevamente a la herramienta de visualización y comprobar su estado, prestando especial atención a la información generada en sesiones anteriores. 

A partir de esta observación, se espera que identifiquen posibles cambios en el comportamiento del sistema, analicen las causas que han podido originar esta situación y proponfgan e implementen una solución técnica que resuelva la incidencia detectada y comprobar su eficacia mediante un nuevo reinicio del sistema, documentando todo el proceso seguido, desde la identificación del problema hasta la validación de la solución adoptada.

## 6.  Ejecución del job de Spark SQL
---
Descarga el dataset de **Netflix desde Kaggle** y colócalo en la carpeta de Spark. Una vez disponible, ejecuta el job (job.py que estara en la carpeta Spark) desde el nodo master y anota los resultados que aparecen en la terminal para responder las siguientes preguntas:
1. ¿Cuántos títulos hay de tipo Movie y cuántos de TV Show?
2. ¿Qué país tiene más producciones en Netflix?
3. ¿Cuál es el año con más lanzamientos?
4. ¿Qué director tiene más títulos en el catálogo?
5. ¿Cuál es la categoría más frecuente?

## 7. Observación de métricas en Grafana
---
Mientras el job del apartado anterior está en ejecución, abre Grafana en http://localhost:3000 y observa cómo cambian los paneles del dashboard Spark Cluster Monitoring. Una vez finalizado el job responde las siguientes preguntas:

1. ¿Qué cambio observaste en el uso de CPU durante la ejecución del job?
2. ¿Cuánta memoria llegó a consumir el cluster en el momento de mayor carga?
3. ¿Los tres workers participaron en el procesamiento o solo algunos?

## 8. Alerta de uso de CPU
Configura una alerta en Prometheus que se dispare cuando el uso de CPU del nodo supere el 60% durante más de un 10s. Para ello deberás modificar los archivos ``rules.yml``.
Para comprobar su funcionamiento ejecuta una prueba de estrés desde el nodo master que genere carga suficiente para superar el umbral configurado. Observa cómo la alerta pasa por los estados PENDING y FIRING en http://localhost:9090/alerts y comprueba que finalmente aparece en la interfaz de Alertmanager en http://localhost:9093.

## 9. Alerta de worker caído con notificación a Telegram
Configura una alerta que detecte cuando uno de los workers del cluster se cae y envíe una notificación automática a Telegram. Para ello deberás modificar los archivos ``rules.yml`` y ``alertmanager.yml``.
Para comprobar su funcionamiento para manualmente uno de los workers con ``docker stop spark-worker-2`` y verifica que la alerta se dispara en Prometheus, aparece en Alertmanager y el mensaje llega correctamente a Telegram.

## 10. Visualización del cluster con Ganglia
Añade ``docker-compose.ganglia.yml`` a tu infraestructura de monitorización e intégralo con el cluster de Spark. Ganglia es una herramienta de monitorización distribuida especialmente diseñada para clusters, que permite visualizar métricas de rendimiento de forma agregada. Una vez en funcionamiento, compara la información que ofrece Ganglia con la que ya tienes en Grafana y reflexiona sobre las diferencias entre ambas herramientas: qué visualiza mejor cada una, qué métricas están disponibles en una y no en la otra, y en qué escenarios usarías cada una de ellas.

## Entrega

La entrega de esta actividad constará de dos partes:

**1. Archivos del proyecto** — Se deberán entregar los siguientes archivos:
- jobs.py
- docker-compose.saprk.yml
- prometheus.yml

**2. Informe técnico** — Se redactará un informe siguiendo las pautas generales del curso. El informe debe incluir: portada con nombre, fecha y título de la actividad; índice numerado; desarrollo de cada uno de los 10 apartados con explicación de los pasos seguidos, comandos utilizados y capturas de pantalla como evidencia; apartado de conclusiones donde se reflexione sobre el funcionamiento del pipeline y las dificultades encontradas; y bibliografía o referencias consultadas.

El informe se entregará en el formato indicado por el profesor a través de la plataforma del curso antes de la fecha límite establecida.