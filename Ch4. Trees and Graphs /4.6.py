'''
Ziqi Li
4.6 Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure. 
    NOTE: This is not necessarily a binary search tree.'''
# tree structure
class treeNond:
    def __init__(self, data,left,right):
        self.data = data
        self.left = left
        self.right = right

def isChild(root,a):
    if root ==a:
        return True
    if not root:
        return False
    return isChild(root.left,a) or isChild(root.right,a)

def LCA(root,a,b):
    if not root:
        return None
    elif root==a or root==b:
        return root
    elif isChild(root.left,a) and isChild(root.right,b) or (isChild(root.left,b) and isChild(root.right,a)):
        return root
    elif isChild(root.left,a) and isChild(root.left,b):
        return LCA(root.left,a,b)
    elif isChild(root.right,a) and isChild(root.right,b):
        return LCA(root.right,a,b)

def main():

if __name__ == "__main__":
	main()