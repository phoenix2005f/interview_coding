class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        length = len(nums)
        nums = sorted(nums)
        
        res=[]
        idx = 0
        
        
        def addsum(nums,length,idx,path):
            if (len(path)==3) and (sum(path)==0):
                if not any([path==ele for ele in res]):
                    res.append(path)
                return    
            if (len(path)==3) and (sum(path)!=0):
                return
            
            for i in range(idx,length):
                addsum(nums,length,i+1,path+[nums[i]])
                
        addsum(nums,length,idx,[])
        
        
        
        return res
