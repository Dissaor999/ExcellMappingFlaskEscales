import base64
import io
import json
import re
import numpy as np
import pandas as pd

def jsontoNodos(json):
    df = pd.DataFrame(json)
    nodes = pd.unique(df.values.ravel())
    nodes_df = pd.DataFrame({'id': range(1, len(nodes) + 1), 'Label': nodes})
    print(nodes_df)

def process(excel_filename):
    excel = "./app/files/" + excel_filename
    file = pd.read_excel(excel, engine="openpyxl", dtype=str)
    excel_json = json.loads(file.to_json(orient="records"))
    excelNodos = jsontoNodos(excel_json)
    