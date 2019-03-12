var maxProfit = function(prices) {
    maxPro = 0;
    minPri = prices[0];
    for(var i=0,len=prices.length;i<len;i++){
      if(prices[i]<minPri){
        minPri = prices[i];
      }else{
        maxPro = Math.max(maxPro,prices[i]-minPri)
      }
    }
    return maxPro;
};