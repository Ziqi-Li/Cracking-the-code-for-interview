'''
Ziqi Li
4.1 Check if a tree is a balanced tree
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

#get the height of a tree
def height(tree):
    if not tree:
        return 0
    return max(height(tree.left),height(tree.right)) + 1

#check if the tree is balanced(4.1)
def balanced(tree):
    if not tree:
        return True
    return abs(height(tree.left)-height(tree.right))<=1

def main():
    tree1 = tree(10,tree(9,tree(8,tree(5,None,None),None),None),tree(3,None,None))
    tree2 = tree(3,tree(2,tree(1,None,None),None),tree(9,None,None))
    print "in order"
    printTreeInOrder(tree1)
    print "height",height(tree1)
    print "height",height(tree2)
    print "height",height(None)


if __name__ == "__main__":
	main()