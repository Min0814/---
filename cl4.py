# 라이브러리 준비하기
import csv
import requests
from bs4 import BeautifulSoup

url ="https://www.kunsan.ac.kr/board/list.kunsan?boardId=BBS_0000011&menuCd=DOM_000000105001004000&contentsSid=214&cpath="

# 엑셀 파일로 저장하기
filename = "군산대 행사 및 뉴스.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)



# 웹 서버에 요청하기
res = requests.get(url)
res.raise_for_status()

# soup 객체 만들기
soup = BeautifulSoup(res.text, "lxml")
announcementBOX = soup.find('div', attrs={"class": "bbs_list01"}) # 전체 영역에서 'a' 태그를 찾지 않고 인기 급상승 영역으로 범위 제한
announcement = announcementBOX.find_all('tr') # 인기 급상승 영역에서 'a'태그 모두 찾아 변수 announcement에 할당

i = 1

# 반복문으로 제목 가져오기(터미널 창 출력 및 엑셀 저장)
for announcement1 in announcement: 
    title = announcement1.get_text(strip=True)  # 텍스트 추출
    print(f"{str(i)}위: {title}")
    data = [str(i), title]
    writer.writerow(data)
    i += 1
    #.