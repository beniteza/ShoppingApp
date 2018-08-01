from flask import jsonify
from dao.sellerDao import SellerDAO

class SellerHandler:
    def getAllSeller(self):
        pass

    def getItemSupplierById(self, id):
        dao = SellerDAO()
        result = dao.getItemSupplierById(id) #item id
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

    def insertSeller(self, form):
        if len(form) != 1:
            return jsonify(Error="Malformed post request"), 400
        else:
            account_id = form['account_id']
            if account_id:
                dao = SellerDAO()
                id = dao.insertSeller(account_id)
                result = self.mapToSellerDict([id, account_id])
                return jsonify(Seller=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertSupplier(self, form):
        if len(form) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            account_id = form['item_id']
            seller_id = form['seller_id']
            if account_id and seller_id:
                dao = SellerDAO()
                id = dao.insertSupplier(account_id, seller_id)
                result = self.mapToSupplierDict([id, account_id, seller_id])
                return jsonify(Seller=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def mapToSupplierDict(self, row):
        result = {}
        result["supplies_id"] = row[0]
        result["item_id"] = row[1]
        result["seller_id"] = row[2]
        return result