from flask import jsonify
from dao.accountDao import AccountDAO

class AccountHandler:
    def getAllAccount(self):
        dao = AccountDAO()
        result = dao.getAllAccount()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToAccountDict(r))
        return jsonify(Account=mapped_result)

    def getAccountById(self, id):
        dao = AccountDAO()
        result = dao.getAccountById(id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToAccountDict(result)
            return jsonify(Account=mapped)

    def insertAccount(self, form):
        if len(form) != 6:
            return jsonify(Error="Malformed post request"), 400
        else:
            first_name = form['first_name']
            last_name = form['last_name']
            email = form['email']
            username = form['username']
            password = form['password']
            if first_name and last_name and email and password and username:
                dao = AccountDAO()
                id = dao.insertAccount(first_name, last_name, email, username, password)
                result = self.mapToAccountDict([id, first_name, last_name, email, username, password])
                return jsonify(Account=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def mapToAccountDict(self, row):
        result = {}
        result["account_id"] = row[0]
        result["first_name"] = row[1]
        result["last_name"] = row[2]
        result["email"] = row[3]
        result["username"] = row[4]
        result["password"] = row[5]
        return result

    def deleteAccount(self, form):
        if len(form) != 1:
            return jsonify(Error="Malformed post request"), 400
        else:
            id = form['id']
            if id:
                dao = AccountDAO()
                dao.deleteAccount(id)
                return jsonify(DeleteStatus="OK"), 200
