class Solution:
  # def threeSumClosest(self,nums,target):
  #   res = [];
  #   distance = float('inf');
  #   for i in range(len(nums)):
  #     for j in range(i+1,len(nums)):
  #       for k in range(j+1,len(nums)):
  #         res.append(nums[i]+nums[j]+nums[k]);
  #   for i in range(len(res)):
  #     if abs(res[i]-target)<distance:
  #       closetSum = res[i];
  #       distance = abs(res[i]-target);
  #   return closetSum;
  def threeSumClosest(self,nums,target):
    dis = float('inf');
    nums.sort()
    for i in range(len(nums)-2):
      if i > 0 and nums[i]==nums[i-1]:
        continue
      j = i+1
      k = len(nums)-1
      while j < k:
        s = nums[i] + nums[j] + nums[k]
        if s == target:
          return target
        else:
          if s > target:
              k -= 1
          elif s < target:
              j += 1
          if abs(s-target)<dis:
            dis = abs(s-target)
            res = s

    return res

    

# print(Solution().threeSumClosest([1,1,1,1],0))
