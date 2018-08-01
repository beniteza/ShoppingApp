from flask import jsonify
from dao.itemDao import ItemDAO

class ItemHandler:
    def mapToItemDict(self, row):
        result = {}
        result["item_id"] = row[0]
        result["item_name"] = row[1]
        result["description"] = row[2]
        result["price"] = row[3]
        return result

    def insertItem(self, form):
        if len(form) != 3:
            return jsonify(Error="Malformed post request"), 400
        else:
            item_name = form['item_name']
            description = form['description']
            price = form['price']
            if item_name and description and price:
                dao = ItemDAO()
                id = dao.insertItem(item_name, description, price)
                result = self.mapToItemDict([id, item_name, description, price])
                return jsonify(Item=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400