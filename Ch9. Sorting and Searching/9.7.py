'''
Ziqi Li
9.7 A circus is designing a tower routine consisting of people standing atop one another's shoulders. 
For practical and aesthetic reasons, each person must be both shorter and lighter than the person below him or her. 
Given the heights and weights of each person in the circus, write a method to compute the largest possible number of people in such a tower.

EXAMPLE:

Input (ht, wt): (65, 100) (70,150) (56, 90) (75, 190) (60, 95) (68, 110)

Output: The longest tower is length 6 and includes from top to bottom: (56, 90) (60,95) (65,100) (68,110) (70,150) (75,190)
'''
#DP-LIS and sort
def manTower(heights,weights):
	a = zip(heights,weights)
	a.sort(key=lambda x:x[0])
	res = 0
	left = 0
	right = left
	d = [1 for i in xrange(len(a))]
	res = 0
	for i in xrange(1,len(a)):
		for j in xrange(i):
			if a[i][1]>a[j][1]:
				d[i] = max(d[i],d[j]+1)
		res = max(res,d[i])
	print d			
	return res
		
def main():
	A = [65,70,75,80,85,90]
	B = [7,8,6,9,10,6.5]
	print manTower(A,B)

if __name__ == "__main__":
    main()