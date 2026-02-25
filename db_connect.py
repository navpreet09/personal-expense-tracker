import psycopg2

conn = psycopg2.connect(
    host="bztoxujq8fekhvlwqwzr-postgresql.services.clever-cloud.com",
    database="bztoxujq8fekhvlwqwzr",
    user="uns7rtguhxxta5mtbgdh",
    password="0LBu74rl2Zr0Gl6eBbJVmOYUlSXkid",
    port="5432",
    sslmode="require"
)

print("Connected successfully!")

conn.close()