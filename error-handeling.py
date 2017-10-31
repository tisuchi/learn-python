try:
	fh = open('xfile.txt')
	for line in fh.readline():
		print(line)
except:
	print("Something bad happend")