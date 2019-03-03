class Solution:
	def lengthOfLongestSubstring(self, s):
		res = []
		i = 0
		while i<len(s):
			string = s[i]
			while i+1<len(s) and s[i+1] not in string:
				string  += s[i+1]
				i += 1
			if i+1<len(s):
				index = string.find(s[i+1])
				length = len(string)-index-2
				i -= length
			else:
				i += 1
			res.append(len(string))
		if len(s) == 0:
			return 0
		return max(res)
# print(Solution().lengthOfLongestSubstring('dfdv'))

        