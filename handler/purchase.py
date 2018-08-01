from flask import jsonify
from dao.purchaseDao import PurchaseDAO
from handler.item import ItemHandler

class PurchaseHandler:
    def getPurchaseById(self, id):
        dao = PurchaseDAO()
        result = dao.getPurchaseById(id) #account id
        mapped_result = []
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        for r in result:
            mapped_result.append(self.mapToPurchaseDict(r))
        return jsonify(Notifications=mapped_result)

    def getSinglePurchaseById(self, account_id, purchase_id):
        dao = PurchaseDAO()
        result = dao.getSinglePurchaseById(account_id, purchase_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToPurchaseDict(result)
            return jsonify(Notification=mapped)

    def mapToPurchaseDict(self, row):
        result = {}
        result["purchase_id"] = row[0]
        result["account_id"] = row[1]
        # result["message"] = row[2]
        result["message"] = 'INSERT_TIME_HERE'
        return result

    def insertPurchase(self, form):
        pass

    def getItemPurchaseById(self, id):
        dao = PurchaseDAO()
        item_handler = ItemHandler()
        result = dao.getItemPurchaseById(id) #purchase id
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(item_handler.mapToItemDict(r))
            return jsonify(Items_Purchased=mapped_result)

    def insertItemPurchase(self, form):
        pass