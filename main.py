from flask import Flask, request
from flask_cors import CORS, cross_origin

from handler.account import AccountHandler
from handler.cart import CartHandler
from handler.wishlist import WishlistHandler
from handler.notification import NotificationHandler
from handler.review import ReviewHandler
from handler.item import ItemHandler
from handler.seller import SellerHandler
from handler.purchase import PurchaseHandler

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
def getAccount():
    if request.method == 'GET':
        return AccountHandler().getAllAccount()
    elif request.method == 'POST':
        return AccountHandler().insertAccount(request.get_json())

#Get an account using the id
@app.route("/ShoppingApp/account/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def getAccountById(id):
    return AccountHandler().getAccountById(id)

@app.route("/ShoppingApp/seller", methods=['GET', 'POST', 'DELETE'])
def getSeller():
    if request.method == 'GET':
        return SellerHandler().getAllSeller()
    elif request.method == 'POST':
        return SellerHandler().insertSeller(request.get_json())

#Get the items in an account's cart
@app.route("/ShoppingApp/account/cart/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def getCartById(id):
    if request.method == 'GET':
        return CartHandler().getCartById(id)
    elif request.method == 'POST':
        return CartHandler().insertItemCart(request.get_json())

#Get the items in an account's wishlist
@app.route("/ShoppingApp/account/wishlist/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def getWishlistById(id):
    if request.method == 'GET':
        return WishlistHandler().getWishlistById(id)
    elif request.method == 'POST':
        return WishlistHandler().insertItemWishlist(request.get_json())

#Get the notifications of an account
@app.route("/ShoppingApp/account/notification/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def getNotificationById(id):
    if request.method == 'GET':
        return NotificationHandler().getNotificationById(id)
    elif request.method == 'POST':
        return NotificationHandler().insertNotification(request.get_json())

@app.route("/ShoppingApp/account/notification/<int:account_id>/<int:notification_id>", methods=['GET', 'PUT', 'DELETE'])
def getSingleNotificationById(account_id, notification_id):
    return NotificationHandler().getSingleNotificationById(account_id, notification_id)

#Get reviews of an item and add a new review
@app.route("/ShoppingApp/item/review/<int:id>", methods=['GET', 'POST', 'DELETE'])
def getReviewById(id):
    if request.method == 'GET':
        return ReviewHandler().getReviewById(id)
    elif request.method == 'POST':
        return ReviewHandler().insertReview(request.get_json())

@app.route("/ShoppingApp/item/review/<int:item_id>/<int:review_id>", methods=['GET', 'POST', 'DELETE'])
def getSingleReviewById(item_id, review_id):
    return ReviewHandler().getSingleReviewById(item_id, review_id)

#Get items and add new ones
@app.route("/ShoppingApp/item", methods=['GET', 'POST', 'DELETE'])
def getAllItem():
    if request.method == 'GET':
        # return ItemHandler().getAllItem()
        pass
    elif request.method == 'POST':
        return ItemHandler().insertItem(request.get_json())

@app.route("/ShoppingApp/item/seller/<int:id>", methods=['GET', 'POST', 'DELETE'])
def getItemSupplierById(id):
    if request.method == 'GET':
        return SellerHandler().getItemSupplierById(id)

@app.route("/ShoppingApp/item/supplier", methods=['GET', 'POST', 'DELETE'])
def getItemSupplier():
    if request.method == 'GET':
        #return SellerHandler().getAllItemSupplier()
        pass
    elif request.method == 'POST':
        return SellerHandler().insertSupplier(request.get_json())

@app.route("/ShoppingApp/account/purchase/<int:id>", methods=['GET', 'POST', 'DELETE'])
def getPurchaseById(id):
    if request.method == 'GET':
        return PurchaseHandler().getPurchaseById(id)
    elif request.method == 'POST':
        return PurchaseHandler().insertPurchase(request.get_json())

@app.route("/ShoppingApp/account/purchase/<int:account_id>/<int:purchase_id>", methods=['GET', 'PUT', 'DELETE'])
def getSinglePurchaseById(account_id, purchase_id):
    return PurchaseHandler().getSinglePurchaseById(account_id, purchase_id)

@app.route("/ShoppingApp/account/purchase/item/<int:id>", methods=['GET', 'POST', 'DELETE'])
def getItemPurchaseById(id):
    if request.method == 'GET':
        return PurchaseHandler().getItemPurchaseById(id)
    elif request.method == 'POST':
        return PurchaseHandler().insertItemPurchase(request.get_json())

###########################################
if __name__ == '__main__':
    app.debug = True
    app.run()