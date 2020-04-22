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


calculator = FourCal("이상경", "26", "korea")
print(calculator.name, calculator.age, calculator.univ)

print(calculator.add(2,5))
print(calculator.add(3,5))
print(calculator.minus(7,5))
print(calculator.mul(3,5))
print(calculator.div(10,5))
print(calculator.div(12,5))
print(calculator.div(5,5))

print(calculator.showCount())


