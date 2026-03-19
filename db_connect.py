from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT"),
    sslmode="require"
)

print("Connected successfully!")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id SERIAL PRIMARY KEY,
    amount DECIMAL NOT NULL,
    category VARCHAR(50) NOT NULL,
    date DATE NOT NULL
);
""")
conn.commit()
print("Table created successfully!")

cur.execute("""
INSERT INTO expenses (amount, category, date)
VALUES (25.50, 'Food', '2026-02-25');
""")
conn.commit()

cur.execute("SELECT * FROM expenses;")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()
