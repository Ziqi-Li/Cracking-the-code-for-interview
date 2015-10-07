'''
    Ziqi Li
    8.5 Implement an algorithm to print all valid (e.g., properly opened and closed) combinations of n-pairs of parentheses.
    '''

def parentheses(n):
    def dfs(n,left,right,path,res):
        if left == n and right ==n:
            res.append(path)
            return
        if left>=right and left<n:
            dfs(n,left+1,right,path+"(",res)
        if left>right and right<n:
            dfs(n,left,right+1,path+")",res)
    res = []
    dfs(n,0,0,"",res)
    return res


def main():
    print parentheses(3)

if __name__ == "__main__":
    main()