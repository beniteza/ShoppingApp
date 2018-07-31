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
