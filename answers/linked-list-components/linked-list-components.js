/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number[]} G
 * @return {number}
 */
var numComponents = function(head, G) {
    debugger
    var p = head;
    var num =0;
    var flag = true;
    while(p){
        var val = p.val;
        if(G.indexOf(val)>-1){
            if(flag){
               num++;
               flag = false;
             }
        }else{
            flag = true;
        }
        p=p.next
    }
    return num
};