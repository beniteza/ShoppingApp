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
        pass