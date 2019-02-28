class Solution:
    def threeSum(self, nums):
      if min(nums)>=0 or max(nums)<=0 or len(nums)<3:
        return []
      # python自带的list排序函数
      else :
        nums.sort();
        res = [];
        for i in range(len(nums)):
          for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
              if nums[i]+nums[j]+nums[k]==0:
                res.append([nums[i],nums[j],nums[k]]);
        return list(set(res));





Solution().threeSum([-2,-1,1,1,2,3])

