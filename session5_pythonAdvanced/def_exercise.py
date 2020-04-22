
def add(a,b):
    return a+b

def show_add(a,b):
    print(a+b)

def get_number():
    return 4

def say_hello():
    print("hello")



def isOddOrNot(num):
    if num%2==0:
        print('짝수')
    else:
        print('홀수')

isOddOrNot(2)
isOddOrNot(3)

def gugudan_even():
 for i in range(2,10,2):
    for j in range(1,10):
        print("%d x %d = %d" % (i, j, i*j))

def gugudan_odd():
 for i in range(1,10,2):
    for j in range(1,10):
        print("%d x %d = %d" % (i, j, i*j))

def gugudan(num):
    if num%2==0:
      gugudan_even()
    else:
      gugudan_odd()


gugudan(3)
gugudan(8)


