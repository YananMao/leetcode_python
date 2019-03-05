class Solution:
# 	def lengthOfLongestSubstring(self, s):
# 		res = []
# 		i = 0
# 		while i<len(s):
# 			string = s[i]
# 			while i+1<len(s) and s[i+1] not in string:
# 				string  += s[i+1]
# 				i += 1
# 			if i+1<len(s):
# 				index = string.find(s[i+1])
# 				length = len(string)-index-2
# 				i -= length
# 			else:
# 				i += 1
# 			res.append(len(string))
# 		if len(s) == 0:
# 			return 0
# 		return max(res)
	def lengthOfLongestSubstring(self, s):
		res = 0
		start = 0
		dic = {}
		for index, val in enumerate(s):
			if val in dic:
				start = max(dic[val]+1,start)
			dic[val] = index
			res = max(res,index-start+1)
		return res


print(Solution().lengthOfLongestSubstring('abba'))

        