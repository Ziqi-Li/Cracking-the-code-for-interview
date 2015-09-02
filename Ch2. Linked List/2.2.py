'''
Ziqi Li
2.2 Implement an algorithm to find the nth to last element of a singly linked list.
'''



class node(object):
    def __init__(self,data,next):
        self.data = data
        self.next = next

def printList(list):
    while list.next:
        print list.data
        list=list.next

def findLastNth(list):
    global n
    if not list:
        return
    findLastNth(list.next)
    if n==1:
        print list.data
    n = n - 1

def main():
    list = node(0,node(1,node(2,node(3,node(4,node(5,None))))))
    #printList(list)
    global n
    n = 2
    findLastNth(list)


if __name__ == "__main__":
	main()