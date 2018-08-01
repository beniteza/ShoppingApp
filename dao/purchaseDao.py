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

    def insertPurchase(self, account_id, purchase_date):
        cursor = self.conn.cursor()
        query = "insert into purchase(account_id, purchase_date) " \
                "VALUES (%s, %s) returning purchase_id;"
        cursor.execute(query, (account_id, purchase_date))
        id = cursor.fetchone()[0]
        self.conn.commit()
        return id

    def insertItemPurchase(self, purchase_id, item_id, quantity, seller_id, price):
        cursor = self.conn.cursor()
        query = "insert into item_purchase(purchase_id, item_id, quantity, seller_id, price) " \
                "VALUES (%s, %s, %s, %s, %s) returning item_purchase_id;"
        cursor.execute(query, (purchase_id, item_id, quantity, seller_id, price))
        id = cursor.fetchone()[0]
        self.conn.commit()
        return id

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
