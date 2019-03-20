var missingNumber = function(nums) {
    const incre = nums.sort((a,b)=>{
        return a-b
    })
    for(let i=0,len=incre.length;i<len;i++){
        if(incre[i]!==i){
            return i
            
        }
        if(i===incre.length-1){
            return i+1
        }
    }
    
};