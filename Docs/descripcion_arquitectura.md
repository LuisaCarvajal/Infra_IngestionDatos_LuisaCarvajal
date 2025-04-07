
#  Descripción General de la Arquitectura

## Visión Global

Este proyecto simula una arquitectura de Big Data en la nube a través de un flujo ETL (Extracción, Transformación y Carga) aplicado al dominio de datos nutricionales de frutas. Las fases clave del proceso son:

- **Ingesta:** Se consumen datos desde una API pública ([Fruityvice](https://www.fruityvice.com/api/fruit/all)) utilizando scripts Python. Esta información se transforma a formato tabular (CSV) y se almacena en una base de datos local SQLite.
- **Preprocesamiento:** Los datos ingeridos pasan por una fase de limpieza que corrige errores, elimina duplicados o datos faltantes, y normaliza campos necesarios.
- **Enriquecimiento:** Se agregan nuevas variables o se recalculan métricas derivadas (por ejemplo, categorías nutricionales) para potenciar el análisis posterior.

Todo este flujo se organiza en una estructura de carpetas simulando un entorno de producción en la nube, en donde los distintos módulos actúan como microservicios o componentes independientes.

##  Componentes Principales

| Componente                     | Descripción                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| **Base de Datos (SQLite)**    | Almacena los datos finales estructurados para su consulta y análisis.       |
| **Script de Ingesta**         | `ingestion.py` extrae datos de la API y los convierte en CSV y base SQLite.|
| **Script de Limpieza**        | `cleaning.py` realiza validación, limpieza y estandarización de datos.     |
| **Script de Enriquecimiento** | `enrichment.py` añade columnas calculadas y mejora los datos existentes.     |
| **Auditoría**                 | Los archivos `.txt` registran reportes de cada fase para trazabilidad.     |
| **Automatización (manual/scripting)** | Aunque no se usa Apache Airflow, la estructura modular permite su ejecución secuencial con scripts. |

## Estructura del Proyecto

Está organizada bajo una raíz llamada `BigData` que contiene:

- `src/BigData/static/db`: contiene la base de datos SQLite.
- `src/BigData/static/xlsx`: CSV de cada fase.
- `src/BigData/static/auditoria`: Reportes generados en cada etapa.
- Scripts `.py` independientes para cada fase del flujo.
