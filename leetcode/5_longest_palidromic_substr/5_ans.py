class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length=1
        start = 0
        
        if len(s)==0:
            return ""
        elif len(s)==1:
            return s
        
        for i in range(len(s)):
            
            if i-max_length >= 0 and s[i-max_length:i+1]==s[i-max_length:i+1][::-1]:
                start = i-max_length
                max_length+=1
                continue
            
            if i-max_length-1 >= 0 and s[i-max_length-1:i+1]==s[i-max_length-1:i+1][::-1]:
                start = i-max_length-1
                max_length+=2

                
        return s[start:start+max_length]
