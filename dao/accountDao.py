from config.dbconfig import pg_config
import psycopg2
class AccountDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllAccount(self):
        cursor = self.conn.cursor()
        query = "select * from account;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        if result == []:
            return None
        return result

    def getAccountById(self, id):
        cursor = self.conn.cursor()
        query = "select * from account where account_id = %s;"
        cursor.execute(query, (id,)) #the id needs a ',' next to it to be able to support indexing
        result = cursor.fetchone()
        if result == []:
            return None
        return result

    def insertAccount(self, first_name, last_name, email, username, password):
        cursor = self.conn.cursor()
        query = "insert into account(first_name, last_name, email, username, password) " \
                "values (%s, %s, %s, %s, %s) returning account_id;"
        cursor.execute(query, (first_name, last_name, email, username, password))
        id = cursor.fetchone()[0]
        self.conn.commit()
        return id