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
var middleNode = function(head) {
    var nodeArray = [];
    var p = head;
    while(p){
        nodeArray.push(p);
        p = p.next;
    }
    return nodeArray[Math.floor(nodeArray.length/2)]
    
};