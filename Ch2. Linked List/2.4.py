'''
Ziqi Li
2.4 You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.

EXAMPLE
Input: (3 -> 1 -> 5), (5 -> 9 -> 2)
Output: 8 -> 0 -> 8
'''

class node(object):
    def __init__(self, data,next):
        self.data = data
        self.next = next

def printList(list):
    while list:
        print list.data
        list = list.next

def addTwo(a,b):
    c = node(None,None)
    list = c
    temp = 0
    while a or b:
        if not a:
            varA = 0
            varB = b.data
        if not b:
            varB = 0
            varA = a.data
        if a and b:
            varA = a.data
            varB = b.data

        sum = varA + varB + temp
        if sum >= 10:
            temp = 1
            c.next = node(sum - 10 ,None)
            c = c.next
        else:
            temp = 0
            c.next = node(sum,None)
            c = c.next
        if a:
            a = a.next
        if b:
            b = b.next
            
    if temp == 1:
        c.next = node(1,None)
    
    return list.next
	
def main():
    numA = node(9,node(9,node(9,node(9,None))))
    numB = node(1,None)
    
    printList(addTwo(numA,numB))

if __name__ == "__main__":
	main()

