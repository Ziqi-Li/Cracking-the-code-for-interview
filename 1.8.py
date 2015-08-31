'''
Ziqi Li
1.8 Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (i.e., "waterbottle" is a rotation of "erbottlewat").
'''

def isSubstring(string,substring):
    return substring in string

def isRotation(stringA,stringB):
    if len(stringA) != len(stringB) or len(stringA) == 0 or len(stringB) == 0:
        return False
    return isSubstring(stringA + stringA,stringB)

def main():
    print isRotation("waterbottle","bottlewater")
    print isRotation("waterbottle","erbottlewat")
    print isRotation("","")
if __name__ == '__main__':
    main()