class Solution:
    def reverse(self, x: int) -> int:
        total=0
        first_zero = True
        sign = -1 if x<0 else 1
        
        
        if sign==-1:
            x = x*sign
        length = len(str(x))
        while x//10 !=0:
            remain = x%10
            x = x//10
            if (first_zero==True) and (remain==0):
                pass
                
            else:
                total += remain * 10**(length-1)
                first_zero=False
            length = length -1
        total += x%10
        res = sign*total
        
        if (res > 2**31-1) or (res < -1*2**31):
            res=0
        
        return res
