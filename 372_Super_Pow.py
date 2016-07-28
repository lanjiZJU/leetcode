class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        b.reverse()
        record = a%1337
        remainder = 1
        for i in xrange(len(b)):
        	if i != 0:
        		record = pow(record,10)%1337
        		factor1 = record
        	else:
        		factor1 = record
        	remainder = (remainder*pow(factor1,b[i]))%1337
        return remainder