public class Solution {
    public String longestPalindrome(String s) {
    	int left=0;
    	int right=0;
    	int RecLeft=0;
    	int RecRight=0;
    	int lengthCount=0;
    	int maxlength=0;
    	
    	for(int i=0 ; i < s.length(); i++){
    		left = i;
    		right = i;
    		
    		while(left>=0 && right<s.length()){

	    		char templeft = s.charAt(left);
	    		char tempright = s.charAt(right);
	    		
	    		//往外找不到一樣的字母
	    		if(templeft!=tempright){	    			
		    		if(lengthCount > maxlength){
		    			maxlength = lengthCount;
		    			RecLeft = left+1;
		    			RecRight = right-1;
		    		}
	    			break;
	    		}
	    		
	    		
	    		//往外有找到一樣的字母
	    		lengthCount = right - left + 1;
	    		left--;
	    		right++;	
	    		
	    		
	    		//判斷若是其中一邊超出範圍就要記錄位置
	    		if((left < 0 || right >=s.length()) && lengthCount>maxlength ){
	    			maxlength = lengthCount;
	    			RecLeft = left+1;
	    			RecRight = right-1;
	    		}
	    		
	    		
    		}
    		//System.out.println(RecLeft+"\t"+RecRight);
    		
    		left = i;
    		right = i+1;

    		while(left>=0 && right<s.length()){
    			if(s.charAt(left)!=s.charAt(right))
    				break;
	    		char templeft = s.charAt(left);
	    		char tempright = s.charAt(right);
	    		
	    		//往外找不到一樣的字母
	    		if(templeft!=tempright){	    			
		    		if(lengthCount > maxlength){
		    			maxlength = lengthCount;
		    			RecLeft = left+1;
		    			RecRight = right-1;
		    		}
	    			break;
	    		}
	    		
	    		
	    		//往外有找到一樣的字母
	    		lengthCount = right - left + 1;
	    		left--;
	    		right++;	
	    		
	    		
	    		if(lengthCount > maxlength){
	    			maxlength = lengthCount;
	    			RecLeft = left+1;
	    			RecRight = right-1;
	    		}
	    		/*
	    		//判斷若是其中一邊超出範圍就要記錄位置
	    		if((left < 0 || right >=s.length()) && lengthCount>maxlength ){
	    			maxlength = lengthCount;
	    			RecLeft = left+1;
	    			RecRight = right-1;
	    		}
	    		*/
    		}
    		
    		
    		
    	}
    	//System.out.println(s.substring(RecLeft,RecRight+1));
    	return s.substring(RecLeft,RecRight+1);
    }
}
