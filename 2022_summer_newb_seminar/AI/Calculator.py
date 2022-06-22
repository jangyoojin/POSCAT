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