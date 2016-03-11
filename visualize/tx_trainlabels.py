import sys
i=0
one_in_x = int(sys.argv[1])
with open('trainlabels.txt', 'r') as f, open('Y.txt', 'w') as g:
	for line in f:
		if (i < 94250 and i%one_in_x==0):
			g.write("   "+"{:1.7e}".format(float(line))+"\n")
		i=i+1
