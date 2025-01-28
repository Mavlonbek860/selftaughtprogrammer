# data abstraction algorithms in Java 4th edition
#3:51, Jan 28, 2025
# A simple counter object. simulates a counter

class Counter:
	def __init__(self, name='Counter'):
		self._name = name
		self._count = 0
	def increment(self):
		self._count += 1
	def tally(self):
		return self._count
	def __repr__(self):
		return str(self._count) + ' ' + self._name
	def __lt__(self, other):
		return self._count < other._count
	def __gt__(self, other):
		return self._count > other._count
	def __eq__(self, other):
		return self._count == other._count

if __name__ == '__main__':
	import random, sys
	T = int(sys.argv[1])
	heads = Counter('heads')
	tails = Counter('tails')
	for i in range(T):
		if random.choice((0, 1)) == 0: heads.increment()
		else: tails.increment()
	print(heads)
	print(tails)
	delta = heads.tally() - tails.tally()
	print('delta = ', abs(delta))