import mysql.connector
from prefect import task


@task(name='Cargar y limpieza de ofertas en bd')
def task_load_offers_baseline(offers):
    try:
        conn = mysql.connector.connect(
            user='root',
            password='root',
            host='localhost',
            database='db_codigo'
        )
        cursor = conn.cursor()

        query_drop = "drop table if exists tbl_oferta"
        cursor.execute(query_drop)
        conn.commit()

        query_table = """
        create table if not exists tbl_oferta(
        id INT AUTO_INCREMENT PRIMARY KEY,
        codigo VARCHAR(255),
        titulo VARCHAR(255),
        ubicacion VARCHAR(255),
        empresa VARCHAR(255),
        fecha DATE,
        url TEXT,
        skill VARCHAR(255),
        fecha_creacion DATETIME default CURRENT_TIMESTAMP
        )
        """
        cursor.execute(query_table)
        conn.commit()

        query_insert = """
        insert into tbl_oferta(codigo,titulo,ubicacion,empresa,fecha,url,skill)
        values(%s,%s,%s,%s,%s,%s,%s)
        """

        for offer in offers:
            cursor.execute(query_insert,offer)

        conn.commit()
        cursor.close()
        conn.close()
        print("datos guardados en bd...")
    except mysql.connector.Error as err:
        print(err)

@task(name='Carga nuevas ofertas')
def task_load_offers_update(offers):
    try:
        conn = mysql.connector.connect(
            user='root',
            password='root',
            host='localhost',
            database='db_codigo'
        )
        cursor = conn.cursor()

        query_exists = "select id from tbl_oferta where codigo = %s"
        query_insert = """
            insert into tbl_oferta(codigo,titulo,ubicacion,empresa,fecha,url,skill)
            values(%s,%s,%s,%s,%s,%s,%s)
            """

        for offer in offers:
            cursor.execute(query_exists,(offer[0],))
            row = cursor.fetchone()
            if row is None:
                cursor.execute(query_insert,offer)
                conn.commit()
        
        cursor.close()
        conn.close()
        print("datos guardados en bd...")
    except mysql.connector.Error as err:
        print(err)