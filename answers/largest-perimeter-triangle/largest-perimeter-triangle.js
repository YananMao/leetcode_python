var largestPerimeter = function(A) {
    A=A.sort((a,b)=>{return b-a})
    for(let i=2,len=A.length;i<len;i++){
        if(A[i]+A[i-1]>A[i-2]){
            return A[i]+A[i-1]+A[i-2]
        }
        
    }
    return 0
    
};