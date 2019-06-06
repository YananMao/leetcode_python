
  // Definition for singly-linked list.
  // function ListNode(val) {
  //     this.val = val;
  //     this.next = null;
  // }

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
   var head = new ListNode(0);
    var p = head;
    while (l1 || l2){
        if(!l1){
           p.next = l2;
            l2 = null;
            break;
        } 
        if (!l2){
            p.next = l1;
            l1 = null;
            break;
        }
        flag = l1.val<=l2.val;
        if(flag){
            p.next = l1;
            l1 = l1.next;
        }else{
            p.next = l2;
            l2 = l2.next;
        }
        p = p.next;
    }
    return head.next
    
    
};