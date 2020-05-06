import requests
import csv
from corona_hospital_func import extract_info
from bs4 import BeautifulSoup

file = open("corona_hospital.csv", mode="w", newline='')
writer = csv.writer(file)
writer.writerow(["city", "district", "clinic_name", "telephone_num"])

hospital_html = requests.get("https://www.mohw.go.kr/react/popup_200128_3.html")
hospital_html.encoding = "utf-8"
hospital_soup = BeautifulSoup(hospital_html.text, "html.parser")
hospital_list_box = hospital_soup.find("tbody", {"class" : "tb_center"}) 
hospital_list = hospital_list_box.find_all("tr")

final_result = extract_info(hospital_list)

for result in final_result:
    row = []
    row.append(result["city"])
    row.append(result["district"])
    row.append(result["clinic_name"])
    row.append(result["telephone_num"])

    writer.writerow(row)

print("크롤링 끝")