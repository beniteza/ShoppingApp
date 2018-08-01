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
        pass