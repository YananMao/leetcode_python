class Solution:
  # 这种时间复杂度o(n^2),会超时，嘤嘤嘤
  # def maxProfit(self, prices):
  #   maxPro = 0;
  #   for i in range(len(prices)):
  #     for j in range(i+1,len(prices)):
  #       maxPro = max(maxPro,prices[j]-prices[i]);
  #   return maxPro;
  # 这种时间复杂度o(n)
  def maxProfit(self,prices):
    # python里面无穷大的表示方法
    minVal = float('inf');
    maxPro = 0;
    for i in range(len(prices)):
      if prices[i]<minVal:
        minVal = prices[i]
      elif prices[i]-minVal>maxPro:
        maxPro = prices[i]-minVal;
    return maxPro;

# print(Solution().maxProfit([7,1,5,3,6,4]));

