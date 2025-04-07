
# Modelo de Datos - ETL Frutas

---

## Tabla: `frutas`

| Campo         | Tipo     | Descripción                                     |
|---------------|----------|-------------------------------------------------|
| id            | INTEGER  | Identificador único de la fruta (PK)            |
| nombre        | TEXT     | Nombre común de la fruta                        |
| familia       | TEXT     | Familia botánica                                |
| orden         | TEXT     | Orden taxonómico                                |
| carbohidratos | REAL     | Carbohidratos por 100g                          |
| proteinas     | REAL     | Proteínas por 100g                              |
| grasas        | REAL     | Grasas por 100g                                 |
| calorias      | REAL     | Calorías por 100g                               |

---

## Relaciones

Este modelo solo incluye una tabla por simplicidad, pero puede escalarse fácilmente si se agregan otras fuentes o información adicional.

---

## Justificación del Diseño

- Se extrajo solo la información relevante para análisis nutricional y clasificación de taxonimia.
- Usar SQLite permite una solución liviana y portátil.
- El modelo es limpio, legible y optimizado para consultas básicas.
