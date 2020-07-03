class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
root = TreeNode(val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}})

def levelOrderBottom(root) -> List[List[int]]:
    List = []

    def PreOrder(root):
        List.append(root.val)
        if (root.left) is None:
            List.append(None)
        else:
            PreOrder(root.left)
        if root.right is None:
            List.append(None)
        else:
            PreOrder(root.right)

    for ele in List:
        print(ele)
    return List


levelOrderBottom(root)
