# LME Pipeline - Coleta e Armazenamento de Dados de Commodities

Pipeline de dados desenvolvido para realizar a extração automática dos valores diários do **alumínio na London Metal Exchange (LME)**, tratamento das informações e armazenamento em banco de dados PostgreSQL.

O projeto foi estruturado seguindo uma arquitetura simples de **ETL (Extract, Transform, Load)**, com execução automatizada utilizando **GitHub Actions**.

---

## Arquitetura

```
                 GitHub Actions
                       |
                       |
                       v
              +----------------+
              |  Python Scraper |
              +----------------+
                       |
                       |
              Extração dos dados
                       |
                       v
             Tratamento das datas
                       |
                       v
              Inserção no banco
                       |
                       v
              PostgreSQL / Supabase
```

---

## Funcionalidades

* Extração automática dos valores históricos da LME.
* Tratamento e padronização das datas.
* Conversão dos valores coletados para formato numérico.
* Persistência dos dados em banco PostgreSQL.
* Controle de duplicidade utilizando chave única.
* Atualização automática de registros existentes.
* Execução diária automatizada via GitHub Actions.
* Possibilidade de execução manual informando uma data específica.

---

## Tecnologias utilizadas

### Linguagem

* Python 3.12+

### Bibliotecas

* `requests` - Requisições HTTP para coleta dos dados.
* `BeautifulSoup4` - Parsing e extração das informações HTML.
* `psycopg2` - Comunicação com banco PostgreSQL.

### Banco de dados

* PostgreSQL
* Supabase

### Automação

* GitHub Actions

---

## Estrutura do projeto

```
lme-pipeline
│
├── database
│   └── schema.sql
│
├── src
│   ├── scraper.py
│   ├── Insert.py
│   ├── Db_connection.py
│   ├── date_treatment.py
│   └── valores_scraping_lme_rows.csv
│
├── requirements.txt
└── README.md
```

---

## Fluxo do Pipeline

### 1. Extract

O scraper realiza uma requisição HTTP para a página contendo os dados históricos da LME.

Exemplo:

```
https://shockmetais.com.br/lme/MM-AAAA
```

Os dados da tabela são coletados utilizando BeautifulSoup.

---

### 2. Transform

Durante o processamento são realizados:

* Limpeza dos valores coletados.
* Conversão de string para número.
* Padronização das datas.
* Remoção de registros inválidos.

Exemplo:

```
"3,159.5"
        |
        v
3159.5
```

---

### 3. Load

Os dados são armazenados na tabela:

```sql
valores_scraping_lme
```

Estrutura:

| Campo           | Tipo    |
| --------------- | ------- |
| data_referencia | DATE    |
| valor           | NUMERIC |

A inserção utiliza:

```sql
ON CONFLICT (data_referencia)
DO UPDATE
```

garantindo que registros existentes sejam atualizados sem gerar duplicidade.

---

## Execução local

### Instalar dependências

```bash
pip install -r requirements.txt
```

---

### Executar normalmente

O pipeline utiliza automaticamente o dia anterior como referência:

```bash
python src/scraper.py
```

---

### Executar para uma data específica

Também é possível informar uma data manualmente:

```bash
python src/scraper.py 31-07-2026
```

Formato esperado:

```
DD-MM-YYYY
```

---

## Execução automática

O pipeline é executado diariamente utilizando GitHub Actions.

Workflow:

```
.github/workflows/lme.yml
```

Configuração:

* Execução automática diária.
* Execução manual via workflow dispatch.
* Possibilidade de informar uma data de referência.

---

## Banco de Dados

A conexão com o banco utiliza variáveis de ambiente:

```
DB_HOST
DB_USER
DB_PASSWORD
DB_NAME
DB_PORT
```

Essas informações são armazenadas utilizando GitHub Secrets/Variables.

---

## Melhorias futuras

Possíveis evoluções:

* Implementação de logs estruturados.
* Containerização utilizando Docker.
* Criação de API para consulta dos dados.
* Dashboard de acompanhamento dos preços.
* Orquestração utilizando Apache Airflow.
* Monitoramento de falhas do pipeline.

---

## Autor

**Guilherme Rodrigues**

Projeto desenvolvido com foco em práticas de Engenharia de Dados, automação de pipelines e integração entre coleta, processamento e armazenamento de dados.
