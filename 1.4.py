'''
Ziqi Li
1.4 Given two strings, write a method to decide if one is a permutation of the other
'''

def permutation(stringA, stringB):
    if sorted(stringA) == sorted(stringB):
    	return True
    else: 
    	return False


def main():
    print permutation("abc","bcccca")
    print permutation("abc","cba")
    print permutation("Ziqi Li", "Li ZZqi")
    print permutation("  Z"," Z ")

if __name__ == '__main__':
    main()