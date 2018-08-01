from config.dbconfig import pg_config
import psycopg2

class NotificationDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getNotificationById(self, id):
        cursor = self.conn.cursor()
        query = "select * " \
                "from notification " \
                "where notification_id = " \
                "( select notification_id from sent_notification where receiver_id = %s );"
        cursor.execute(query, (id,))
        result = []
        for row in cursor:
            result.append(row)
        if result == []:
            return None
        return result

    def getSingleNotificationById(self, account_id, notification_id):
        cursor = self.conn.cursor()
        query = "select * " \
                "from notification " \
                "where notification_id = " \
                "( select notification_id from sent_notification where receiver_id = %s ) " \
                "and notification_id = %s;"
        cursor.execute(query, (account_id, notification_id))
        result = cursor.fetchone()
        if result == []:
            return None
        return result

    def insertNotification(self, subject, message, sender_id):
        cursor = self.conn.cursor()
        query = "insert into notification(subject, message, sender_id) " \
                "VALUES (%s, %s, %s) returning notification_id;"
        cursor.execute(query, (subject, message, sender_id))
        id = cursor.fetchone()[0]
        self.conn.commit()
        return id

    def insertSentNotification(self, notification_id, receiver_id):
        cursor = self.conn.cursor()
        query = "insert into sent_notification(notification_id, receiver_id) " \
                "VALUES (%s, %s) returning sent_notification_id;"
        cursor.execute(query, (notification_id, receiver_id))
        id = cursor.fetchone()[0]
        self.conn.commit()
        return id