
def nextSmallerElementToLeft(arr, n):
	s = []
	res = []

	for i in range(0, n):
		while(len(s) != 0 and s[-1] >= arr[i]):
			s.pop()

		if len(s) == 0 :
			res.append(-1)

		else:
			res.append(s[-1])

		s.append(arr[i])

	return res
