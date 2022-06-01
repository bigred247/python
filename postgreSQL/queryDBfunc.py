import psycopg2
def db_login():
    conn = None
    try: 
        conn = psycopg2.connect("host=127.0.0.1 dbname=screwfixdb user=postgres password=magic")
        cur = conn.cursor()
        cur.execute("SELECT * FROM persons")
        print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
db_login()