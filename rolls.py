from counter import Counter
import sys, random

if __name__ == '__main__':
	T = int(sys.argv[1])
	sides = 6
	rolls = [  ]
	for i in range(1, sides + 1):
		rolls.append(Counter(str(i) + 'lar'))
	for t in range(T):
		result = random.randint(1, 6)
		rolls[result -1 ].increment()
		
	for i in range(1, sides + 1):
		print(rolls[i - 1])