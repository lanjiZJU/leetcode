class Solution(object):
	def countNumbersWithUniqueDigits(self, n):
		if n == 0:
			return 1
		dp = []
		dp.append(1)
		for i in xrange(1,11):
			temp = 9
			for j in xrange(i-1):
				temp *= 9 - j
			dp.append(temp + dp[i-1])
		if n >= 11:
			return dp[10]
		return dp[n]