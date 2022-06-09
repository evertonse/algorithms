class Array(object):

	def __init__(self, items: list) -> None:
		self.items = items

	def __repr__(self) -> str:
		return '{}({})'.format(self.__class__.__name__, self.items)

	def __len__(self) -> int:
		return len(self.items)

	def __contains__(self, item: any) -> bool:
		return item in self.items

	def __getitem__(self, key: int) -> any:
		if key < 0: raise "key menor que zero"
		return self.items[key - 1]

	def __setitem__(self, key: int, value: any) -> None:
		if key < 0: raise "key menor que zero"
		self.items[key - 1] = value

	def __delitem__(self, key: int) -> None:
		if key < 0: raise "key menor que zero"
		del self.items[key - 1]