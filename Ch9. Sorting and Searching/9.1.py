'''
Ziqi Li
9.1 You are given two sorted arrays, A and B, and A has a large enough buffer at the end to hold B. Write a method to merge B into A in sorted order.
'''

def mergeTwosortedArray(A,n,B,m):
    index = m+n-1
    i = n -1
    j = m-1
    while i>=0 and j>=0:
        if A[i]>=B[j]:
            A[index] = A[i]
            i-=1
        else:
            A[index] = B[j]
            j-=1
        index-=1
    while j>=0:
        A[index] = B[j]
        index-=1
        j-=1
    return A

def main():
    print mergeTwosortedArray([1,3,4,5,6,7,11,23,None,None,None,None,None,None,None],8,[1,2,3,4,8,9,10],7)

if __name__ == "__main__":
    main()