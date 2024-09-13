'''
    Problem of the Day 4 - 13th Sep 2024

    Given a Binary Tree, convert it into its mirror.

    Examples:

    Input:
      1
    /  \
   2    3
    Output: 3 1 2
    Explanation: The tree is
      1    (mirror)     1
     /  \    =>        /  \
    2    3           3   2

The inorder of mirror is 3 1 2
'''

#Code:

class Solution:
    def mirror(self, root):
        if root is None:
            return
        self.mirror(root.left)
        self.mirror(root.right)
        root.left, root.right = root.right, root.left

def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.data] + inorder_traversal(root.right)