# while <조건문>:
#     <수행할 문장1>
#     <수행할 문장2>
#     <수행할 문장3>
#     ...


tree_hit = 0

# while tree_hit < 10:
#     tree_hit = tree_hit + 1
#     print("나무를 %d번 찍었습니다." % tree_hit)

#     if tree_hit == 10:
#         print("나무 넘어갑니다.")

# 위에랑 아래는 달라요.. 파이썬은 들여쓰기로 차별하거든요

while tree_hit < 10:
    tree_hit = tree_hit + 1
    print("나무를 %d번 찍었습니다." % tree_hit)

if tree_hit == 10:
    print("나무 넘어갑니다.")


# 포매팅
# print('몇번 : %d' % 10)

# number = 99
# print('몇번 : %d' % number)

# print('이름: %s' % '주원')
# name = '주원'
# print('이름: %s' % name)


# break

coffee = 10
money = 300

while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break


# continue

a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0:
        continue
    print(a)
