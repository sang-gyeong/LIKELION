
def extract_info(note_list):
    result = []
    for note in note_list:
        title = note.find("div", {"class" : "tit"}).find("a").string
        price = note.find("span", {"class" : "price"}).find("em").text.strip() #find(em)없어도 되지만 price에 광고가있는경우 ㅇ류가 나므로 더 구체적으로 써주는 것이 해결방법이 왼다!
        img_src = note.find("img", {"class" : "_productLazyImg"})["data-original"]
        link = note.find("div", {"class" : "tit"}).find("a")["href"]

        note_info = {
        "title" : title,
        "price" : price,
        "img_src" : img_src,
        "link" : link
        }
        result.append(note_info)

    return result