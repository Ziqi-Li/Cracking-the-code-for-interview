'''
Ziqi Li
1.2 Implement a function to reverse string
'''

def reverse(string):
    return string[::-1]


def main():
    print reverse("a")
    print reverse("Ziqi Li")
    print reverse("   1234567890   ")

if __name__ == '__main__':
    main()