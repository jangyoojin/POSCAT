#리스트 참조
l1=[1,2,3,4,5]
l2=l1.copy() #l2=l1[:]

print(id(l1),id(l2))

#list 원소 추가/삭제
lst = [1, 2, 3, 4, 5]
lst.append(6)
print(lst)

del lst[0]
print(lst)

#튜플
'''장정: 여러개의 변수에 값을 대입할 때 편리(단, 개수가 맞아야 함)'''
t = (1, 2, 3)
a, b, c = t
a, b, _ = t
print(a, b)
'''
#튜플은 수정이 불가능하다
t[0] = 5 #오류가 발생
'''
'''소괄호 생략 가능'''
t = 1, 2 
print(t)

#dictionary, set도 있음

#정수, 실수, 문자열, 리스트, 튜플
#lst[2:4], lst[-1]
#튜플: 리스트와 유사하지만 변경이 불가능. 대신 여러 개의 변수에 한 번에 대입할 수 있음

# if, while, for
# C와 달리 탭으로 블록 구분

#연이어서 출력하기
for i in range(1, 11):
    print(i, end=' ')

#두 리스트 더하기::zip
lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8, 9, 10]
lst3 = []

for x, y in zip(lst1, lst2):
    lst3.append(x+y)

#list 만들기
lst1 = [1, 2, 3, 4, 5]
lst2 = [i*2 for i in lst1]

#함수
def add(a, b):
    return a + b
print(add(1, 2))
print(add(1.4,2.0))

#가독성을 위해 함수 파라미터 자료형 명시
def add(a: int, b: int) -> int:
    return a + b
print(add(1.5/2)) #이렇게 쓸 수 있지만 쓰지 않는 것 권장

#class
#쿠키 틀이다. class로 만든 object가 쿠키
#예) 계산기
#메모리 기능 -> 가장 마지막 계산 결과를 가져오는 기능
class mini_calculator:

    # add, sub가 한 번이라도 호출되면 memory가 저장
    # 맨 처음에는? self.memory가 없음
    # 맨 처음에도 메모리를 추가하고 싶으면?

    #class에서 사용하는 특수한 함수: __init__()
    
    def __init__(self, x):
        self.memory = x

    def add(self, a, b): #self가 필요.
        #memory = a + b, 이렇게 하면 그냥 외부에 변수 memory가 생김
        self.memory = a + b
        return a + b
    
    def sub(self, a, b):
        self.memory = a - b
        return a - b

    def div(self, a, b):
        self.memory = a / b
        return a / b # b==0이면?

calc1 = mini_calculator(5)
calc2 = mini_calculator(10)

calc1.add(1, 2)
calc2.sub(3, 7)

print(calc1.memory)
print(calc2.memory)

#class 상속
class calculator(mini_calculator):
    #def add
    #def sub
    def mul(self, a, b):
        self.memory = a * b
        return a * b

    def div(self, a, b):
        if b== 0:
            return 0
        self.memory = a / b
        return a / b

cal = calculator(0)

print(cal.add(1, 4))
print(cal.mul(2, 4))

