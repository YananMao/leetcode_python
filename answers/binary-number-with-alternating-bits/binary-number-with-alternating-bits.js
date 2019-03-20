var hasAlternatingBits = function(n) {
    const bin = n.toString(2);
    let temp = !bin[0];
    for(let i=0,len=bin.length;i<len;i++){
        if(bin[i]==temp){
            return false
        }else{
            temp = !temp;
        }
    }
    return true
    
};