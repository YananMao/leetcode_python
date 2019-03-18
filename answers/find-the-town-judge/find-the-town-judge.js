var findJudge = function(N, trust) {
    let trustLists = {};
    let isTrustedLists = {};
    if(trust.length === 0 && N ===1){
        return 1
    }
    for (let i=0,len=trust.length;i<len;i++) {
        const trustIndex = trust[i][0];
        const trustedIndex = trust[i][1];
        if(!trustLists[trustIndex]){
            trustLists[trustIndex] = trustIndex;
        }
        if(!isTrustedLists[trustedIndex]){
            isTrustedLists[trustedIndex]=[trustIndex]
        }else{
            isTrustedLists[trustedIndex].push(trustIndex);
        }
    }
    for(let key in isTrustedLists){
        if(isTrustedLists[key].length === N-1 && !trustLists[key]  ){
            return key
        }
    }
    return -1
    
};