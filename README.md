# Data Formats with Python (CSV · JSON · XML · YAML)

Reading, analyzing and converting data across the four most common file formats, using the
Python standard library and pandas.

*Lectura, análisis y conversión de datos entre CSV, JSON, XML y YAML con Python y pandas.*

## What's inside

### 1. Academic system — `main.py`

Interactive console app that combines three formats:

| Option | Format | What it does |
|---|---|---|
| Show / search students | CSV | Reads `estudiantes.csv` with `csv.DictReader`, searches by code |
| Grade statistics | CSV | Average, highest and lowest grade, passed vs. failed |
| Student details / search by program | XML | Parses `estudiantes.xml` with `xml.etree.ElementTree` |
| System configuration | YAML | Loads nested settings from `configuracion.yaml` with `yaml.safe_load` |

Sample output (option 3):

```
---------ESTADISTICAS-------
Cantidad de estudiantes:  10
Promedio:  3.59
Mayor Nota:  Sofia 4.9
Menor Nota:  Pedro 1.8
Aprobados:  7
Reprobados:  3
```

### 2. CSV → JSON converters

Same conversion done two ways, to compare approaches:

| Script | Approach | Output |
|---|---|---|
| `conversor.py` | Standard library (`csv` + `json`), casting numeric fields manually | `inventario_convert.json` |
| `convertidor_pandas.py` | `pandas.read_csv()` + `to_dict(orient="records")` | `inventario_pandas.json` |

### 3. Format readers

Minimal examples reading the product inventory in each format:
`ejemplo_csv.py`, `ejemplo_xml.py`, `ejemplo_yaml.py`.

## How to run

```bash
pip install -r requirements.txt

python main.py                 # academic system
python conversor.py            # CSV -> JSON (standard library)
python convertidor_pandas.py   # CSV -> JSON (pandas)
```

Run the scripts from inside this folder so the relative data paths resolve.

## Author

**Juan Sebastián Perlaza** — Data Analyst | SQL · Python · Power BI
[LinkedIn](https://www.linkedin.com/in/sebastianperlaza) ·
[GitHub](https://github.com/SebasPerlaza895)
