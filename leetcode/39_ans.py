class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(candidates , idx ,target , path):
            if target<0:
                return
            if target==0:
                res.append(path)
                return
            
            for i in range(idx,len(candidates)):
                dfs(candidates,i,target-candidates[i],path+[candidates[i]])
            
            
        dfs(candidates,0,target,[])
        return res
