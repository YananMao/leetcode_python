class Solution:
    def longestPalindrome(self, s):
    	maxLen = 0
    	start,end = 0,0
    	for i in range(len(s)):
    		for j in range(len(s),i,-1):
    			if self.isPalindrome(s[i:j]):
    				if j-i>maxLen:
    					maxLen = j-i
    					start = i
    					end = j
    				break
    	return s[start:end]



    def isPalindrome(self, s):
    	isPali = True
    	i, j = 0,len(s) - 1
    	while i <= j:
    		if s[i] == s[j]:
    			i += 1
    			j -= 1
    		else:
    			isPali = False
    			break
    	return isPali
print(Solution().longestPalindrome('addc'))

        