'''
Ziqi Li
8.4 Write a method to compute all permutations of a string
'''

def permutations(nums):
    def helper(nums,index,path,res):
        if index==len(nums):
            res.append(path)
            return
        for i in xrange(0,len(nums)):
            if nums[i] not in path:
                helper(nums,index+1,path+[nums[i]],res)
    res = []
    helper(nums,0,[],res)
    return res


def main():
    print permutations([1,2,3,4])

if __name__ == "__main__":
    main()