from config.dbconfig import pg_config
import psycopg2

class WishlistDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getWishlistById(self, id):
        cursor = self.conn.cursor()
        query = "select * " \
                "from item " \
                "where item_id = " \
                "( select item_id from wishlist_item where account_id = %s )"
        cursor.execute(query, (id,))
        result = []
        for row in cursor:
            result.append(row)
        if result == []:
            return None
        return result

    def insertItemWishlist(self, item_id, account_id):
        cursor = self.conn.cursor()
        query = "insert into wishlist_item(item_id, account_id) " \
                "VALUES (%s, %s) returning wishlist_item_id;"
        cursor.execute(query, (item_id, account_id))
        id = cursor.fetchone()[0]
        self.conn.commit()
        return id