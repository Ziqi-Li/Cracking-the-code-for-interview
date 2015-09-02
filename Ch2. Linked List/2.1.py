'''
Ziqi Li
2.1 Write code to remove duplicates from an unsorted linked list.
FOLLOW UP:
How would you solve this problem if a temporary buffer is not allowed?
'''
class node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class linkedList(object):
    def __init__(self,next = None):
        self.next = next

def printList(list):
    while list.next != None:
        list = list.next
        print str(list.data)

def removeDup(list):
    head = list
    dict = {}
    
    while list.next != None:
        p = list.next
        if not p.data in dict:
            dict[p.data] = True
            list = p
        else:
            print "haha"
            list.next = p.next
    return head


def main():
    #printList(linkedList(node(1,node(2,node(3,node(3,node(4,None)))))))
    printList(removeDup(linkedList(node(2,node(1,node(2,node(1,node(4,None))))))))

if __name__ == "__main__":
	main()