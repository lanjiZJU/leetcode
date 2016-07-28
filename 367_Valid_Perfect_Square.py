class Solution(object):
    def isPerfectSquare(self, num):
        for i in xrange(num+1):
        	if i*i == num:
        		return True
        	if i*i > num:
        		break
        return False