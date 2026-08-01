CREATE TABLE IF NOT EXISTS valores_scraping (
    id BIGSERIAL PRIMARY KEY,
    data_referencia DATE NOT NULL,
    valor NUMERIC(18, 4) NOT NULL,
    data_coleta TIMESTAMPTZ DEFAULT NOW()
);