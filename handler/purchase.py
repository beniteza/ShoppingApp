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
        # result["purchase_date"] = row[2]
        result["purchase_date"] = 'INSERT_TIME_HERE'
        return result


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

    def insertPurchase(self, form):
        if len(form) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            account_id = form['account_id']
            # purchase_date = form['purchase_date']
            purchase_date = 'now()'
            if account_id and purchase_date:
                dao = PurchaseDAO()
                id = dao.insertPurchase(account_id, purchase_date)
                result = self.mapToPurchaseDict([id, account_id, purchase_date])
                return jsonify(Purchase=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertItemPurchase(self, form):
        if len(form) != 5:
            return jsonify(Error="Malformed post request"), 400
        else:
            purchase_id = form['purchase_id']
            item_id = form['item_id']
            quantity = form['quantity']
            seller_id = form['seller_id']
            price = form['price']
            if purchase_id and item_id and quantity and seller_id and price:
                dao = PurchaseDAO()
                id = dao.insertItemPurchase(purchase_id, item_id, quantity, seller_id, price)
                result = self.mapToPurchaseDict([id, purchase_id, item_id, quantity, seller_id, price])
                return jsonify(Item_Purchase=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def mapToItemPurchaseDict(self, row):
        pass