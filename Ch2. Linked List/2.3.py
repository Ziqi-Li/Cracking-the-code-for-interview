'''
Ziqi Li
2.3 Implement an algorithm to delete a node in the middle of a single linked list, given only access to that node.
EXAMPLE

Input: the node 'c' from the linked list a->b->c->d->e Result: nothing is returned, but the new linked list looks like a->b->d->e
'''

class node(object):
    def __init__(self,data,next):
        self.data = data
        self.next = next

def printList(list):
    if not list:
        print None
        return
    while list!= None:
        print str(list.data)
        list = list.next

    
def deleteNode(nodeX):
    while nodeX.next:
        p = nodeX
        nodeX.data = nodeX.next.data
        nodeX = nodeX.next
    p.next = None

	
def main():
    list = node(0,node(1,node(2,node(3,node(4,node(5,None))))))
    index = 2
    c = list
    for i in range(0,index):
        c = c.next
    deleteNode(c)
    printList(list)

if __name__ == "__main__":
	main()