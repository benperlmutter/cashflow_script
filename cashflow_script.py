#forecast_script.py
import sys, getopt

# scenario = sys.argv[1]

for j in range(50, 56):
	s="hello"
	incAlph = "K"
	inc = ""
	lastInc = ""
	cusp = False

	for i in range(1,26):

		nextAlph = chr(ord(incAlph)+3)
		if ord(nextAlph) > ord("Y"):
			# print(ord("A"))
			# print(ord(incAlph)+3)
			# print(ord("Z"))
			# print(ord(incAlph)+3 - 28)
			# =IF(AND(C51="Inflow", OR(AND(K48>=E51,F51="Y"),AND(E51>=K48,E51<N48))),D51,0)
			if inc=="":
				inc = "A"
			else:
				lastInc = inc
				inc = chr(ord(inc)+1)
			nextAlph = chr(ord(incAlph)+3 - 26)
			cusp = True

		
		s+=" ; =C"+str(j)

		if cusp:
			s+=" ; =IF(AND(C"+str(j)+"=\"Inflow\", OR(AND("+lastInc+incAlph+"48>=E"+str(j)+",F"+str(j)+"=\"Y\"),AND(E"+str(j)+">="+lastInc+incAlph+"48,E"+str(j)+"<"+inc+nextAlph+"48))),D"+str(j)+",0)"
		else:
			if ord(nextAlph) > ord("Z"):
				nextAlph = chr(ord(nextAlph)-1)
			s+=" ; =IF(AND(C"+str(j)+"=\"Inflow\", OR(AND("+inc+incAlph+"48>=E"+str(j)+",F"+str(j)+"=\"Y\"),AND(E"+str(j)+">="+inc+incAlph+"48,E"+str(j)+"<"+inc+nextAlph+"48))),D"+str(j)+",0)"

		if cusp:
			s+=" ; =IF(AND(C"+str(j)+"=\"Outflow\", OR(AND("+lastInc+incAlph+"48>=E"+str(j)+",F"+str(j)+"=\"Y\"),AND(E"+str(j)+">="+lastInc+incAlph+"48,E"+str(j)+"<"+inc+nextAlph+"48))),D"+str(j)+",0)"
		else:
			if ord(nextAlph) > ord("Z"):
				nextAlph = chr(ord(nextAlph)-1)
			s+=" ; =IF(AND(C"+str(j)+"=\"Outflow\", OR(AND("+inc+incAlph+"48>=E"+str(j)+",F"+str(j)+"=\"Y\"),AND(E"+str(j)+">="+inc+incAlph+"48,E"+str(j)+"<"+inc+nextAlph+"48))),D"+str(j)+",0)"

		incAlph = nextAlph
		cusp = False

	print(s)

# =L2+IF(AND(A80 >= Summary!C7,OR(Summary!E7="All",REGEXMATCH(Summary!E7,"Most Likely"))),Summary!B7,0)