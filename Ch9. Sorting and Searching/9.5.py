'''
Ziqi Li
9.5 Given a sorted array of strings which is interspersed with empty strings, write a method to find the location of a given string.

Example: find "ball" in ["at", "", "", "", "ball", "", "", "car", "","", "dad", "", ""] will return 4

Example: find "ballcar" in ["at", "", "", "", "", "ball", "car", "", "", "dad", "", ""] will return -1
'''

def searchInArray(string,target):
	def helper(string,left,right,target):
		if left>right:
			return -1
		mid = (left+right)/2
		if string[mid] == target:
			return mid
		leftNext = mid
		rightNext = mid
		if string[mid]!="":
			if string[mid] > target:
				return helper(string,left,mid-1,target)
			else:
				return helper(string,mid+1,right,target)
		while rightNext<=right and string[rightNext] == "":
			rightNext+=1
		while leftNext>=left and string[leftNext] == "":
			leftNext-=1
		print left,mid,right,leftNext,rightNext
		if rightNext>right or leftNext>=left and string[leftNext]>=target:
			return helper(string,left,leftNext,target)
		elif leftNext<left or rightNext<=right and string[rightNext]<=target:
			return helper(string,rightNext,right,target)
		return -1
			
			
	return helper(string,0,len(string)-1,target)
		
def main():
	A = ["at", "", "", "", "ball", "ballla", "", "car", "","", "dad", "", ""]
	B = ["","",""]
	print searchInArray(B,"a")
	print searchInArray(A,"ball")

if __name__ == "__main__":
    main()