'''
Ziqi Li
9.6 Given a matrix in which each row and each column is sorted, write a method to find an element in it.
'''

def searchIn2DSortedArray(array,target):
	#Ignore case when just one col or one row, in which situation that we could use binary search
	#other wise the time complexity is O(M+N)
	m = len(array)
	n = len(array[0])
	i = m-1
	j = 0
	while i>=0 and j<n:
		if array[i][j] == target:
			return i,j,target
		elif array[i][j]>target:
			i-=1
		elif array[i][j]<target:
			j+=1
	return "No target" 
		
def main():
	A = [[1,2,3,4,5],[3,7,8,9,11],[5,9,10,17,18],[7,12,15,19,23],[9,13,16,20,25]]
	print searchIn2DSortedArray(A,21)

if __name__ == "__main__":
    main()