import psycopg2



hostname = 'localhost'
port_id ='5432'
username = 'postgres'
database = 'Practice'
pwd = '3045'

conn = None
cur = None

Archive = open('PruebaRElaciones','r')

try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
        )

    cur = conn.cursor() 

    insert = 'INSERT INTO relaciones11 (id_lema1,id_lema2,weight) VALUES (%s,%s,%s)'

    for line in Archive:
        word = line.split()

        
        cur.execute("SELECT lemas.id_lema FROM lemas WHERE lema ='" +word[0]+"' ")
        lema = cur.fetchone()
        lema1 = lema[0]
        cur.execute("SELECT lemas.id_lema FROM lemas WHERE lema ='" +word[1]+"' ")
        lemas = cur.fetchone()
        lema2 = lemas[0]

        insert_values = (int(lema1),int(lema2),int(word[2]))
        cur.execute(insert, insert_values)

    #cur.execute('SELECT * FROM prueba WHERE (id_lema = 23)')
    #print(cur.fetchall())
    
    conn.commit()
except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
    Archive.close()