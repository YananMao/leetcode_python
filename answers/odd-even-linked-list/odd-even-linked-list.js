/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var oddEvenList = function(head) {
    if(!head){
        return null
    }
    var evenT = head;
    var oddH = head.next;
    var oddT = head.next;
    var i=0;
    while( oddT && oddT.next){
        evenT.next = oddT.next;
        evenT = evenT.next;
        oddT.next = evenT.next;
        oddT = oddT.next;
        
        
        
    }
    evenT.next = oddH;
    return head
};
