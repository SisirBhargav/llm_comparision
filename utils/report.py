import pandas as pd
import os
from datetime import datetime

def generate_report(prompt:str,responses:dict):
    os.makedirs("data/comparision_reports",exist_ok=True)

    rows = []
    for model,output in responses.items():
        rows.append({
            "Model":model,
            "Prompt":prompt,
            "Response":output,
            "Timestamp":datetime.now().strftime("%y-%m-%d  %H:%M:%S")
        })
    df= pd.DataFrame(rows)
    df.to_csv("data/comparision_reports/reports.csv",index = False)


    return "data/comparision_reports/reports.csv"