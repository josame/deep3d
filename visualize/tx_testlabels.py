i=0
with open('testlabels.txt', 'r') as f, open('txlabels.txt', 'w') as g:
	for line in f:
		if (i < 29500):
			g.write("   "+line)
		i=i+1
