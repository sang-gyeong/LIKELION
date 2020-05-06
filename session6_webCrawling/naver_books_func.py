def extract_info(book_list):

    result = []

    for book in book_list :

        title = book.find("a", {"class" : "N=a:bta.title"}).string
        img_src = book.find("a", {"class" : "N=a:bta.thumb"}).find("img")["src"]
        url = book.find("a", {"class" : "N=a:bta.title"})["href"]
        author = book.find("a", {"class" : "N=a:bta.author"}).string
        publisher = book.find("a", {"class" : "N=a:bta.publisher"}).string
        price_box = book.find("em", {"class" : "price"})
        if price_box == None:
            price = "가격정보 없음"
        else:
            price = price_box.string

        book_info = {
            "title" : title,
            "img_src" : img_src,
            "url" : url,
            "author" : author,
            "publisher" : publisher,
            "price" : price
        }
        result.append(book_info)
        
    return result