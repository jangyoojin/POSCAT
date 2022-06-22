from dictionary import Dictionary

class Checker:

	def __init__(self):

		self.index = 0
		self.passed = 0
		self.failed = 0

		f = open("C:/Users/jangyj2020/Desktop/POSCAT/2022_summer_newb_seminar/AI/Week1_python_basic/Practice/solution", "r")
		self.answer = f.readlines()
		self.answer = [s[:-1] for s in self.answer]
		f.close()

	def test(self, function, result):
		
		result = str(result)
		if result == self.answer[self.index]:
			self.passed += 1
		else:
			self.failed += 1
			print("{} failed".format(function))
			print("expected: {}".format(self.answer[self.index]))
			print("actual  : {}\n".format(result))
		self.index += 1

	def print_result(self):
		print("----RESULT----")
		print("[PASS / TOTAL]\n[{:4d} / {:5d}]".format(self.passed, self.passed + self.failed))

checker = Checker()

def init_function_test():

	# 빈 딕셔너리 초기화 테스트
	checker.test("Dictionary()",
				Dictionary())

	# 내용이 있는 딕셔너리 초기화 테스트
	checker.test("Dictionary(['one', 'two', 'three'], [1, 2, 3])",
				Dictionary(['one', 'two', 'three'], [1, 2, 3]))

	# value로 리스트를 가지고 있는 딕셔너리 초기화 테스트
	checker.test("Dictionary(['one', 'two', 'three'], [[1], [2], [3]])",
				Dictionary(['one', 'two', 'three'], [[1], [2], [3]]))

def keys_test():

	# 빈 딕셔너리 keys 테스트
	checker.test("Dictionary().keys()",
				Dictionary().keys())

	# 내용이 있는 딕셔너리 keys 테스트
	checker.test("Dictionary(['one', 'two', 'three'], [1, 2, 3]).keys()",
				Dictionary(['one', 'two', 'three'], [1, 2, 3]).keys())

	# keys list를 변경해도 딕셔너리의 key는 안변하는지 테스트
	dic = Dictionary(['one', 'two', 'three'], [1, 2, 3])
	keys = dic.keys()
	keys[0] = 4
	checker.test("Key Consistecy Check", dic)

def values_test():

	# 빈 딕셔너리 values 테스트
	checker.test("Dictionary().values()",
				Dictionary().values())

	# 내용이 있는 딕셔너리 values 테스트
	checker.test("Dictionary(['one', 'two', 'three'], [1, 2, 3]).values()",
				Dictionary(['one', 'two', 'three'], [1, 2, 3]).values())

	# values list를 변경해도 딕셔너리의 value는 안변하는지 테스트
	dic = Dictionary(['one', 'two', 'three'], [1, 2, 3])
	values = dic.values()
	values[0] = "four"
	checker.test("Value Consistecy Check", dic)

def items_test():

	# 빈 딕셔너리 items 테스트
	checker.test("Dictionary().items()",
				Dictionary().items())

	# 내용이 있는 딕셔너리 items 테스트
	checker.test("Dictionary(['one', 'two', 'three'], [1, 2, 3]).items()",
				Dictionary(['one', 'two', 'three'], [1, 2, 3]).items())

def clear_test():

	# clear 테스트
	dic = Dictionary(['one', 'two', 'three'], [1, 2, 3])
	dic.clear()
	checker.test("Dictionary(['one', 'two', 'three'], [1, 2, 3]).clear()", dic)

	# clear 후에 추가가 잘 되는지 테스트
	dic['one'] = 1
	checker.test("Add element after Clear", dic)

def getitem_test():
	
	# __getitem__ 테스트
	checker.test("Dictionary(['one', 'two', 'three'], [1, 2, 3])['two']",
				Dictionary(['one', 'two', 'three'], [1, 2, 3])['two'])

def setitem_test():

	# 딕셔너리에 존재하는 key에 대해 __setitem__ 테스트
	dic = Dictionary(['one', 'two', 'three'], [1, 2, 3])
	dic['two'] = '2'
	checker.test("dic['two'] = '2'", dic)

	# 딕셔너리에 존재하지 않는 key에 대해 __setitem__ 테스트
	dic = Dictionary(['one', 'two', 'three'], [1, 2, 3])
	dic['four'] = 4
	checker.test("dic['four'] = 4", dic)

def contains_test():

	# 딕셔너리에 존재하는 key 확인
	checker.test("'one' in Dictionary(['one', 'two', 'three'], [1, 2, 3])",
				'one' in Dictionary(['one', 'two', 'three'], [1, 2, 3]))

	# 딕셔너리에 존재하지 않는 key 확인
	checker.test("'four' in Dictionary(['one', 'two', 'three'], [1, 2, 3])",
				'four' in Dictionary(['one', 'two', 'three'], [1, 2, 3]))

def update_test():

	# 두 딕셔너리 병합
	dic1 = Dictionary(["one", "two", "three"], [1, 2, 3])
	dic2 = Dictionary(["three", "four"], [333, 4444])
	dic1.update(dic2)
	checker.test("dic1.update(dic2)",
				dic1)

def setdefault_test():

	dic = Dictionary(['one', 'two', 'three'], [1, 2, 3])

	# 이미 딕셔너리에 key가 존재하는 경우
	checker.test("dic.setdefault('three', 333)",
				dic.setdefault("three", 333))
	checker.test("dic.setdefault('three', 333)",
				dic)

	# 딕셔너리에 key가 존재하지 않는 경우
	checker.test("dic.setdefault('four', 4444)",
				dic.setdefault('four', 4444))

	checker.test("dic.setdefault('four', 4444)",
				dic)

	# 딕셔너리에 key가 존재하지 않고, default가 주어지지 않은 경우
	checker.test("dic.setdefault('five')",
				dic.setdefault('five'))
	checker.test("dic.setdefault('five')",
				dic)

def pop_test():

	# 딕셔너리에서 key 제거
	dic = Dictionary(['one', 'two', 'three'], [1, 2, 3])
	checker.test("dic.pop('one')",
				dic.pop('one'))
	checker.test("dic.pop('one')",
				dic)

def len_test():

	# 비어있는 딕셔너리의 길이
	checker.test("len(Dictionary())",
				len(Dictionary()))

	# 비어있지 않은 딕셔너리의 길이
	checker.test("len(Dictionary(['one', 'two', 'three'], [1, 2, 3]))",
				len(Dictionary(['one', 'two', 'three'], [1, 2, 3])))

def main():

	init_function_test() # __init__() test

	len_test() # __len__() test

	getitem_test() # __getitem__() test

	setitem_test() #__setitem__() test

	contains_test() # __contains__() test

	setdefault_test() # setdefault() test

	pop_test() # pop() test

	keys_test() # keys() test

	values_test() # values() test

	items_test() # items() test

	clear_test() # clear() test

	update_test() # update() test

	checker.print_result()

if __name__ == "__main__":
	main()