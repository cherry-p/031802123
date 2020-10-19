import A
if __name__ == '__main__':
	a = A.A(A.Node([[2,8,3],[1,0,5],[4,7,6]]), A.Node([[1,2,3],[4,5,6],[7,8,0]]));
	print ("start:");
	if a.start():
		a.showPath();
	else:
		print ("no way");