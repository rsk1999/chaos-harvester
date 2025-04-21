CREATE TABLE raw_chaos (
    id SERIAL PRIMARY KEY,
    source TEXT,
    payload JSONB,
    processed BOOLEAN DEFAULT FALSE,
    timestamp TIMESTAMP DEFAULT NOW()
);

CREATE TABLE extracted_value (
    id SERIAL PRIMARY KEY,
    raw_id INT REFERENCES raw_chaos(id),
    insights TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
