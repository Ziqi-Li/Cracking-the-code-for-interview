'''
Ziqi Li
2.5 Given a circular linked list, implement an algorithm which returns node at the beginning of the loop.

DEFINITION
Circular linked list: A (corrupt)Linked list in which a node's next pointer points to an earlier node, so as to make a loop in the linked list.

EXAMPLE
Input: A -> B -> C -> D -> E -> C [the same C as earlier]
Output: C
'''

class node(object):
    def __init__(self, data,next):
        self.data = data
        self.next = next

def printList(list):
    while list.next:
        print list.data
        list = list.next

def findCircle(list):
    dict = {}
    if not list:
        return list
    while not (list.data in dict):
        dict[list.data] = True
        list = list.next

    return list.data

def main():
    
    nodeA = node('A',None)
    list = nodeA
    nodeB = node('B',None)
    nodeC = node('C',None)
    nodeD = node('D',None)
    nodeE = node('E',None)
    nodeA.next = nodeB
    nodeB.next = nodeC
    nodeC.next = nodeD
    nodeD.next = nodeE
    nodeE.next = nodeA
    #printList(list)
    print findCircle(list)

if __name__ == "__main__":
	main()