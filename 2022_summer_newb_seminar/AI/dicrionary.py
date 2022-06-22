class Dictionary:

    def __init__(self, key_list = [], value_list = []):
        self.key_list = key_list
        self.value_list = value_list

    def __str__(self):
        res = []
        for key, value in zip(self.key_list, self.value_list):
            res.append(key.__repr__() + ": " + value.__repr__())
        res = "{" + ", ".join(res) + "}"
        return res

dic = Dictionary(["one", "two", "three"], [1, 2, 3])
print(dic)
