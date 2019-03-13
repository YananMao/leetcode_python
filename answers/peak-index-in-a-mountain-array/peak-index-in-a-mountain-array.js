// var peakIndexInMountainArray = function(A) {
//     for(let i=1,len=A.length-1;i<len;i++) {
//         if(A[i]>A[i+1]){
//            return i;
//         }
        
//     }
    
// };
// 使用...扩展运算符把数组变为参数序列
var peakIndexInMountainArray = function(A) {
    return A.indexOf(Math.max(...A));
};