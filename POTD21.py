''' 
Problem of the Day 21 - 30th Sep 2024

Merge two BST 's

Given two BSTs, return elements of merged BSTs in sorted form.

Example :

Input:

BST1:

       5
     /   \
    3     6
   / \
  2   4  

BST2:

        2
      /   \
     1     3
            \
             7
            /
           6

Output: 1 2 2 3 3 4 5 6 6 7

Explanation: After merging and sorting the two BST we get 1 2 2 3 3 4 5 6 6 7.

'''

#Code

class Solution:
    def inorder(self, root, arr):
        # Perform in-order traversal and store the elements in arr
        if root is None:
            return
        self.inorder(root.left, arr)
        arr.append(root.data)
        self.inorder(root.right, arr)
    
    def mergeSortedLists(self, list1, list2):
        # Merge two sorted lists
        merged = []
        i = j = 0
        
        # Traverse both lists and add the smaller element to the merged list
        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1
        
        # Add any remaining elements from list1 or list2
        while i < len(list1):
            merged.append(list1[i])
            i += 1
        while j < len(list2):
            merged.append(list2[j])
            j += 1
        
        return merged
    
    def merge(self, root1, root2):
        # Step 1: Get the in-order traversal of both BSTs
        list1, list2 = [], []
        self.inorder(root1, list1)
        self.inorder(root2, list2)
        
        # Step 2: Merge the two sorted lists
        mergedList = self.mergeSortedLists(list1, list2)
        
        return mergedList
