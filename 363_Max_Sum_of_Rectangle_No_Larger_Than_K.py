import sys
import bisect
class Solution(object):
	def maxSumSubmatrix(self, matrix, k):
		length = len(matrix)
		width = len(matrix[0])
		Max = - sys.maxint
		if length < width:
			matrix_ = []
			for i in xrange(width):
				matrix_.append([])
				for j in xrange(length):
					matrix_[i].append(matrix[j][i])
			temp = length
			length = width
			width = temp
			for i in xrange(width):
				temp = [0]*length
				for j in xrange(i,width):
					for n in xrange(length):
						temp[n] += matrix_[n][j]
					# print temp
					tempMax = self.MaxSeqK(temp,k)
					if tempMax > Max:
						Max = tempMax
		else:
			for i in xrange(width):
				temp = [0]*length
				for j in xrange(i,width):
					for n in xrange(length):
						temp[n] += matrix[n][j]
					tempMax = self.MaxSeqK(temp,k)
					if tempMax > Max:
						Max = tempMax
		return Max
	# def twoDivide(self, array, value):
	# 	if array == []:
	# 		return 0
	# 	low = 0
	# 	high = len(array) - 1
	# 	if value <= array[low]:
	# 		return low
	# 	if value >= array[high]:
	# 		return high + 1
	# 	while low < high:
	# 		middle = (low + high)/2
	# 		if value > array[middle]:
	# 			low = middle + 1
	# 		if value < array[middle]:
	# 			high = middle - 1
	# 		if value == array[middle]:
	# 			return middle
	# 	return (low + high)/2
	def MaxSeqK(self, array, k):
		# print array,k
		Sum = []
		Sum.append(array[0])
		for i in xrange(1,len(array)):
			Sum.append(array[i] + Sum[i-1])

		Max = -sys.maxint
		Sum_ = []
		Sum_.append(0)
		for i in xrange(0,len(array)):
			Value = Sum[i] - k
			seq = bisect.bisect_left(Sum_,Value)
			# print seq, Sum_,Sum[i]
			if seq != len(Sum_):
				if Sum[i] - Sum_[seq] == k:
					return k
				else:
					temp = Sum[i] - Sum_[seq]
						# print Sum[i],Sum_[seq],temp
						# print temp,"1_"
						# print Sum_
					# else:
					# 	temp = Sum[i] - Sum_[seq + 1]
						# print temp,"2_"
				if Max < temp:
					Max = temp
			bisect.insort(Sum_,Sum[i])
		return Max