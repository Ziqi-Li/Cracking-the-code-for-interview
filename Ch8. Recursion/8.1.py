'''
Ziqi Li
8.1 Write a method to generate the nth Fibonacci number.
'''

def fib(n):
    if n==1:
        return 1
    if n==2:
        return 1
    return fib(n-1) + fib(n-2)


def main():
    print fib(10)

if __name__ == "__main__":
    main()