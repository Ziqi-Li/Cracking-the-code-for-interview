'''
Ziqi Li
8.8 Write an algorithm to print all ways of arranging eight queens on a chess board so that none of them share the same row, column or diagonal.
'''
#Backtracking
def solveNQueens(n):
    def dfs(n,index,path,res):
    	if index==n:
    		temp = []
    		for i in xrange(n):
    			temp.append("*"*(path[i])+"Q"+"*"*(n-path[i]-1))
    		res.append(temp)
    		return
    	for i in xrange(n):
    		if not path:
    			dfs(n,index+1,path+[i],res)
    		elif i not in path:
    			flag = True
    			for j in xrange(len(path)):
    				if abs(path[j]-i)==abs(j-index):
    					flag = False
    					break
    			if flag:
    				dfs(n,index+1,path+[i],res)
    res = []
    dfs(n,0,[],res)
    return res,len(res)
		
def main():

	print solveNQueens(8)

if __name__ == "__main__":
    main()