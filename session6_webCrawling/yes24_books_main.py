import requests
import csv
from bs4 import BeautifulSoup
from yes24_books_func import extract_info


file = open("yes24_books.csv", mode="w", newline='') #읽기모드
writer = csv.writer(file)
writer.writerow(["title", "img_src", "author", "publisher", "price", "summary"])

final_result = []

for i in range(20):
    print(f"{i+1}번째 페이지 크롤링 중...")
    book_html = requests.get(f"http://www.yes24.com/24/category/bestseller?CategoryNumber=001&sumgb=03&PageNumber={i+1}")
    book_soup = BeautifulSoup(book_html.text, "html.parser")
    book_list_box = book_soup.find("table", {"class" : "list"}) 
    book_list = book_list_box.find_all("tr")
    final_result += extract_info(book_list)

for result in final_result:
    row = []
    row.append(result["title"])
    row.append(result["img_src"])
    row.append(result["author"])
    row.append(result["publisher"])
    row.append(result["price"])
    row.append(result["summary"])

    writer.writerow(row)

print("크롤링 끝")