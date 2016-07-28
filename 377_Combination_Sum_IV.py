class Solution(object):
    def combinationSum4(self, nums, target):
    	dp = []
    	for i in xrange(target + 1):
    		dp.append(0)
    	for i in xrange(1,target + 1):
    		for j in xrange(len(nums)):
    			if nums[j] < i:
    				dp[i] += dp[i - nums[j]]
    			if nums[j] == i:
    				dp[i] += 1
    	return dp[target]