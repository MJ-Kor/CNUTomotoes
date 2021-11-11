import math
import requests
from bs4 import BeautifulSoup

def get_movie_title(movie_code):
    url = 'https://movie.naver.com/movie/bi/mi/basic.naver?code={}'.format(movie_code)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    result = requests.get(url, headers=headers)
    doc = BeautifulSoup(result.text, 'html.parser')

    title = doc.select('h3.h_movie > a')[0].get_text()
    return title

def calc_pages(movie_code):
    url = 'https://movie.naver.com/movie/bi/mi/basic.naver?code={}'.format(movie_code)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    result = requests.get(url, headers=headers)
    doc = BeautifulSoup(result.text, 'html.parser')

    all_count = doc.select('strong.total > em')[0].get_text().strip()
    return math.ceil(int(all_count) / 10)

def get_reviews(movie_code, pages):
    count = 0  # Total Review Count

    for pages in range(1, pages + 1):

        new_url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code={}&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'.format(movie_code, pages)
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
        result = requests.get(new_url, headers=headers)
        doc = BeautifulSoup(result.text, 'html.parser')
        review_list = doc.select('div.score_result > ul > li')

        for one in review_list:
            count += 1
            print('## USER -> {} ###################################################################'.format(count))

            # 평점 정보 수집
            score = one.select('div.star_score > em')[0].get_text()

            # 리뷰 정보 수집
            review = one.select('div.score_reple > p > span')[-1].get_text().strip()

            # 작성자(닉네임) 정보 수집
            original_writer = one.select('div.score_reple dt em')[0].get_text().strip()
            idx_end = original_writer.find('(')
            writer = original_writer[0:idx_end]

            # 날짜 정보 수집
            original_date = one.select('div.score_reple dt em')[1].get_text()
            date = original_date[:10]

            # yyyy.MM.dd 전처리 코드 작성
            #print('TITLE: {}'.format(title))
            print('REVIEW: {}'.format(review))
            print('WRITER: {}'.format(writer))
            print('SCORE: {}'.format(score))
            print('DATE: {}'.format(date))