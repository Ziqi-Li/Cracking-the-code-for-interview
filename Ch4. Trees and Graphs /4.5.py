'''
Ziqi Li
4.1 Check if a tree is a balanced tree
4.3 Given a sorted (increasing order) array, write an algorithm to create a binary tree with minimal height.
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
def checkBST(tree):
    if not tree:
        return True
    if not checkBST(tree.left) or not checkBST(tree.right):
        return False
    if not tree.left and not tree.right:
        return True
    if not tree.left:
        return tree.data<=tree.right.data
    if not tree.right:
        return tree.data>=tree.left.data

    return tree.data>=tree.left.data and tree.data<=tree.right.data

def main():
    tree1 = tree(10,tree(9,tree(8,tree(5,None,None),None),None),tree(3,None,None))
    tree2 = tree(3,tree(2,tree(1,None,None),None),tree(9,None,None))
    print "BST?",checkBST(tree1)
    print "BST",checkBST(tree2)
    print "BST",checkBST(None)

if __name__ == "__main__":
	main()