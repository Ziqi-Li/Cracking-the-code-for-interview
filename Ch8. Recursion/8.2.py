'''
Ziqi Li
8.2 Implement the "paint fill" function that one might see on many image editing programs. That is, given a screen (represented by a 2-dimensional array of Colors), a point, and a new color, fill in the surrounding area until you hit a border of that color.
'''
def robotWalk(m, n):
    if m == 1 or n == 1:
        return 1
    else:
        return robotWalk(m-1,n) + robotWalk(m,n-1)

def robotPaths(matrix):
	n = len(matrix)
	m = len(matrix[0])
	def dfs(n,m,i,j,path,res):
		if i==n and j==m and matrix[i-1][j-1]==0:
			res.append(path+[(i,j)])
			
			return
		if i+1<=n and matrix[i][j-1]==0:
			dfs(n,m,i+1,j,path+[(i,j)],res)
		if j+1<=m and matrix[i-1][j]==0:
			dfs(n,m,i,j+1,path+[(i,j)],res)
			
	res = []
	dfs(n,m,1,1,[],res)
	return res

def printM(m):
	for k in m:
		print k 


def main():
	matrixA = [[0,0,0,1,1,1,1,0],[0,0,1,0,0,0,1,0],[0,0,0,0,0,0,1,0],[0,1,0,0,0,0,1,0],[0,1,0,0,0,0,1,0],[0,1,0,0,0,0,1,0],[0,1,1,1,0,0,0,0],[0,0,0,1,1,0,0,0]]
	matrixB = [[0,0,0,1],[1,0,0,0],[0,0,0,0]]
	printM(matrixB)
	A = robotPaths(matrixB)
	print "without traps there are:",robotWalk(len(matrixB),len(matrixB[0])),"paths"
	print "with traps paths are:"
	for i in A:
		print i

if __name__ == "__main__":
    main()