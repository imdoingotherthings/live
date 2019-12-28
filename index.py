from flask import Flask
from bs4 import BeautifulSoup
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Auto reload working?!'

@app.route('/lol')
def main():
    response = requests.get('https://watch.lolesports.com/schedule?leagues=all-star,lcs,lec,lck,lpl,lcs-academy,turkiye-sampiyonluk-ligi,cblol-brazil,lla,oce-opl,ljl-japan,worlds,msi,rift-rivals-na-eu,rift-rivals-kr-cn-lms-vn,league-of-legends-college-championship,european-masters')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.prettify())
    return ''