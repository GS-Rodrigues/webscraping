import datetime

meses = {
    "Jan": 1, "Fev": 2, "Mar": 3, "Abr": 4, "Mai": 5, "Jun": 6,
    "Jul": 7, "Ago": 8, "Set": 9, "Out": 10, "Nov": 11, "Dez": 12
}

def parse_data_br(data_str , year):
    dia, mes_abrev = data_str.split('/')
    dia = int(dia)
    mes = meses[mes_abrev]
    ano = year
    return datetime.date(ano, mes, dia)
