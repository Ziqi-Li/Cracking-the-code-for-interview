'''
Ziqi Li
4.5 Check if a tree is binary search tree
'''

# tree structure
class tree:
    def __init__(self, data,left,right):
        self.data = data
        self.left = left
        self.right = right


#in order print the tree
def printTreeInOrder(tree):
    if not tree:
        return
    printTreeInOrder(tree.left)
    print tree.data
    printTreeInOrder(tree.right)

#check if the tree is a BST
def isValidBST(root):
    min = float("-infinity")
    max = float("+infinity")
    def helper(root,min,max):
        if not root:
            return True
        if root.val<=min or root.val>=max:
            return False
        return helper(root.left,min,root.val) and helper(root.right,root.val,max)
    return helper(root,min,max)

def main():
    tree1 = tree(10,tree(9,tree(8,tree(5,None,None),None),None),tree(3,None,None))
    tree2 = tree(3,tree(2,tree(1,None,None),None),tree(9,None,None))
    print "BST?",checkBST(tree1)
    print "BST",checkBST(tree2)
    print "BST",checkBST(None)

if __name__ == "__main__":
	main()