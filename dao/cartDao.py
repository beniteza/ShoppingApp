from config.dbconfig import pg_config
import psycopg2

class CartDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getCartById(self, id):
        cursor = self.conn.cursor()
        query = "select * " \
                "from item " \
                "where item_id = " \
                "( select cart_item_id from cart_item where account_id = %s )"
        cursor.execute(query, (id,))
        result = []
        for row in cursor:
            result.append(row)
        if result == []:
            return None
        return result