class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs)==0:
            return ""
        res = ''
        
        sorted_strs = sorted(strs,key = lambda x:len(x))
        
        k_w = sorted_strs[0]
        
        for i in range(len(k_w)):
            k_c = k_w[i]
            if all(w[i]==k_c for w in sorted_strs):
                res+=k_w[i]
            else:
                break
            
        return res
