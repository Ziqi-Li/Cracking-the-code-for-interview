'''
Ziqi Li
1.6 Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
'''

def rotate(img,n):
    for i in range (0,n):
        for j in range (i+1,n):
            img[i][j], img[j][i] = img[j][i], img[i][j]
    for i in range (0,n/2):
        for j in range (0,n):
            img[i][j], img[n-i-1][j] = img[n-i-1][j], img[i][j]
    return img


def main():
    print rotate([1],1)
    print rotate([[1,2],[3,4]],2)
    print rotate([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],4)
    print rotate([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]],5)

if __name__ == '__main__':
    main()