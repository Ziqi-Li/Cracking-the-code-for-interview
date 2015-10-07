'''
Ziqi Li
8.7 Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents) and pennies (1 cent), write code to calculate the number of ways of representing n cents.
'''

def coins(n):
    def helper(n,cur):
        next = 0
        if cur == 25:
            next = 10
        elif cur == 10:
            next = 5
        elif cur == 5:
            next = 1
        elif cur == 1:
            return 1
        i = 0
        count = 0
        while i*cur<=n:
            count+=helper(n-i*cur,next)
        return count
    return helper(n,25)


def main():
    print coins(6)

if __name__ == "__main__":
    main()