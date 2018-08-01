from flask import jsonify
from dao.wishlistDao import WishlistDAO
from handler.item import ItemHandler

class WishlistHandler:
    def getWishlistById(self, id):
        dao = WishlistDAO()
        item_handler = ItemHandler()
        result = dao.getWishlistById(id) #account id
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(item_handler.mapToItemDict(r)) #Should be a loop
            return jsonify(Wishlist=mapped_result)

    def insertItemWishlist(self, form):
        if len(form) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            item_id = form['item_id']
            account_id = form['account_id']
            if item_id and account_id:
                dao = WishlistDAO()
                id = dao.insertItemWishlist(item_id, account_id)
                result = self.mapToWishlistItemDict([id, item_id, account_id])
                return jsonify(Wishlist_Item=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def mapToWishlistItemDict(self, row):
        result = {}
        result["wishlist_item_id"] = row[0]
        result["item_id"] = row[1]
        result["account_id"] = row[2]
        return result
