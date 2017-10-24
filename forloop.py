#leanring for loop



# read file.txt file
fo = open('file.txt')


# read all the line and print
for line in fo.readlines():
	print(line, end='')
	# by default print() function return one empty line after every print, if you need 
	# to stop this, just use end='' at the end of the function. Its only for Python 3