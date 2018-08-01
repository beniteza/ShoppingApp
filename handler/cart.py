from flask import jsonify
from dao.cartDao import CartDAO
from handler.item import ItemHandler

class CartHandler:
    def getCartById(self, id):
        dao = CartDAO()
        item_handler = ItemHandler()
        result = dao.getCartById(id) #account id
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(item_handler.mapToItemDict(r)) #Should be a loop
            return jsonify(Cart=mapped_result)

    def insertItemCart(self, form):
        if len(form) != 3:
            return jsonify(Error="Malformed post request"), 400
        else:
            item_id = form['item_id']
            quantity = form['quatity']
            account_id = form['account_id']
            if item_id and quantity and account_id:
                dao = CartDAO()
                id = dao.insertItemCart(item_id, quantity, account_id)
                result = self.mapToCartItemDict([id, item_id, quantity, account_id])
                return jsonify(Cart_Item=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def mapToCartItemDict(self, row):
        result = {}
        result["cart_item_id"] = row[0]
        result["item_id"] = row[1]
        result["quantity"] = row[2]
        result["account_id"] = row[3]
        return result