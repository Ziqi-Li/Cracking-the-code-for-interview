'''
Ziqi Li
9.2 Write a method to sort an array of strings so that all the anagrams are next to each other.
'''
#O(NlogN)time
def sortAnagrams1(lst):
    def getKey(a):
        return sorted(a)
    return sorted(lst, key=getKey)

#O(N) time and O(N) space
def sortAnagrams2(lst):
    d = {}
    for i in lst:
        
        if "".join(sorted(i)) in d:
            d["".join(sorted(i))].append(i)
        else:
            d["".join(sorted(i))] = [i]
    res = []
    for j in d:
        for str in d[j]:
            res.append(str)
    return res



def main():
    A = ["axyz", "abc", "yzax", "bac", "zyxa", "fg", "gf"]
    print sortAnagrams1(A)
    print sortAnagrams2(A)

if __name__ == "__main__":
    main()