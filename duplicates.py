import psycopg2



hostname = 'localhost'
port_id ='5432'
username = 'postgres'
database = 'Practice'
pwd = '3045'

conn = None
cur = None

Archive = open('DataNoDuplicada','a')

try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
        )

    cur = conn.cursor() 

    cur.execute('SELECT id_lema1, id_lema2, SUM(weight) FROM relaciones Group by (id_lema1,id_lema2) HAVING COUNT(*)>=0 ORDER by id_lema1 ASC')
    data = cur.fetchall()

    for register in data:
        word = (str(register[0])+'\t'+str(register[1])+'\t'+str(register[2])+'\n')
        Archive.write(word)
    conn.commit()
except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
    Archive.close()