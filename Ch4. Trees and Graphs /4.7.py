'''
Ziqi Li
4.7 You have two very large binary trees: T1, with millions of nodes, and T2, with hundreds of nodes. Create an algorithm to decide if T2 is a subtree of T1
'''

# tree structure
class treeNode:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right

def isSameTree(a,b):
	if not a and not b:
		return True
	if not a or not b:
		return False
	return a.data==b.data and isSameTree(a.left,b.left) and isSameTree(a.right,b.right)

def isSubTree(root,sub):

    if not sub:
    	return True
    if not root:
    	return False
    return isSameTree(root,sub) or isSubTree(root.left,sub) or isSubTree(root.right,sub)
        






def main():
	sub = treeNode(4,treeNode(3,None,None),treeNode(6,None,None))
	big = treeNode(1,treeNode(1,treeNode(2,None,None),treeNode(3,None,None)),treeNode(4,treeNode(3,None,None),treeNode(6,None,None)))
	print isSubTree(big,sub)
	print isSubTree(big,None)
	print isSubTree(None,big)
if __name__ == "__main__":
	main()