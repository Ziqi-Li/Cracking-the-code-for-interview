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

#check if the tree is a BST(4.5)
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

#create BST with min height (4.3)
def createBST(list):
    if not list:
        return None
    k = len(list)
    mid = k/2
    temp = tree(list[mid],None,None)
    temp.left = createBST(list[0:mid])
    temp.right = createBST(list[mid+1:k])
    return temp

def main():
    tree1 = tree(10,tree(9,tree(8,tree(5,None,None),None),None),tree(3,None,None))
    tree2 = tree(3,tree(2,tree(1,None,None),None),tree(9,None,None))
    list = [1,2,3,4,5,6,7,8,9]
    print "in order"
    printTreeInOrder(tree1)
    print "height",height(tree1)
    print "balanced?",balanced(tree1)
    print "BST?",checkBST(tree2)
    printTreeInOrder(createBST(list))


if __name__ == "__main__":
	main()