import sys
class Solution(object):
	def maxFactor(self, x, y):
		Max = x if x > y else y
		Min = x if x < y else y
		if Max % Min == 0:
			return Min
		while Max % Min != 0:
			residual = Max % Min
			if Min % residual == 0:
				return residual
			Max = Min
			Min = residual

	def canMeasureWater(self, x, y, z):
		if z == 0:
			return True
		if x == 0 and y == 0 or z > x + y:
			return False
		if x == 0:
			if z - y == 0:
				return True
			else:
				return False
		if y == 0:
			if z - x == 0:
				return True
			else:
				return False
		maxFactor = self.maxFactor(x,y)
		if z % maxFactor == 0:
			return True
		else:
			return False