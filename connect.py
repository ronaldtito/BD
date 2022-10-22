import psycopg2



hostname = 'localhost'
port_id ='5432'
username = 'postgres'
database = 'BDPartial2'
pwd = '3045'

conn = None
cur = None

Archive = open('LemaFin','r')

try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
        )

    cur = conn.cursor() 

    insert = 'INSERT INTO lemas (id_lema,lema) VALUES (%s,%s)'

    id = 1
    for line in Archive:
        word = line.split()
        insert_values = (id,word[0])
        cur.execute(insert, insert_values)
        id +=1

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