class Solution:
    def longestPalindrome(self, s):
    	


    def isPalindrome(self, s):
    	isPali = True
    	i = 0, j = len(s) - 1
    	while i <= j:
    		if s[i] == s[j]:
    			i += 1
    			j -= 1
    		else:
    			isPali = False
    			break
    	return isPali

        