import psycopg2
from worker.worker import process_chaos

conn = psycopg2.connect("dbname=chaos user=postgres password=secret")
cur = conn.cursor()

def run_loop():
    cur.execute("SELECT id, payload FROM raw_chaos WHERE processed IS FALSE")
    for id, payload in cur.fetchall():
        process_chaos.delay(payload)
        cur.execute("UPDATE raw_chaos SET processed = TRUE WHERE id = %s", (id,))
        conn.commit()
