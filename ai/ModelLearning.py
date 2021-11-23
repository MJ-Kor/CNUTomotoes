#conda install -c conda-forge jpype1
#nltk
#matplotlib
# pip install konlpy
# conda install -c jmcmurray json

# Generate A.I Model
# >> Model : 긍정, 부정 분석 모델(감성분석)
# >> Module : Tensorflow, Keras
# >> Dataset : Naver Sentiment Movie Corpus(https://github.com/e9t/nsmc/)

#################
# Dataset Intro #
#################

# 데이터셋 : Naver Sentiment Movie Corpus(https://github.com/e9t/nsmc/)
# >> 네이버 영화 리뷰 중 영화당 100개의 리뷰를 모아
# >> 총 200,000개의 리뷰 (훈련: 15만개, 테스트: 5만개)로
# >> 이루어져있고, 1~10점까지의 평점 중 중립적인 평점(5~8)은
# >> 제외하고 1~4점을 부정, 9~10점을 긍정으로 동일한 비율로
# >> 데이터에 포함시킴
#
# >> 데이터는 id, document, label 세개의 열로 이루어져있음
# >> id : 리뷰의 고유한 key값
# >> document : 리뷰의 내용
# >> label : 긍정(1)인지 부정(0)인지 나타냄
#            평점이 긍정(9~10), 부정(1~4), 5~8점은 제거

import json
import os
import nltk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
from pprint import pprint
from konlpy.tag import Okt
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from tensorflow.keras import metrics

#############
# File Open #
#############

# ~.txt 파일에서 데이터를 불러오는 method
def read_data(filename):
    with open(filename, 'r', encoding='UTF-8') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        # 안에서부터 읽기 => for line in.. 부터 읽기
        # 위의 코드는
        # data = []
        # for line in f.read().splitlines():
        #       data.append(line.split('\t'))
        # 와 동일
        data = data[1:] # 제목열 제외
    return data

# nsmc 데이터를 불러와서 python 변수에 담기
# 프로그램 만들때는 상대 경로
# / => 하위 폴더
# .. => 상위 폴더
# . => 현재 폴더
train_data = read_data('./dataset/ratings_train.txt') # 트렝리닝 데이터 Open
train_test = read_data('./dataset/ratings_test.txt')
print(len(train_data))
print(train_data[0])
print(train_data[1])
print(len(train_test))
print(train_test[0])
print(train_test[1])