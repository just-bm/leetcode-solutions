# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stk=[]
        i=0
        dashes=0
        while i<len(traversal):
            #find the number of dashes
            if traversal[i]=='-':
                dashes+=1
                i+=1
            else:
                #not a dash we need to find the number that is present
                j=i
                while j<len(traversal) and traversal[j]!='-':
                    j+=1
                val=int(traversal[i:j])
                node=TreeNode(val) #creating a newnode
                #if dashes and len(stack) should be same
                while len(stk)>dashes:
                    stk.pop() #length and dashes are equal
                #if stack has no element perfrom nothing#if stack has elements, get the last element if left child of the last node is none, then add the new node to left child else to right child
                
                if stk and stk[-1].left is None:
                    stk[-1].left=node
                elif stk and stk[-1].right is None:
                    stk[-1].right=node
                stk.append(node)
                i=j
                dashes=0 #dashes should be set to zero

        #return root node
        return stk[0]
                

                
