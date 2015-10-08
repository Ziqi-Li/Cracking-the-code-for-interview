'''
Ziqi Li
8.2 Implement the "paint fill" function that one might see on many image editing programs. That is, given a screen (represented by a 2-dimensional array of Colors), a point, and a new color, fill in the surrounding area until you hit a border of that color.
'''
from collections import deque
def BFS(g,start,end):
	dq = deque([[start]])
	path=[]
	while dq:
		cur = dq.popleft()
		if cur[-1] == end:
			path.append(cur)
		for i in xrange(0,len(g[start])):
			if i!=cur[-1] and g[cur[-1]][i]==1:
				newPath = cur+[i]
				dq.append(newPath)
	return path
				
def DFS(g,start,end):
	def helper(g,start,end,path,res):
		if start == end:
			res.append(path)
			return
		for i in xrange(0,len(g[start])):
			if i!=start and g[start][i]==1:
				helper(g,i,end,path+[i],res)
	res = []
	helper(g,start,end,[start],res)
	return res


def printM(m):
	for k in m:
		print k 

def main():
	matrix = [[1,1,1,0,0,0,0],[0,1,0,1,0,0,0],[0,0,0,0,1,0,0],[0,0,0,1,0,1,1],[0,0,0,1,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1]]
	print "G is:"
	printM(matrix)
	print "BFS path",BFS(matrix,0,6)
	print "DFS path",DFS(matrix,0,6)

if __name__ == "__main__":
    main()