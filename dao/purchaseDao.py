from config.dbconfig import pg_config
import psycopg2

class PurchaseDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getPurchaseById(self, id):
        cursor = self.conn.cursor()
        query = "select * from purchase where account_id = %s;"
        cursor.execute(query, (id,))
        result = []
        for row in cursor:
            result.append(row)
        if result == []:
            return None
        return result

    def getSinglePurchaseById(self, account_id, purchase_id):
        cursor = self.conn.cursor()
        query = "select * from purchase where account_id = %s and purchase_id = %s;"
        cursor.execute(query, (account_id, purchase_id))
        result = cursor.fetchone()
        if result == []:
            return None
        return result

    def insertPurchase(self, form):
        pass

    def getItemPurchaseById(self, id):
        cursor = self.conn.cursor()
        query = "select * from item " \
                "where item_id = " \
                "( select item_id from item_purchase where purchase_id = %s )"
        cursor.execute(query, (id,))
        result = []
        for row in cursor:
            result.append(row)
        if result == []:
            return None
        return result

    def insertItemPurchase(self, form):
        pass