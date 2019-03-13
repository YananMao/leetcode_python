/**
 * @param {string[]} A
 * @return {number}
 */
var minDeletionSize = function(A) {
    if (A.length<2) {
        return 0;
    }
    let res = [];
    for(let i=0,len=A.length-1;i<len;i++){
        const cur = A[i];
        const next = A[i+1];
        for(let j=0,len1 = cur.length;j<len1;j++){
            if(cur[j]>next[j] && res.indexOf(j) === -1){
                res.push(j);
            }
        }
        
        
    }
    return res.length;
};