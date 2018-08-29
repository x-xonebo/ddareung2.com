# 부트스트랩 페이지 연결하기  
# 

import csv
import random
 
f = open('C:/Users/전유정/Desktop/multi/parkbicyclenew2.csv', 'r', encoding='UTF8')
rdr = csv.reader(f)
wedo = []
keungdo = []
for line in rdr:
    wedo.append(float(line[5]))
    keungdo.append(float(line[6]))
    

f.close()
'''
fp = open('C:/Users/전유정/Desktop/multi/parkbicycle.csv','r')
crd = csv.reader(fp)
lat = []
lon = []
for lines in crd:
    lat.append(float(lines[9]))
    lon.append(float(lines[10]))

fp.close()
'''
#dfijwofjqwoejoqwejfoqijwefio



# 플라스크 모듈 불러오기
from flask import Flask, render_template, request

# app 객체 생성
app = Flask(__name__)

# http://127.0.0.1:5000/
@app.route("/")
# 뷰함수 -> 화면 표시 함수
# templates 폴더 아래의 index.html 로 연결
def hello_world():
    return render_template('tvtvtv.html', wedo=wedo)

@app.route("/abcd/")
# 뷰함수 -> 화면 표시 함수
# templates 폴더 아래의 index.html 로 연결
def grape():
    
    return render_template('parkpark.html')

#@app.route('/qwer/')
#def grape():
#    return render_template('')

@app.route('/map/', methods=['POST'])
def apple():

    maping = request.form['maping']
    
   
    return render_template('jidopage.html', maping=maping, wedo=wedo, keungdo=keungdo, lat=lat, lon=lon)

# 앱 실행
if __name__ == "__main__":
    app.run(debug=True)

