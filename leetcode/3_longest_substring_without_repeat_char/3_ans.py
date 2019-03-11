class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        lookup = {}
        start = 0 
        length = 0
        
        for i in range(len(s)):
            
            if s[i] in lookup:
                
           
                if  start < lookup[s[i]]+1:
                    start = lookup[s[i]]+1
                lookup[s[i]] = i
                
            else:
                lookup[s[i]] = i
            
            if i-start+1 > length:
                length = i-start+1
            
            if len(s)==1:
                length = 1
          
            
        return length
