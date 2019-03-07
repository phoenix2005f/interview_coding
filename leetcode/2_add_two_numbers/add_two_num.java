/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        if(l1==null) return l2;
        if(l2==null) return l1;
        
        ListNode head = new ListNode(0);
        ListNode res = head;
        int carry=0;
        
        while(carry!=0 || (carry==0 && l1!=null && l2!=null)){
            
            if(l1==null && l2==null){
                head.next = new ListNode(carry);
                head = head.next;
                carry=0;
            }else{
                
                int num1 = l1==null?0:l1.val;
                int num2 = l2==null?0:l2.val;
                
                int temp = (num1+num2+carry)%10;
                carry = (num1+num2+carry)/10;
                
                head.next = new ListNode(temp);
                head = head.next;
                
                if(l1!=null) l1=l1.next;
                if(l2!=null) l2=l2.next;
            }
            
        }
        head.next = l1==null ? l2:l1;
        return res.next;
        
        
    }
}
