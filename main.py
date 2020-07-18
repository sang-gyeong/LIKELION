import requests
import csv
from bs4 import BeautifulSoup
from note import extract_info


file = open("notes.csv", mode="w", newline='') #읽기모드
writer = csv.writer(file)
writer.writerow(["title", "price", "img_src", "link"])


final_result = []
for i in range(5):
    print(f"{i+1}번째 페이지 크롤링 중...")
    note_html = requests.get(f"https://search.shopping.naver.com/search/all.nhn?origQuery=%EB%85%B8%ED%8A%B8&pagingIndex={i+1}&pagingSize=80&viewType=list&sort=rel&frm=NVSHPAG&query=%EB%85%B8%ED%8A%B8")
    note_soup = BeautifulSoup(note_html.text, "html.parser")
    note_list_box = note_soup.find("ul", {"class" : "goods_list"})
    note_list = note_list_box.find_all("li",{"class" : "_itemSection"})
    #하나가 아니기 때문에 find_all을 써서 배열로 담음!
    
    final_result += extract_info(note_list)
    #final_result = [{},{},{},{},...{}] + [{},{},{},{}...{}]
    
    for result in final_result :
        row = []
        row.append(result["title"])
        row.append(result["price"])
        row.append(result["img_src"])
        row.append(result["link"])
        writer.writerow(row)

print("크롤링 끝")
