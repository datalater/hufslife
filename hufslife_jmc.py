import requests
import getpass
from bs4 import BeautifulSoup
import re
import time

#id, pw 미리 입력
yourid="doshiro"
yourpwd=getpass.getpass(prompt='Password:')

'''
#id, pw input으로 받기
yourid=input("아이디를 입력하세요 : ")
yourpwd=input("비밀번호를 입력하세요 : ")
'''
#리퀘스트에서 세션 객체를 생성
session=requests.Session()

#해당 url을 GET 방식으로 사이트 오픈(세션: 브라우져에서 웹페이지를 여는 것)
r=session.get("http://www.hufslife.com/?mid=main&act=dispMemberLoginForm")

#동일 session에서 BeautifulSoup 실시
#html=BeautifulSoup(r.text,"html.parser")

#로그인에 필요한 hidden input인 token과 params 데이터 가져오기
#token=html.input.next_sibling["value"]
params={
  '_filter':'login',
  'user_id':yourid ,
  'password':yourpwd,
  'module':'member',
  'act':'procMemberLogin'
  }

#로그인 url에 POST 방식으로 사이트 오픈
r=session.post("http://www.hufslife.com/index.php",params)

for i in range(5):
  r=session.get("http://www.hufslife.com/?mid=job&page={0}".format(i))
  html=BeautifulSoup(r.text,"html.parser")

  for review_title in html.find_all(string=re.compile("후기")):
    review_num = review_title.parent.parent.previous_sibling.previous_sibling.string
    review_author = review_title.parent.parent.next_sibling.next_sibling.string
    review_date = review_title.parent.parent.next_sibling.next_sibling.next_sibling.string
    print(review_num+"|"+review_title+"|"+str(type(review_author))+"|"+str(type(review_date)))
    

# review_title(ResultSet): html.find_all(string=re.compile("후기"))
# review_num: review_title.parent.parent.previous_sibling.previous_sibling.string
# review_date: 
# review_author:
