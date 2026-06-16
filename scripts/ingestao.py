import sqlite3
import time
import random
import os

os.makedirs('../data', exist_ok=True)

conn = sqlite3.connect('../data/farmtech.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS SENSORES (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    TIMESTAMP DATETIME DEFAULT CURRENT_TIMESTAMP,
    UMIDADE_SOLO REAL,
    PH REAL,
    NITROGENIO REAL,
    FOSFORO REAL,
    POTASSIO REAL,
    VAI_CHOVER INTEGER,
    BOMBA_LIGADA REAL
)
''')
conn.commit()

print("Iniciando ingestão de dados simulados (Pressione Ctrl+C para parar)...")

try:
    while True:
        umidade = round(random.uniform(20.0, 80.0), 2)
        ph = round(random.uniform(5.0, 7.5), 2)
        n = round(random.uniform(10, 50), 2)
        p = round(random.uniform(10, 50), 2)
        k = round(random.uniform(10, 50), 2)
        vai_chover = random.choice([0, 1])
        
        tempo_bomba = 0
        if umidade < 40 and vai_chover == 0:
            tempo_bomba = round((40 - umidade) * 1.5, 2)

        cursor.execute('''
        INSERT INTO SENSORES (UMIDADE_SOLO, PH, NITROGENIO, FOSFORO, POTASSIO, VAI_CHOVER, BOMBA_LIGADA)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (umidade, ph, n, p, k, vai_chover, tempo_bomba))
        
        conn.commit()
        print(f"[{time.strftime('%H:%M:%S')}] Dados inseridos: Umidade={umidade}%, Bomba={tempo_bomba} min")
        
        time.sleep(3) 

except KeyboardInterrupt:
    print("\nIngestão finalizada.")
finally:
    conn.close()