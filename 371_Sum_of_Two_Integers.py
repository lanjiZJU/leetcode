class Solution(object):
	def getSum(self, a, b):
		signal = -1
		operate = -1
		if a >= 0 and b >= 0:
			signal = 1
			operate = 1
		if a < 0 and b < 0:
			signal = 0
			operate = 1
			a = -a 
			b = -b
		if a >= 0 and b < 0:
			if a >= -b:
				signal = 1
				a = a
				b = -b
				operate = 0
			else:
				signal = 0
				temp = a
				a = -b
				b = temp
		if a < 0 and b >= 0:
			temp = a
			a = b
			b = temp
			if a >= -b:
				signal = 1
				a = a
				b = -b
				operate = 0
			else:
				signal = 0
				temp = a
				a = -b
				b = temp
		result = []
		aList = list(str(bin(a)))[2:]
		bList = list(str(bin(b)))[2:]
		aList.reverse()
		bList.reverse()
		# print aList
		# print bList
		# print operate
		# print signal
		if operate == 1:
			common = min(len(aList),len(bList))
			carry = 0
			# print aList
			# print bList
			for i in xrange(common):
				num1 = int(aList[i])
				num2 = int(bList[i])
				result.append(num1^num2^carry)
				if carry == 1:
					if num1 == 1 or num2 == 1:
						carry = 1
					else:
						carry = 0	
				else:
					if num1 == 1 and num2 == 1:
						carry = 1	
					else:
						carry = 0
			if len(aList) > common:
				for i in xrange(common, len(aList)):
					num1 = int(aList[i])
					result.append(num1^carry)
					if num1 == 1 and carry == 1:
						carry = 1
					else:
						carry = 0
				if carry == 1:
					result.append(carry)
			else:
				if len(bList) > common:
					for i in xrange(common, len(bList)):
						num1 = int(bList[i])
						result.append(num1^carry)
						if num1 == 1 and carry == 1:
							carry = 1
						else:
							carry = 0
					if carry == 1:
						result.append(carry)
				else:
					if carry == 1:
						result.append(carry)
			result.reverse()
			result_ = ""
			for item in result:
				result_ += str(item)
			if signal == 0:
				result_ = "-" + result_
			return int(result_,2)
		else:
			common = min(len(aList),len(bList))
			abdicate = 0
			for i in xrange(common):
				num1 = int(aList[i])
				num2 = int(bList[i])
				result.append(num1^num2^abdicate)
				if abdicate == 1:
					if num1 == 1 and num2 == 0:
						abdicate = 0
					else:
						abdicate = 1
				else:
					if num1 == 1 or num2 == 0:
						abdicate = 0
					else:
						abdicate = 1
			if len(aList) > common:
				for i in xrange(common, len(aList)):
					num1 = int(aList[i])
					result.append(num1^abdicate)
					if num1 == 1 or abdicate == 0:
						abdicate = 0
					else:
						abdicate = 1
			result.reverse()
			result_ = ""
			for item in result:
				result_ += str(item)
			if signal == 0:
				result_ = "-" + result_
			return int(result_,2)