from flask import jsonify
from dao.notificationDao import NotificationDAO

class NotificationHandler:
    def getNotificationById(self, id):
        dao = NotificationDAO()
        result = dao.getNotificationById(id)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToNotificationDict(r))
        return jsonify(Notifications=mapped_result)

    def getSingleNotificationById(self, account_id, notification_id):
        dao = NotificationDAO()
        result = dao.getSingleNotificationById(account_id, notification_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToNotificationDict(result)
            return jsonify(Notification=mapped)

    def mapToNotificationDict(self, row):
        result = {}
        result["notification_id"] = row[0]
        result["subject"] = row[1]
        result["message"] = row[2]
        result["sender_id"] = row[3]
        return result

    def insertNotification(self, form):
        if len(form) != 3:
            return jsonify(Error="Malformed post request"), 400
        else:
            subject = form['subject']
            message = form['message']
            sender_id = form['sender_id']
            if subject and message and sender_id:
                dao = NotificationDAO()
                id = dao.insertNotification(subject, message, sender_id)
                result = self.mapToNotificationDict([id, subject, message, sender_id])
                return jsonify(Notification=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertSentNotification(self, form):
        if len(form) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            notification_id = form['notification_id']
            receiver_id = form['receiver_id']
            if notification_id and receiver_id:
                dao = NotificationDAO()
                id = dao.insertSentNotification(notification_id, receiver_id)
                result = self.mapToSentNotificationDict([id, notification_id, receiver_id])
                return jsonify(Sent_Notification=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def mapToSentNotificationDict(self, row):
        result = {}
        result["sent_notification_id"] = row[0]
        result["notification_id"] = row[1]
        result["receiver_id"] = row[2]
        return result