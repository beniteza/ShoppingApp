from config.dbconfig import pg_config
import psycopg2

class ReviewDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getReviewById(self, id):
        cursor = self.conn.cursor()
        query = "select * from review where item_id = %s;"
        cursor.execute(query, (id,))
        result = []
        for row in cursor:
            result.append(row)
        if result == []:
            return None
        return result

    def getSingleReviewById(self, item_id, review_id):
        cursor = self.conn.cursor()
        query = "select * from review where item_id = %s and review_id = %s;"
        cursor.execute(query, (item_id, review_id))
        result = cursor.fetchone()
        if result == []:
            return None
        return result

    def insertReview(self, form):
        pass