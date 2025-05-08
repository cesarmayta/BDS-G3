import psycopg2
from airflow.models import BaseOperator
from airflow.utils.context import Context

class LoadOffersOperator(BaseOperator):
    def __init__(self, offers_key, mode='baseline', **kwargs):
        super().__init__(**kwargs)
        self.offers_key = offers_key
        self.mode = mode  # 'baseline' o 'update'

    def execute(self, context: Context):
        ti = context['ti']
        offers = ti.xcom_pull(task_ids='extract', key=self.offers_key)
        
        
        if not offers:
            self.log.warning("No hay ofertas para cargar.")
            return
        
        print(offers)

        conn = psycopg2.connect(
            user='airflow',
            password='airflow',
            host='postgres',
            dbname='airflow'
        )
        cursor = conn.cursor()

        if self.mode == 'baseline':
            cursor.execute("DROP TABLE IF EXISTS tbl_oferta")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tbl_oferta (
                    id SERIAL PRIMARY KEY,
                    codigo VARCHAR(255),
                    titulo VARCHAR(255),
                    ubicacion VARCHAR(255),
                    empresa VARCHAR(255),
                    fecha DATE,
                    url TEXT,
                    skill VARCHAR(255),
                    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()

            insert_query = """
                INSERT INTO tbl_oferta (codigo, titulo, ubicacion, empresa, fecha, url, skill)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            for offer in offers:
                cursor.execute(insert_query, (
                    offer['codigo'],
                    offer['titulo'],
                    offer['ubicacion'],
                    offer['empresa'],
                    offer['fecha'],
                    offer['url'],
                    offer['skill']
                ))

        elif self.mode == 'update':
            exists_query = "SELECT id FROM tbl_oferta WHERE codigo = %s"
            insert_query = """
                INSERT INTO tbl_oferta (codigo, titulo, ubicacion, empresa, fecha, url, skill)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            for offer in offers:
                cursor.execute(exists_query, (offer['codigo'],))
                if cursor.fetchone() is None:
                    cursor.execute(insert_query, (
                        offer['codigo'],
                        offer['titulo'],
                        offer['ubicacion'],
                        offer['empresa'],
                        offer['fecha'],
                        offer['url'],
                        offer['skill']
                    ))

        conn.commit()
        cursor.close()
        conn.close()
        self.log.info("Ofertas cargadas exitosamente.")
