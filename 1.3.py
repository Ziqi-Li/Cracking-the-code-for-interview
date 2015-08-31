'''
Ziqi Li
1.3 Design an algorithm and write code to remove the duplicate characters in a string without using any additional buffer. NOTE: One or two additional variables are fine. An extra copy of the array is not.
'''

def removeDups(string):
    return "".join(set(string))


def main():
    print removeDups("bcccca")
    print removeDups("cba")
    print removeDups("Li ZZqi")
    print removeDups(" Z ")

if __name__ == '__main__':
    main()