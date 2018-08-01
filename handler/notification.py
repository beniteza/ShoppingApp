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
        pass