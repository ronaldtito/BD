import psycopg2



hostname = 'localhost'
port_id ='5432'
username = 'postgres'
database = 'BDPartial2'
pwd = '3045'

conn = None
cur = None


try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
        )

    cur = conn.cursor() 

    matriz = []
    
    select_lemas  = 'SELECT lemas.id_lema, lemas.lema FROM lemas'
    cur.execute(select_lemas)
    lemas = cur.fetchall()

    #id_lema1
    for lema in lemas:
        word = str(lema[1])
        view = ("CREATE VIEW lemax"+word+" AS SELECT lemas2.id_lema2 as id_lema, lemas2.lema2 as lema , lemas.id_lema as id_lema2, lemas.lema as lema2 FROM lemas CROSS JOIN (SELECT lemas.id_lema as id_lema2, lemas.lema as lema2 FROM lemas WHERE lema =')"+word+"') as lemas2;")
        cur.execute(view)
         
        consulta =("SELECT lemax"+word+".id_lema2, lemax"+word+".lema2, CASE WHEN relation.weight IS NULL THEN 0 ELSE relation.weight END FROM lemax"+word+" LEFT JOIN (SELECT relaciones.id_lema1, relaciones.id_lema2 , relaciones.weight FROM lemax"+word+" INNER JOIN relaciones ON (lemax"+word+".id_lema2 = relaciones.id_lema2 AND lemax"+word+".id_lema = relaciones.id_lema1 )) as relation ON lemax"+word+".id_lema = relation.id_lema1 AND lemax"+word+".id_lema2 = relation.id_lema2")

        cur.execute(consulta)

        result = cur.fetchall()
        for line in result:
            print(line)
        
        cur.execute("DROP VIEW lemax"+word+";")

    
        conn.commit()
except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()