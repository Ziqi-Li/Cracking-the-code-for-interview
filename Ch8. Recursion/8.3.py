'''
Ziqi Li
8.3 Write a method that returns all subsets of a set.
'''

def subsets(nums):
    def helper(nums,index,path,res):
        if path not in res:
            res.append(path)
        for i in xrange(index,len(nums)):
            helper(nums,i+1,path+[nums[i]],res)
    res = []
    helper(sorted(nums),0,[],res)
    return res

def main():
    print subsets([1,2,3,4])

if __name__ == "__main__":
    main()