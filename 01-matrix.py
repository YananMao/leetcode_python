import collections;
class Solution:
  def updateMatrix(self, matrix):
    # 定义全局变量的两种方式,另一种是使用 global
    self.cols = len(matrix);
    self.lines = len(matrix[0]);
    # 生成一个跟matrix大小相同的矩阵来存储返回值
    res = [[-1]*self.lines for i in range(self.cols)];
    for 

print(Solution().updateMatrix([[0,1,1]]))

