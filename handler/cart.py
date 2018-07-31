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
                mapped_result.append(item_handler.mapToItemDict(result)) #Should be a loop
            return jsonify(Cart=mapped_result)
