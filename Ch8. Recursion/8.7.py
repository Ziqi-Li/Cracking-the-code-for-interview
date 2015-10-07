'''
    Ziqi Li
    8.7 Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents) and pennies (1 cent), write code to calculate the number of ways of representing n cents.
    '''

def coins(n):
    def helper(n,cur):
        next = 0
        if cur == 25:
            next = 10
        if cur == 10:
            next = 5
        if cur == 5:
            next = 1
        if cur == 1:
            return 1
        i = 0
        count = 0
        while i*cur<=n:
            print i,n,next
            count+=helper(n-i*cur,next)
            i+=1
        return count
    return helper(n,25)


def main():
    print coins(5)

if __name__ == "__main__":
    main()