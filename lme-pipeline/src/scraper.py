import requests
from Insert import insert_row
from datetime import datetime, timedelta
from Db_connection import get_connection
import date_treatment
from bs4 import BeautifulSoup

conn = get_connection();
cursor = conn.cursor();

try:
    yesterday = (datetime.now() - timedelta(days=1)).date()
    data_str = yesterday.strftime("%m-%Y")

    url = f"https://shockmetais.com.br/lme/{data_str}";
    response = requests.get(url, timeout=10);
    response.raise_for_status()
    
    html_content = response.content;
    
    soup = BeautifulSoup(html_content, 'html.parser');
    
    tables = soup.find_all(
        name='table',
        attrs= {'class' : 'table table-hover table-sm table-striped shadow'}
    );

    if not tables:
        raise RuntimeError("Tabela LME não encontrada na página")
    else:
        table = tables[0]

    
    for row in table.find_all('tr')[1:-1]:
        colms = row.find_all('td');

        if not colms:
            continue;
        else:
            month_year = colms[0].text.strip();
            if "feriado" in month_year.lower() or "média" in month_year.lower():
                continue;
            
            raw_value = colms[3].get_text(strip=True)

            try:
                aluminium = float(raw_value.replace(" ", "").replace("\n", "").replace(",", ""));
                date_clean = date_treatment.parse_data_br(month_year, yesterday.year);
                if date_clean.month == yesterday.month:
                    aluminium = float(aluminium);
                    insert_row(cursor, date_clean, aluminium);
            except ValueError:
                continue
    conn.commit();

except Exception as e:
    conn.rollback()
    print("Erro no scraping LME:", e)

finally:
    cursor.close()
    conn.close()
