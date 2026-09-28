import pandas as pd
import json
df = pd.read_csv("inventario.csv")
json_data = df.to_dict(orient="records")
with open("inventario_pandas.json","w", encoding="utf-8") as archivo:
    json.dump(json_data,archivo,indent=4)
print("JSON GENERADO")
#pip install pandas