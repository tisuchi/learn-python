try:
	fh = open('xfile.txt')
	for line in fh.readline():
		print(line)
except IOError as a:
	print("Something bad happened ({})". format(a))