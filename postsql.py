import psycopg2

con = psycopg2.connect(database="suicide", user="postgres", password="Password", host="suicide-db.cfnbykir9i4m.us-east-1.rds.amazonaws.com", port="5432")

cur = con.cursor()
cur.execute("SELECT country from public.suicide")
rows = cur.fetchall()

print("Rows: ", rows)

print("Database opened successfully")