from flask import jsonify
from dao.reviewDao import ReviewDAO

class ReviewHandler:
    def getReviewById(self, id):
        dao = ReviewDAO()
        result = dao.getReviewById(id)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToReviewDict(r))
        return jsonify(Reviews=mapped_result)

    def getSingleReviewById(self, item_id, review_id):
        dao = ReviewDAO()
        result = dao.getSingleReviewById(item_id, review_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToReviewDict(result)
            return jsonify(Review=mapped)

    def mapToReviewDict(self, row):
        result = {}
        result["review_id"] = row[0]
        result["item_id"] = row[1]
        result["account_id"] = row[2]
        result["rating"] = row[3]
        result["review_text"] = row[4]
        return result

    def insertReview(self, form):
        if len(form) != 4:
            return jsonify(Error="Malformed post request"), 400
        else:
            item_id = form['item_id']
            account_id = form['account_id']
            rating = form['rating']
            review_text = form['review_text']
            if item_id and rating and account_id and review_text:
                dao = ReviewDAO()
                id = dao.insertReview(item_id, account_id, rating, review_text)
                result = self.mapToReviewDict([id, item_id, account_id, rating, review_text])
                return jsonify(Review=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400