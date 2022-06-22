from copy import copy

class Dictionary:
	
	def __init__(self, key = [], value = []):

		self.key_list = key
		self.value_list = value

	def __str__(self):
		res = []
		for key, value in zip(self.key_list, self.value_list):
			res.append("{}: {}".format(key.__repr__(), value.__repr__()))
		res = "{" + ", ".join(res) + "}"
		return res

	def __len__(self):
		return len(self.key_list)

	def __getitem__(self, key):
		idx = self.key_list.index(key)
		return self.value_list[idx]

	def __setitem__(self, key, value):
		if key in self.key_list:
			idx = self.key_list.index(key)
			self.value_list[idx] = value
		else:
			self.key_list.append(key)
			self.value_list.append(value)

	def __contains__(self, key):
		return key in self.key_list

	def setdefault(self, key, default = None):
		if not key in self.key_list:
			self.__setitem__(key, default)
		return self.__getitem__(key)

	def pop(self, key):
		idx = self.key_list.index(key)
		res = self.value_list[idx]
		del self.key_list[idx]
		del self.value_list[idx]
		return res

	def keys(self):
		return copy(self.key_list)

	def values(self):
		return copy(self.value_list)

	def items(self):
		return [(key, value) for key, value in zip(self.key_list, self.value_list)]

	def clear(self):
		del self.key_list[:]
		del self.value_list[:]

	def update(self, other):
		for key, value in other.items():
			self.__setitem__(key, value)