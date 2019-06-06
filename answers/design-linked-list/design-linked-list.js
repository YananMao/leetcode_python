/**
 * Initialize your data structure here.
 */
var reg = /^[1-9]\d*|0$/;
var MyLinkedList = function() {
    this.head = null;
    
};

/**
 * Get the value of the index-th node in the linked list. If the index is invalid, return -1. 
 * @param {number} index
 * @return {number}
 */
MyLinkedList.prototype.get = function(index) {
    var i = 0;
    var p = this.head;
    
    if(!reg.test(index)){
        return -1
    }
    while(p){
        if(i === index){
            return p.val
        }
        i++;
        p = p.next;
        
    }
    return -1
    
};

/**
 * Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtHead = function(val) {
    var p = {
        val: val,
        next:this.head
    };
    this.head = p;
    
};

/**
 * Append a node of value val to the last element of the linked list. 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtTail = function(val) {
    var p = this.head;
    while(p.next){
        p = p.next;
    }
    p.next = {
        val:val,
        next:null
    }
};

/**
 * Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. 
 * @param {number} index 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtIndex = function(index, val) {
    // if(!reg.test(index)){
    //     return
    // }
    
    if(index <= 0){
        var head = {
            val:val,
            next:this.head
        }
        this.head = head;
        return
    }
    var p = this.head;
    var i=0
    while(p){
        if(i === index-1){
            var temp = p.next;
            var newNode = {
                val:val,
                next:temp
            };
            p.next = newNode;
            return
        }
        i++;
        p = p.next;
    }
    
};

/**
 * Delete the index-th node in the linked list, if the index is valid. 
 * @param {number} index
 * @return {void}
 */
MyLinkedList.prototype.deleteAtIndex = function(index) {
    if(!reg.test(index)){
        return
    }
    if(index === 0){
        this.head = this.head.next;
        return
    }
    var i = 0;
    var p = this.head;
    while(p.next){
        if(index-1 === i){
           p.next = p.next.next
            return
        }
        p = p.next;
        i++;
    }
    
};

/** 
 * Your MyLinkedList object will be instantiated and called as such:
 * var obj = new MyLinkedList()
 * var param_1 = obj.get(index)
 * obj.addAtHead(val)
 * obj.addAtTail(val)
 * obj.addAtIndex(index,val)
 * obj.deleteAtIndex(index)
 */