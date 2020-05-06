def extract_info(book_list):

    result = []

    for i in range(len(book_list)):
        if i%2==0:
            goodsTxtInfo = book_list[i].find("td", {"class" : "goodsTxtInfo"})
            aupu = goodsTxtInfo.find("div", {"class" : "aupu"}).find_all("a")
            p_list = goodsTxtInfo.find_all("p")

            title = p_list[0].find("a").string
            price = p_list[1].find("span", {"class" : "priceB"}).string
            img_src = book_list[i].find("div", {"class" : "goodsImgW"}).find("a").find("img")["src"]
            
            if len(aupu)==1:
                author = "편집부"
                publisher = aupu[0].string
            else:
                author = aupu[0].string
                publisher = aupu[1].string
        else:
            try:
                summary = book_list[i].find("p", {"class" : "read"}).string.strip()
            except:
                summary = "내용 없음"

            book_info = {
                "title" : title,
                "img_src" : img_src,
                "author" : author,
                "publisher" : publisher,
                "price" : price,
                "summary" : summary
            }
            result.append(book_info)

    return result