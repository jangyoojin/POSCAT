#POSCAT AI seminar Practice1: class로 Dictionary 구현하기


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
    
    def __len__(self):
        return len(self.key_list)
    
    def __getitem__(self, key):
        return self.value_list[self.key_list.index(key)]
    
    def __setitem__(self, key, value):
        if key in self.key_list:
            self.value_list[self.key_list.index(key)] = value
        else:
            self.key_list.append(key)
            self.value_list.append(value)  

    def __contains__(self, key):
        if key in self.key_list:
            return True
        else:
            return False  

    def setdefault(self, key, default=None):
        if key in self.key_list:
            return self.value_list[self.key_list.index(key)]
        else:
            self.key_list.append(key)
            self.value_list.append(default)
            return default

    def pop(self, key):
        idx = self.key_list.index(key)
        res = self.value_list[idx]
        del self.value_list[idx]
        del self.key_list[idx]
        return res

    def keys(self):
        res = self.key_list.copy()
        return res
    
    def values(self):
        res = self.value_list.copy()
        return res
    
    def items(self):
        res = []
        for key, value in zip(self.key_list, self.value_list):
            res.append((key, value))
        return res
    
    def clear(self):
        self.key_list.clear()
        self.value_list.clear()
    
    def update(self, new_dic):
        for new_key, new_value in new_dic.items():
            if new_key not in self.key_list:
                self.key_list.append(new_key)
                self.value_list.append(new_value)
            else:
                self.value_list[self.key_list.index(new_key)] = new_value

