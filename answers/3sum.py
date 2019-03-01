class Solution:
  # 时间复杂度为o(n^3),又超时了
  # def threeSum(self, nums):
  #   if  len(nums)<3 or min(nums)>0 or max(nums)<0:
  #     return []
  #   # python自带的list排序函数
  #   else :
  #     # 排序可以保证当有一组相同解不会有比如[a,b,c]和[c,b,a]的情况,更容易去重
  #     nums.sort();
  #     res = [];
  #     for i in range(len(nums)):
  #       for j in range(i+1,len(nums)):
  #         for k in range(j+1,len(nums)):
  #           if nums[i]+nums[j]+nums[k]==0:
  #             res.append([nums[i],nums[j],nums[k]]);
  #     # list(set(nums))适用于一维数组的去重，不能用于二维数组的去重
  #     # 二维数组的去重,把内层的list变成tuple.因为list保存的是在内存中的地址,无法进行set()
  #     return list(set([tuple(r) for r in res]));



  # 这是在discuss里看到的答案
  def threeSum(self, nums):
    if len(nums)<3 or min(nums)>0 or max(nums)<0:
      return []
    else:
      res = []
      nums.sort()
      # 我觉得这种方法的逻辑在于排序了之后，[a,b,...,c,...],如果a+b+c=0,那么其他两个与q相加之后得到0的数字一定在b与c之间
      # ps：我发现人家的代码都是没有分号的，学习一下
      # 那这种的时间复杂度呢，o(n^2)
      for i in range(len(nums)-2):
        if i > 0 and nums[i]==nums[i-1]:
          continue
        j = i+1
        k = len(nums)-1
        while j < k:
          s = nums[i] + nums[j] + nums[k]
          if s > 0:
            k -= 1
          elif s < 0:
            j += 1
          else:
            res.append([nums[i],nums[j],nums[k]])
            while j<len(nums)-1 and nums[j]==nums[j+1]:
              j += 1
            while k>0 and nums[k-1]==nums[k]:
              k -= 1
            j += 1
            k -= 1
    
      return res





# print(Solution().threeSum([-2,-1,1,1,2,3]))

