import os
import pandas as pd
from datetime import datetime

CSV_FILE = "valores_scraping_lme_rows.csv"


def insert_row(data_referencia, value):
    # cria DataFrame da nova linha
    new_row = pd.DataFrame([{
        "data_referencia": data_referencia,
        "valor": value
    }])

    # se arquivo já existir
    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)

        # remove linha existente da mesma data
        df = df[df["data_referencia"] != data_referencia]

        # adiciona nova linha
        df = pd.concat([df, new_row], ignore_index=True)

    else:
        # cria novo dataframe
        df = new_row

    # ordena por data
    df["data_referencia"] = pd.to_datetime(df["data_referencia"])
    df = df.sort_values("data_referencia")

    # salva CSV
    df.to_csv(CSV_FILE, index=False)

    print(f"Linha salva com sucesso: {data_referencia} -> {value}")
