public class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        HashMap<Integer, Integer> map = new HashMap<>();
		int[] result = new int[2];
		
		for(int i =0;i<nums.length;i++){
			
			if(map.containsKey(nums[i])){
				
				int index = map.get(nums[i]);
				result[0]= index+1;
				result[1] = i+1;
				break;
				
			}else{
				//差_index
				map.put(target-nums[i], i);
			}
			
			
		}
		
		return result;
        
    }
}
