
#실습2 - 홀수구구단, 짝수구구단 함수 정의 후, 인자에 따라 함수를 실행하는 gugudan_odd_or_even 함수 정의 및 실행 
def gugudan_even():
 for i in range(2,10,2):
    for j in range(1,10):
        print("%d x %d = %d" % (i, j, i*j))

def gugudan_odd():
 for i in range(1,10,2):
    for j in range(1,10):
        print("%d x %d = %d" % (i, j, i*j))

def gugudan_odd_or_even(num):
    if num%2==0:
      gugudan_even()
    else:
      gugudan_odd()

gugudan_odd_or_even(2)
gugudan_odd_or_even(3)



#실습3 - 인자로 받은 숫자에 따라 1~num까지 구구단 출력하는 함수 정의 및 실행
def gugudan_by_num(num):
    for i in range (1,num+1):
        for j in range(1,10):
            print("%d x %d = %d" % (i, j, i*j))

gugudan_by_num(3)



#과제1 - FourCal 클래스에 사칙연산 할때마다 몇번 수행했는지 저장. 연산횟수 출력하는 메서드 추가
class FourCal:
    add_num = 0
    minus_num = 0
    mul_num = 0
    div_num = 0

    def __init__(self, name, age, univ):
        self.name = name
        self.age = age
        self.univ = univ

    def add(self, n1, n2):
        self.add_num +=1
        return n1 + n2
        
    def minus(self, n1, n2):
        self.minus_num +=1
        return n1 - n2
        
    def mul(self, n1, n2):
        self.mul_num +=1
        return n1 * n2
        
    def div(self, n1, n2):
        self.div_num +=1
        if n2 ==0 :
            print('0으로 나눌 수 없습니다')
            return None
        return n1 / n2

    def showCount(self):
        print(f"덧셈 : {self.add_num}\n뺄셈 : {self.minus_num}\n곱셈 : {self.mul_num}\n나눗셈 : {self.div_num}")


cal = FourCal("이상경", "26", "korea")
print(cal.name, cal.age, cal.univ)

cal.add(2,5)
cal.add(3,5)
cal.minus(7,5)
cal.mul(3,5)
cal.div(10,5)
cal.div(12,5)
cal.div(5,5)

cal.showCount()


