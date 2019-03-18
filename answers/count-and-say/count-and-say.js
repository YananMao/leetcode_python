var countAndSay = function(n) {
    if (n===1){
        return '1'
    }
    return getPron(countAndSay(n-1))
};
const getPron = (str)=>{
    let base = str[0];
    let index = 0;
    let res = '';
    for(let i=0,len=str.length;i<=len;i++){
       if(str[i] && str[i]===base){
           continue
       }else{
           res += (i-index)+base;
           base = str[i];
           index = i;
       }
        
    }
    return res
}