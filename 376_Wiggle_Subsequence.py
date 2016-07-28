class Solution(object):	
	def wiggleMaxLength(self, nums):
		if len(nums) < 2:
			return len(nums)
		count = 0
		new_nums = []
		i = 0
		while i < len(nums) - 1:
			if nums[i] == nums[i+1]:
				new_nums.append(nums[i])
				temp = nums[i]
				i += 1
				while nums[i] == temp and i < len(nums) -1:
					i += 1
				i -= 1 
			else:
				new_nums.append(nums[i])
			i += 1
		if nums[-1] != nums[-2]:
			new_nums.append(nums[-1])

		if len(new_nums) < 2:
			return len(new_nums)
		i = 1
		while i < len(new_nums) - 1:
			if new_nums[i-1] < new_nums[i] and new_nums[i] > new_nums[i+1] or new_nums[i-1] > new_nums[i] and new_nums[i] < new_nums[i+1]:
				count += 1
			i += 1
		count += 2
		return count