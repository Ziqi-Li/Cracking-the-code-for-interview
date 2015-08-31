'''
Ziqi Li
1.5 Write a method to replace all spaces in a string with "%20". 
Note the end of string contains extra spaces to remain same length after adding "%20".
'''

def replaceSpaces(string):
    while string[-1] == " ":
        string = string[:-1]
    temp = ""
    for ch in string:
        if ch == " ":
            temp = temp + "%20"
        else:
            temp = temp + ch
    return temp

def main():
    print replaceSpaces("a b  ")
    print replaceSpaces("Li Ziqi  ")
    print replaceSpaces(" Li Zi Qi      ")

if __name__ == '__main__':
    main()