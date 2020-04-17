
'''과제 1. 별찍기 - 아래와 같이 * 을 출력 하는 프로그램을 만들어보세요'''
for i in range(0,9):
    j = 9-i
    stars = ""
    while(j>0):
        j-=1
        stars += "*"
    print(stars)
print()


'''과제 2. 구구단 - 구구단 2단을 출력해보세요!'''
for i in range(1, 10):
    print(f"2 X {i} = {2*i}")
print()


'''과제 3. while 문을 활용하여 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보세요.'''
num=1
sum=0
while(num<=1000):
    if num%3==0:
        sum+=num
    num+=1
print(sum)
print()


'''과제 4. for 문을 활용하여 멋사 학생들의 평균 점수를 구해보세요.
- mutsa_scores = [90, 77, 40, 55, 90, 100, 88]'''

mutsa_scores = [90, 77, 40, 55, 90, 100, 88]
sum_score = 0
count = len(mutsa_scores)
for score in mutsa_scores:
    sum_score += score
print(sum_score/count)
print()