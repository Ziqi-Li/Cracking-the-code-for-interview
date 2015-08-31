'''
Ziqi Li
1.1 Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?
'''
def unique(string):
	if len("".join(set(string))) == len(string):
		return True
	else:
		return False
	
def main():
	print unique("ZZZZiiiiqqqiiii LLLLLLi")
	print unique("Ziqi Li")
	print unique("  ")
	print unique("")
	print unique("123409876")
if __name__ == "__main__":
	main()