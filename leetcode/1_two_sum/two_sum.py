class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        store={}
        
        
        for i in range(len(nums)):
            search = target - nums[i]
            if search in store:
                return [store[search],i]
            else:
                store[nums[i]] = i 
        return 0
