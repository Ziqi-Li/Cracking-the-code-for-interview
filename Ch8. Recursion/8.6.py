'''
Ziqi Li
8.6 Implement the "paint fill" function that one might see on many image editing programs. That is, given a screen (represented by a 2-dimensional array of Colors), a point, and a new color, fill in the surrounding area until you hit a border of that color.
'''
from collections import deque
#DFS
def valid(matrix,m,n,x,y,color):
	if x<0 or x>=m or y<0 or y>=n:
		return False
	if matrix[x][y]==color:
		return False
	return True
	
def paintFillDFS(matrix,m,n,x,y,color):
    if valid(matrix,m,n,x,y,color):
        return
    else:
    	matrix[x][y]=color
    	paintFill(matrix,m,n,x+1,y,color)
    	paintFill(matrix,m,n,x,y+1,color)
    	paintFill(matrix,m,n,x-1,y,color)
    	paintFill(matrix,m,n,x,y-1,color)
	
#BFS
def paintFillBFS(matrix,m,n,x,y,color):
	dq = deque([])
	if valid(matrix,m,n,x,y,color):
		dq.append([x,y])
	while dq:
		cur = dq.popleft()
		X,Y = cur[0],cur[1]
		matrix[X][Y]=color
		if valid(matrix,m,n,X-1,Y,color):
			dq.append([X-1,y])
		if valid(matrix,m,n,X,Y-1,color):
			dq.append([X,Y-1])
		if valid(matrix,m,n,X+1,Y,color):
			dq.append([X+1,Y])
		if valid(matrix,m,n,X,Y+1,color):
			dq.append([X,Y+1])
def printM(m):
	for k in m:
		print k 

def main():
	matrix = [[0,0,0,1,1,1,1,0],[0,0,1,0,0,0,1,0],[0,1,0,0,0,0,1,0],[0,1,0,0,0,0,1,0],[0,1,0,0,0,0,1,0],[0,1,0,0,0,0,1,0],[0,1,1,1,0,0,1,0],[0,0,0,1,1,1,1,0]]
	printM(matrix)
	#paintFillDFS(matrix,8,8,4,3,1)
	paintFillBFS(matrix,8,8,0,7,1)
	print "after"
	printM(matrix)

if __name__ == "__main__":
    main()