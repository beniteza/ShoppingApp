from config.dbconfig import pg_config
import psycopg2

class ItemDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def insertItem(self, item_name, description, price):
        cursor = self.conn.cursor()
        query = "insert into item(item_name, description, price) VALUES (%s, %s, %s) returning item_id"
        cursor.execute(query, (item_name, description, price))
        id = cursor.fetchone()[0]
        self.conn.commit()
        return id