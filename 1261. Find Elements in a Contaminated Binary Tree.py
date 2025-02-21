class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.set=set()

        def travel(node,curr):
            self.set.add(curr)

            if node.left is not None:
                travel(node.left,curr*2+1)
            if node.right is not None:
                travel(node.right,curr*2+2)
        travel(root,0)

    def find(self, target: int) -> bool:
        return target in self.set
        
