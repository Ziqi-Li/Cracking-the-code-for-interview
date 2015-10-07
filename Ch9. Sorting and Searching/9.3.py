'''
Ziqi Li
9.3 Given a sorted array of n integers that has been rotated an unknown number of times, give an O(log n) algorithm that finds an element in the array. You may assume that the array was originally sorted in increasing order.
'''
def findInRoatedSortedArray(nums,target):
    def helper(nums,left,right,target):
        mid = (left + right)/2
        if nums[mid] == target:
            return mid
        elif nums[left]<=target<nums[mid]:
            return helper(nums,left,mid-1,target)
        elif nums[mid]<target<=nums[right]:
            return helper(nums,mid+1,right,target)
        elif nums[mid]>nums[right]:
            return helper(nums,mid+1,right,target)
        elif nums[left]>nums[mid]:
            return helper(nums,left,mid-1,target)
        else:
            return -1
    return helper(nums,0,len(nums)-1,target)

def main():
    A = [15 ,16 ,19 ,20 ,25 ,1 ,3 ,4 ,5 ,7 ,10 ,14]
    print findInRoatedSortedArray(A,16)

if __name__ == "__main__":
    main()