'''
Ziqi Li
4.4 Given a binary search tree, design an algorithm which creates a linked list of all the nodes at each depth 
(i.e., if you have a tree with depth D, you'll have D linked lists).
'''
from collections import deque
# tree structure
class treeNond:
    def __init__(self, data,left,right):
        self.data = data
        self.left = left
        self.right = right
class listNode:
	def __init__(self,data):
		self.data = data
		self.next = None
		
		
def printList(list):
	if not list:
		return ""
	return str(list.data) + printList(list.next)
	
	
#Tree to list 
def BFS(tree):
	if not tree:
		return
	res = []
	dq1 = deque([tree])
	dq2 = deque([])
	dummy = listNode(0)
	head = dummy
	while dq1:
		cur = dq1.popleft()
		head.next = listNode(cur.data)
		head = head.next
		if cur.left:
			dq2.append(cur.left)
		if cur.right:
			dq2.append(cur.right)
		if not dq1:
			dq1,dq2 = dq2,dq1
			res.append(dummy.next)
			head = dummy
			
	for i in res:
		print "->".join(printList(i))
	return
			
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
    temp = treeNond(list[mid],None,None)
    temp.left = createBST(list[0:mid])
    temp.right = createBST(list[mid+1:k])
    return temp

def main():
    list = [1,2,3,4,5,6,7,8,9]
    BFS(createBST(list))
    


if __name__ == "__main__":
	main()