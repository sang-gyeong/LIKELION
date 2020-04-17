
'''문제 1. 전화번호 받기
조건 1. 저장할 때는 공백 문자 없이
조건 2. -, ., , 등이 들어올 때 전부 제외 하고 숫자만 저장!'''

#버전1 (예시 속 특수문자만 제거)
phone_num = input("전화번호를 입력하세요.")
phone_num = phone_num.strip()
phone_num = phone_num.replace(" ", "")
phone_num = phone_num.replace("-", "")
phone_num = phone_num.replace(",", "")
phone_num = phone_num.replace(".", "")
print(phone_num)
print()


#버전2 (숫자 외 전부 제거)
import re
phone_num2 = input("전화번호를 입력하세요.")
phone_num2 = phone_num2.strip()
phone_num2 = re.sub("[^0-9]", "", phone_num2)
print(phone_num2)
print()


'''문제 2. 영어 이름 받기
choi juwon 을 입력 받으면,
first name : Choi, last name: Juwon 이 출력되게 만들기'''

input_name = input("영어 이름을 입력하세요(성과 이름을 공백으로 구분해주세요!)")
eng_name = input_name.split(" ")
print(f"first name : {eng_name[0]}, last name: {eng_name[1]}")

