public class Solution {
    public int lengthOfLongestSubstring(String s) {
    	HashMap<Character, Integer> map = new HashMap<Character, Integer>();
    	int start=0;
    	int lengthValue=0;
    	
    	for(int i=0;i<s.length();i++){
    		
    		
    		
    		if(map.containsKey(s.charAt(i))){	
    			
    			char tempC = s.charAt(i);
    			
    			if(start<map.get(s.charAt(i))+1){
    				start = map.get(s.charAt(i)) + 1;
    			}
    			//map.clear();
    			map.put(tempC, i);
    		}else{
    			map.put(s.charAt(i), i);	// char_index map
    		}
    		//System.out.println(i+"\t"+start+"\t"+(i-start+1));	
    		
    		if((i-start+1 > lengthValue) )
    			lengthValue=i-start+1;	
    		
    		
    		
    	}
    	if(s.length()==1)
    		lengthValue=1;
    	
    	//System.out.println(lengthValue);
    	return lengthValue;
    }
}
