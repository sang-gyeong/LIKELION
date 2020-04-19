# for 변수 in 리스트 :
#   수행할 문장 1
#   수행할 문장 2


users = ['주원', '준태', '중훈', '지환', '성우', '형제', '경연']

# 기본 문법
for user in users:
    print(user)

print('##########################')

# break
for user in users:
    if user == '중훈':
        break
    print(user)

print('##########################')

# continue
for user in users:
    if user == '중훈':
        continue
    print(user)


# range
a = range(10)
print(a[9])


for i in range(10):
    print(i)

print(a)