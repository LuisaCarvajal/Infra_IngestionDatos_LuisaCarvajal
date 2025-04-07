bigdata_actividad1/
│
├── flujo_etl.md               # Documentación del flujo de datos
├── modelo_datos.md            # Documentación del modelo de datos
│
├── src/
│   └── BigData/
│       ├── static/
│       │   ├── auditoria/
│       │   │   ├── cleaning_report.txt        # Reporte de limpieza
│       │   │   ├── enriched_report.txt        # Reporte de enriquecimiento
│       │   │   └── ingestion.txt              # Reporte de ingestión
│       │   │
│       │   ├── db/
│       │   │   └── ingestion.db               # Base de datos SQLite final
│       │   │
│       │   └── xlsx/
│       │       ├── cleaned_data.csv           # Datos limpiados
│       │       ├── enriched_data.csv          # Datos enriquecidos
│       │       └── ingestion.csv              # Datos originales (raw)
│       │
│       ├── audit_script.py                   # Script para generar auditoría
│       ├── cleaning.py                       # Script de limpieza de datos
│       ├── data_sucio.py                     # Script auxiliar con datos sucios
│       ├── enrichment.py                     # Script de enriquecimiento
│       └── ingestion.py                      # Script para extraer desde la API y guardar en CSV