#forecast_script.py
import sys, getopt

scenario = sys.argv[1]

for i in range(2,86):
	s = "=L2"
	if (i==77) or (i==63) or (i==56) or (i==42) or (i==21) or (i==7):
		s += "+Summary!B6"
	for j in range(7,23):
		s += "+IF(AND(A" + str(i) + " >= Summary!C" + str(j) + ",OR(Summary!E"+str(j)+"=\"All\", REGEXMATCH(Summary!E"+str(j)+",\""+scenario+"\"))),Summary!B" + str(j) + ",0)"

	print(s)

#=L2+IF(AND(A80 >= Summary!C7,OR(Summary!E7="All",REGEXMATCH(Summary!E7,"Most Likely"))),Summary!B7,0)