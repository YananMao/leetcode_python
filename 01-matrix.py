import collections;
class Solution:
  def updateMatrix(self, matrix):
      """
      :type matrix: List[List[int]]
      :rtype: List[List[int]]
      """
      self.nRow, self.nCol = len(matrix), len(matrix[0])
      self.ans = [['inf'] * self.nCol for i in range(self.nRow)]
      queue = collections.deque()
      
      for r in range(self.nRow):
          for c in range(self.nCol):
              if matrix[r][c] == 0:
                  self.ans[r][c] = 0
                  queue.append((r,c))
      self.bfs(queue)
      return self.ans
  
  def bfs(self, queue):
      while queue:
          (r, c) = queue.popleft()
          for (d_r, d_c) in [(1,0), (-1,0), (0,1), (0,-1)]:
              n_r, n_c = r+d_r, c+d_c
              if 0 <= n_r < self.nRow and 0 <= n_c < self.nCol and self.ans[r][c]+1 < self.ans[n_r][n_c]:
                  self.ans[n_r][n_c] = self.ans[r][c]+1
                  queue.append((n_r, n_c))
print(Solution().updateMatrix([[0,1,1]]))

