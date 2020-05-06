import requests
import csv
from bs4 import BeautifulSoup
from naver_books_func import extract_info

file = open("naver_books.csv", mode="w", newline='')
writer = csv.writer(file)
writer.writerow(["title", "img_src", "url", "author", "publisher", "price"])

final_result = []

for i in range(8):
    print(f"{i+1}번째 페이지 크롤링 중...")
    book_html = requests.get(f"https://book.naver.com/category/index.nhn?cate_code=100&tab=new_book&list_type=list&sort_type=publishday&page={i+1}")
    book_soup = BeautifulSoup(book_html.text, "html.parser")
    book_list_box = book_soup.find("ol", {"class" : "basic"}) 
    
    # 이용자수 과부화로, 첫번째 페이지에서 book_list_box가 None이 리턴되는 현상이 발생
    if book_list_box == None: 
        writer.writerow([f"{i+1}페이지 로딩실패", f"{i+1}페이지 로딩실패", f"{i+1}페이지 로딩실패", f"{i+1}페이지 로딩실패", f"{i+1}페이지 로딩실패", f"{i+1}페이지 로딩실패"])
        continue
    book_list = book_list_box.find_all("li")

    final_result += extract_info(book_list)

for result in final_result:
    row = []
    row.append(result["title"])
    row.append(result["img_src"])
    row.append(result["url"])
    row.append(result["author"])
    row.append(result["publisher"])
    row.append(result["price"])

    writer.writerow(row)

print("크롤링 끝")