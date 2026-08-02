import os
import psycopg2

def insert_row(cursor, data_referencia, value):
    try:
        cursor.execute("""
            INSERT INTO valores_scraping_lme (data_referencia, valor)
            VALUES (%s, %s)
            ON CONFLICT (data_referencia) DO UPDATE
            SET valor = EXCLUDED.valor;
        """, (data_referencia, value))

    except psycopg2.Error as e:
        print("Erro ao inserir no banco:", e)