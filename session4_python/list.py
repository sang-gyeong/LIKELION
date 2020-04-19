# 리스트의 수정, 삭제, 삽입

# 수정
list_a = ['a', 'b', 'c']
print('수정 전', list_a)

list_a[0] = 'z'
print('수정 후', list_a, '\n')


# 삭제
list_b = ['a', 'b', 'c']
print('삭제 전', list_b)
del list_b[1]
print('삭제 후', list_b, '\n')


# 삽입
list_c = ['a', 'b', 'c']
print('삽입 전', list_c)
list_c.append('d')
print('삽입 후', list_c)
