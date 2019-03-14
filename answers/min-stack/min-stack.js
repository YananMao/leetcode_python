var MinStack = function() {
    this.val = [];
    
};

MinStack.prototype.push = function(x) {
    this.val.push(x);
    
};

MinStack.prototype.pop = function() {
    if(this.val.length>0){
        this.val.splice(this.val.length-1,1);
    }
    
};

MinStack.prototype.top = function() {
    if(this.val.length>0){
        return this.val[this.val.length-1]
    }
    
};

MinStack.prototype.getMin = function() {
    return Math.min(...this.val);
    
};

