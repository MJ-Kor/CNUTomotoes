# DAO => Data Access Object
# Access => CRUD

from pymongo import MongoClient


# MongoDB Connection
def conn_mongo():
    client = MongoClient('localhost', 27017)  # (IP address, Port)
    db = client['local']                      # Allocating 'local' DB
    collection = db.get_collection('movie')   # Allocating 'movie' Collection
    return collection

# Create review data (데이터 등록)
def add_review(data):  # 한 건씩 등록
    collection = conn_mongo()    # MongoDB Connection
    collection.insert_one(data)  # Data save


# select review data (데이터 조회)
def get_reviews():  # 모든 데이터 조회
    collection = conn_mongo()   # MongoDB Connection
    review_list = []
    for one in collection.find({}, {'_id':0, 'TITLE':1, 'REVIEW':1, 'SCORE':1}):    # 제목, 리뷰, 평점만 DB 조회
        review_list.append([one['TITLE'], one['REVIEW'], one['SCORE']])
    return review_list