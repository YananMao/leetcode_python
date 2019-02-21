# 使用字典来保存
# tc:o(n),sc:o(n)
class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'int':
      dic = {};
      for i in nums:
        if i in dic:
          del dic[i];
        else:
          dic[i] = i;
      return list(dic.keys())[0];

# 使用集合去重
# 2*(a+b+c) - (2a+2b+c) = c
# tc:0(n),sc:o(n)
class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'int':
      return 2*sum(set(nums))-sum(nums);


# 使用异或运算
# a^b^c = a^c^b
# a^a = 0
# a^0 = a
# 所以对list的所有元素进行异或运算,就能得到没有配对的那个
# tc:o(n),sc:o(1)
class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'int':
      res = 0;
      for i in nums:
        res ^= i;
      return res

        