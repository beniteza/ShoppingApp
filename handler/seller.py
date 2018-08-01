from flask import jsonify
from dao.sellerDao import SellerDAO

class SellerHandler:
    def getItemSellerById(self, id):
        dao = SellerDAO()
        result = dao.getItemSellerById(id) #item id
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToSellerDict(r))
        return jsonify(Reviews=mapped_result)

    def mapToSellerDict(self, row):
        result = {}
        result["seller_id"] = row[0]
        result["account_id"] = row[1]
        return result