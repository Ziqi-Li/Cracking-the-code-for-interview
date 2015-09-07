'''
Ziqi Li
4.3 Given a sorted (increasing order) array, write an algorithm to create a binary tree with minimal height.
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
    list = [1,2,3,4,5,6,7,8,9]
    print "in order:"
    printTreeInOrder(createBST(list))


if __name__ == "__main__":
	main()