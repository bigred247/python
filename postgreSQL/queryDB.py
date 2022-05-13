import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect("host=127.0.0.1 dbname=screwfixdb user=postgres password=magic")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM persons")

# Retrieve query results
records = cur.fetchall()

for x in records:
    print(x)