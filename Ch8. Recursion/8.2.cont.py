'''
Ziqi Li
8.2 magine a robot sitting on the upper left hand corner of an MxN grid. The robot can only move in two directions: right and down. How many possible paths are there for the robot?
FOLLOW UP
Imagine certain squares are "off limits", such that the robot can not step on them. Design an algorithm to get all possible paths for the robot.
'''

def robotWalk(m, n):
    if m == 1 or n == 1:
        return 1
    else:
        return robotWalk(m-1,n) + robotWalk(m,n-1)



def main():
    print robotWalk(2,2)

if __name__ == "__main__":
    main()