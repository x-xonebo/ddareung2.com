import csv
from bs4 import BeautifulSoup

reader = csv.reader(open('numOfBike.csv','r'), delimiter=",")
svg=open('Seoul_districts.svg','r').read()

bike_count={}
counts_only=[]
min_value=100; max_value=0; past_header=False
for row in reader:
    if not past_header:
        past_header=True
        continue

    try:
        unique=row[0]
        count=float(row[1].strip())
        bike_count[unique]=count
        counts_only.append(count)
    except:
        pass

# 뷰티풀숲으로 로드
soup = BeautifulSoup(svg)
# 구를 식별할 path 데이터 찾기
paths = soup.findAll('path')
# 지도시각화에 사용할 색상 설정
colors = ['#F1EEF6','#D4B9DA','#C994C7', '#DF65B0','#DD1C77','#980043']
# 지도에 나타낼 스타일 설정
path_style = 'font-size:12px;fill-rule:nonzero;stroke:#FFFFFF;stroke-opacity:1;\
              stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt\
              ;marker-start:none;stroke-linejoin:bevel;fill:'

# 따릉이 수에 따른 구 별 색상부여
for p in paths:
    if p['id']:
        try:
            count=bike_count[p['id']]

        except:
            continue 

        # 색상을 부여할 값의 범위
        if count>70:
            color_class=5
        elif count>60:
            color_class=4
        elif count>50:
            color_class=3
        elif count>40:
            color_class=2
        elif count>30:
            color_class=1
        else:
            color_class=0    

        color=colors[color_class]
        p['style']=path_style+color

print(soup.prettify())