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