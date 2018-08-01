from config.dbconfig import pg_config
import psycopg2

class SellerDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getItemSupplierById(self, id):
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

    def insertSeller(self, id):
        cursor = self.conn.cursor()
        query = "insert into seller(account_id) values (%s) returning seller_id"
        cursor.execute(query, (id,))
        id = cursor.fetchone()[0]
        self.conn.commit()
        return id

    def insertSupplier(self, account_id, seller_id):
        cursor = self.conn.cursor()
        query = "insert into supplies(item_id, seller_id) VALUES (%s, %s) returning supplies_id"
        cursor.execute(query, (account_id, seller_id))
        id = cursor.fetchone()[0]
        self.conn.commit()
        return id