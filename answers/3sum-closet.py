class Solution:
  def threeSumCloset(self,nums,target):
    res = [];
    closetSum;
    distance = float('inf');
    for i in range(len(nums)):
      for j in range(i+1,len(nums)):
        for k in range(j+1),len(nums):
          res.append[nums[i]+nums[j]+nums[k]];
    for i in range(len(res)):
      if abs(res[i]-target)<distance:
        closetSum = res[i];
        distance = abs(res[i]-target);
    return closetSum;
