from flask import Flask, request
from flask_cors import CORS, cross_origin

from handler.account import AccountHandler
from handler.cart import CartHandler

#ACTIVATE
app = Flask(__name__)

#Apply CORS to this app
CORS(app)

#Home page
@app.route("/ShoppingApp")
def home():
    return "Welcome to the online shopping application!"

#DB Routes
#Get all accounts, insert new account, delete account
@app.route("/ShoppingApp/account", methods=['GET', 'POST', 'DELETE'])
def account():
    if request.method == 'GET':
        return AccountHandler().getAllAccount()
    elif request.method == 'POST':
        return AccountHandler().insertAccount(request.get_json())
    elif request.method == 'DELETE':
        return AccountHandler().deleteAccount(request.get_json())

#Get an account using the id
@app.route("/ShoppingApp/account/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def getAccountById(id):
    # if request.method == 'GET':
        return AccountHandler().getAccountById(id)

#Get the items in an user's cart
@app.route("/ShoppingApp/account/cart/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def getCartById(id):
    # if request.method == 'GET':
        return CartHandler().getCartById(id)

###########################################
if __name__ == '__main__':
    app.debug = True
    app.run()