import psycopg2
from app.config import Config

def get_db_connection():
    """
        Returns a database connection
    """
    connection = psycopg2.connect(
        host=Config.DB_HOST,
        port=Config.DB_PORT,
        dbname=Config.DB_NAME,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD
    )
    return connection

def get_all_areas():
    """
        Returns all areas
    """
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM areas')
    results = cur.fetchall()
    cur.close()
    conn.close()
    return [{'id': r[0], 'name': r[1]} for r in results]
