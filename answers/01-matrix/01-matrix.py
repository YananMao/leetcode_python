import collections;
class Solution:
  def updateMatrix(self, matrix):
    # 定义全局变量的两种方式,另一种是使用 global
    self.cols = len(matrix);
    self.lines = len(matrix[0]);
    # 生成一个跟matrix大小相同的矩阵来存储返回值
    self.res = [[10001]*self.lines for i in range(self.cols)];
    queue = collections.deque();
    for i in range(self.cols):
      for j in range(self.lines):
        if matrix[i][j] == 0:
          queue.append((i,j));
          self.res[i][j] = 0;
    self.travel(queue);
    return self.res;
  def travel(self,queue):
    while queue:
      (x,y) = queue.popleft();
      pos = [(-1,0),(0,-1),(0,1),(1,0)];
      for (i,j) in pos:
        (cx,cy) = (x+i,y+j);
        if -1<cx<self.cols and -1<cy<self.lines and self.res[cx][cy]>self.res[x][y]+1:
          self.res[cx][cy] = self.res[x][y]+1;
          queue.append((cx,cy));

print(Solution().updateMatrix([[0],[0],[0],[0],[0]]))

