'''
Ziqi Li
1.6 Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0.
'''

def clearRowCol(img,m,n):
    if m == 1:
        for i in range(0,n):
            if img[i] == 0:
                return [0]*n
        return img

    visited = [[False for x in range(n)] for y in range(m)]
    def DFS(i,j):
        if i<0 or i>=m or j<0 or j>=n:
            return
        if visited[i][j]:
            return
        if img[i][j] == 0 and visited[i][j] == False:
            for x in range (0,m):
                img[x][j] = 0
                visited[x][j] = True
            for y in range(0,n):
                img[i][y] = 0
                visited[i][y] = True
        visited[i][j] = True
        DFS(i-1,j)
        DFS(i+1,j)
        DFS(i,j-1)
        DFS(i,j+1)
    DFS(0,0)
    return img


def main():
    print clearRowCol([1,2,3,4,0],1,5)
    print clearRowCol([[1,2],[3,0],[5,6]],3,2)
    print clearRowCol([[1,2,3,4],[5,6,7,8],[9,0,11,12],],3,4)
    print clearRowCol([[0,0,0,0,0],[0,0,0,0,0]],2,5)

if __name__ == '__main__':
    main()