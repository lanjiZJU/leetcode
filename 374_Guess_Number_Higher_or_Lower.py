class Solution(object):
    def guessNumber(self, n):
    	low = 1
    	high = n
    	middle = (low + high)/2
    	while 1:
    		temp = guess(middle)
    		if temp > 0:
    			low = middle + 1
    		else:
    			if temp < 0:
    				high = middle -1
    			else:
    				return middle
    		middle = (low + high)/2