import sys
class Solution(object):
	def kSmallestPairs(self, nums1, nums2, k):
		if len(nums1) == 0 or len(nums2) == 0:
			return []
		if k > len(nums1) * len(nums2):
			k = len(nums1) * len(nums2)

		current1 = []
		out1 = []
		for i in xrange(len(nums1)):
			current1.append(0)
			out1.append(0)
		result = []

		for i in xrange(k):
			Min = sys.maxint
			seq = 0
			for j in xrange(len(nums1)):
				if Min > nums1[j] + nums2[current1[j]] and out1[j] == 0:
					Min = nums1[j] + nums2[current1[j]]
					seq = j
			temp = []
			temp.append(nums1[seq])
			temp.append(nums2[current1[seq]])
			result.append(temp)
			if current1[seq] < len(nums2) - 1:
				current1[seq] += 1
			else:
				out1[seq] = 1
		return result