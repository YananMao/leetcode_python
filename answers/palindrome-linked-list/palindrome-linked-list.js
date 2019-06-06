/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
    var p = head;
    var nodeArr = [];
    while(p){
        nodeArr.push(p.val);
        p = p.next;
    }
    for(i=0,j=nodeArr.length-1;i<=j;i++,j--){
        if(nodeArr[i] !== nodeArr[j]){
            return false
        }
    }
    return true
};