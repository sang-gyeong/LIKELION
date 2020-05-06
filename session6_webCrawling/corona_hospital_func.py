def extract_info(hospital_list):

    result = []

    for hospital in hospital_list :

        info_box = hospital.find_all("td")
        city = info_box[0].string
        district = info_box[1].string
        clinic_name = info_box[2].contents[0]
        telephone_num = info_box[3].string

        hospital_info = {
            "city" : city,
            "district" : district,
            "clinic_name" : clinic_name,
            "telephone_num" : telephone_num
        }
        result.append(hospital_info)
        
    return result