# Agrupamiento de estaciones del Metro de Madrid con K-Means

## Descripción
Proyecto académico de aprendizaje no supervisado. Se utiliza K-Means para agrupar 12 estaciones de referencia según tres variables numéricas.

**Importante:** las variables numéricas son simuladas y no representan estadísticas oficiales del Metro de Madrid. El objetivo es demostrar el procedimiento de aprendizaje no supervisado.

## Tecnologías
- Python
- pandas
- scikit-learn
- matplotlib

## Estructura
```text
metro-madrid-ia/
├── datos/estaciones_metro.csv
├── documentos/descripcion_datos.md
├── pruebas/pruebas.md
├── resultados/                 # se genera al ejecutar el programa
├── src/agrupamiento.py
├── requirements.txt
└── README.md
```

## Instalación
Se recomienda Python 3.10 o superior.

```bash
python -m venv .venv
```

Activar el entorno:

- Windows: `.venv\Scripts\activate`
- Linux/WSL: `source .venv/bin/activate`

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución
Desde la raíz del proyecto:

```bash
python src/agrupamiento.py
```

El programa imprime las estaciones y su grupo, calcula un resumen por grupo y crea:
- `resultados/agrupamiento.png`
- `resultados/estaciones_agrupadas.csv`

## Método
1. Cargar el CSV.
2. Seleccionar las tres variables numéricas.
3. Estandarizar las variables con `StandardScaler`.
4. Entrenar K-Means con tres grupos y `random_state=42`.
5. Mostrar y guardar las asignaciones y un gráfico.

## Interpretación y limitaciones
Los grupos son patrones dentro de esta pequeña muestra simulada. Sus identificadores son arbitrarios y no deben interpretarse como categorías oficiales. Para conclusiones sobre el sistema real se necesitan fuentes oficiales y datos verificables.

## Entregables
- Dataset: `datos/estaciones_metro.csv`
- Código fuente: `src/agrupamiento.py`
- Descripción de datos: `documentos/descripcion_datos.md`
- Pruebas: `pruebas/pruebas.md`
- Gráfico y resultados: carpeta `resultados/`

## Referencias
- Consorcio Regional de Transportes de Madrid, portal de datos abiertos: https://datos.crtm.es/
- Palma Méndez, J. T. (2008). *Inteligencia artificial: métodos, técnicas y aplicaciones*. McGraw-Hill España, capítulo 16 (técnicas de agrupamiento), referencia indicada en la consigna académica.

## Entrega
- Repositorio Git: [añadir URL]
- Video de exposición: [añadir URL]
- Estudiante: Diego Alejandro Ortiz
