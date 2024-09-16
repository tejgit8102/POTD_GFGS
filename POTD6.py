''' 
Problem of the Day 6 - 15th Sep 2024

Binary Tree to DLL

Given a Binary Tree (BT), convert it to a Doubly Linked List (DLL) in place. The left and right pointers in nodes will be used as previous and next pointers respectively in converted DLL. The order of nodes in DLL must be the same as the order of the given Binary Tree. The first node of Inorder traversal (leftmost node in BT) must be the head node of the DLL.

Note: h is the tree's height, and this space is used implicitly for the recursion stack.

Input:
      1
    /  \
   3    2

Output:
3 1 2 
2 1 3

Explanation: DLL would be 3<=>1<=>2

'''
#Code

#Function to convert a binary tree to doubly linked list.
def fixPrevPtr(root):
    if root is not None:
        fixPrevPtr(root.left)
        root.left = fixPrevPtr.pre
        fixPrevPtr.pre = root
        fixPrevPtr(root.right)

def fixNextPtr(root):
    prev = None
    while (root and root.right != None):
        root = root.right
    while (root and root.left != None):
        prev = root
        root = root.left
        root.right = prev
    return root

class Solution:
    def bToDLL(self, root):
        fixPrevPtr.pre = None
        fixPrevPtr(root)
        return fixNextPtr(root)