class Solution(object):
	def largestDivisibleSubset(self, nums):
		nums.sort()
		N = len(nums)
		dp = []
		path = []
		Max = 0
		k = 0
		result = []
		for i in xrange(N):
			dp.append(1)
			path.append(i)
		for i in xrange(N):
			for j in xrange(i):
				if nums[i]%nums[j] == 0:
					if dp[j] + 1 > dp[i]:
						dp[i] = dp[j] + 1
						path[i] = j
					if dp[i] > Max:
						Max = dp[i]
						k = i
		if path != []:
			while path[k] != k:
				result.append(nums[k])
				k = path[k]
			result.append(nums[k])
			result.sort()
		return result