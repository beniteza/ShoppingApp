from config.dbconfig import pg_config
import psycopg2

class SellerDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getItemSellerById(self, id):
        cursor = self.conn.cursor()
        query = "select seller.seller_id, seller.account_id " \
                "from seller, supplies, item " \
                "where seller.seller_id = supplies.seller_id " \
                "and supplies.item_id = item.item_id " \
                "and item.item_id = %s;"
        cursor.execute(query, (id,))
        result = []
        for row in cursor:
            result.append(row)
        if result == []:
            return None
        return result