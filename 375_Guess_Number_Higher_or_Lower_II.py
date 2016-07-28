import sys
class Solution(object):
	def getMoneyAmount(self, n):
		pay = []
		for i in xrange(n+1):
			pay.append([])
			for j in xrange(n+1):
				pay[i].append(0)

		for diff in xrange(n):
			if diff != 0:
				for left in xrange(1, n + 1 - diff):
					right = left + diff
					temp = []
					for pick in xrange(left, right + 1):
						if pick <= left + 1:
							leftValue = 0
						else:
							leftValue = pay[left][pick - 1]
						if pick >= right - 1:
							rightValue = 0
						else:
							rightValue = pay[pick + 1][right]
						temp.append(max(leftValue, rightValue)+pick)
					pay[left][right] = min(temp)
		return pay[1][n]