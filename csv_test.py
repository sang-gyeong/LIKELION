import requests
from bs4 import BeautifulSoup

book_html = requests.get("http://www.yes24.com/24/category/bestseller?CategoryNumber=001&sumgb=03&PageNumber=2")
book_soup = BeautifulSoup(book_html.text, "html.parser")
book_list_box = book_soup.find("table", {"class" : "list"}) 
book_list = book_list_box.find_all("tr")

for i in range(len(book_list)):
    if i%2==0:
        goodsTxtInfo = book_list[i].find("td", {"class" : "goodsTxtInfo"})
        aupu = goodsTxtInfo.find("div", {"class" : "aupu"}).find_all("a")
        p_list = goodsTxtInfo.find_all("p")

        title = p_list[0].find("a").string
        price = p_list[1].find("span", {"class" : "priceB"}).string
        img_src = book_list[i].find("div", {"class" : "goodsImgW"}).find("a").find("img")["src"]
        author = aupu[0].string
        publisher = aupu[1].string
    else:
        summary = book_list[i].find("p", {"class" : "read"})

        print(title)
        print(img_src)
        print(author)
        print(publisher)
        print(price)
        print(summary)