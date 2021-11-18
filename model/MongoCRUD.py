#conda activate cnu
#conda list
#conda install -c anaconda pymongo

# MongoDB Access and CRUD test

from pymongo import MongoClient

# 1. MongoDB connection (신뢰를 쌓는 것)
# IP = 선착장 , PORT = 항구
# 포트번호 = 프로그램 마다 접속할 수 있는 경로 , 27017 -> MongoDB의 포트번호
client = MongoClient('localhost', 27017) # (IP address, Port number) , localhost = 실제 내 컴퓨터 ip = 127.0.0.1
db = client['local']                     # Allocating 'local' DB
collections = db.get_collection('test')  # Allocating 'review' Collection

data = {'name' : 'cherry', 'age' : 8}
collections.insert_one(data)
# MongoDB > database > collection > document
# 우리은행 > 우리은행 광주지점 > 예금 > 50,000 입금 : 김민주
# CRUD => create, read, update, delete