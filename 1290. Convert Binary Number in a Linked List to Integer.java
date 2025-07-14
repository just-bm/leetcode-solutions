/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int getDecimalValue(ListNode head) {
        int [] arr = new int[30];
        int i = 0;
        int len = 0;
        while (head != null) {
            
            arr[i] = head.val;
            head = head.next;
            i++;
            len++;
            
        }
        
        for ( i = 0; i < len / 2; i++) {
            int t = arr[i];
            arr[i] = arr[len - 1 - i];
            arr[len - 1 - i] = t;
        }
        int res = 0;
        for (i = 0; i < len; i++){
            if (arr[i] > 0) res += (Math.pow(2, i));
            System.out.println(res);
        }
        return res;
    }
}
