/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        ListNode* head=NULL;
        ListNode* tail=NULL;
        
        
        int carry=0;
        while(l1||l2||carry){
            int a = l1?l1->val:0;
            int b = l2?l2->val:0;
            
            int sum = a+b+carry;
            carry=0;
            if(sum>9){
                carry++;
                sum=sum-10;
            }
            ListNode* node = new ListNode(sum);
            if(!head){
                head = node;
                tail = node;
            }else{
                tail->next = node;
                tail = node;
            }
            
            l1= l1?l1->next:l1;
            l2= l2?l2->next:l2;
        }
        
        return head;
    }
};
