# binary search algorithm
import sys

def index(arr, key):
	lo = 0
	hi = len(arr) - 1
	while lo <= hi:
		mid = lo + (hi - lo) // 2
		if key < arr[mid]: hi = mid - 1
		elif key > arr[mid]: lo = mid + 1
		else: return mid
	return - 1

if __name__ == '__main__':
	if sys.argv[1]: allowlist = [int(num) for num in open(sys.argv[ 1 ], 'r')]
	else: sys.exit(0)
	allowlist = sorted(allowlist)
	while True:
		try:
			key = int(input())
			if index(allowlist, key) == - 1:
				print(key)
		except EOFError:
			break
