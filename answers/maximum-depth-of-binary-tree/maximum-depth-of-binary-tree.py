# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def maxDepth(self,root):
    if root:
      # 这里不太明白self为什么是这样用的,应该跟python里面self的机制有关
      depth1 = self.maxDepth(root.left);
      depth2 = self.maxDepth(root.right);
      return max(depth2,depth1)+1;
    else:
      return 0;

