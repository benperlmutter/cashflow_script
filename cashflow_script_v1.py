#forecast_script.py
import sys, getopt

# scenario = sys.argv[1]

s="hello"
incAlph = "K"
inc = ""
cusp = False

for i in range(1,26):

	nextAlph = chr(ord(incAlph)+3)
	if ord(nextAlph) > ord("Z"):
		# print(ord("A"))
		# print(ord(incAlph)+3)
		# print(ord("Z"))
		# print(ord(incAlph)+3 - 28)
		# =IF(AND(C51="Inflow", OR(AND(K48>=E51,F51="Y"),AND(E51>=K48,E51<N48))),D51,0)
		if inc=="":
			inc = "A"
		else:
			inc = chr(ord(inc)+1)
		nextAlph = chr(ord(incAlph)+3 - 26)
		cusp = True

	
	s+=" ; =C50"

	if cusp:
		s+=" ; =IF(AND(C50=\"Inflow\", OR(AND("+incAlph+"48>=E50,F50=\"Y\"),AND(E50>="+incAlph+"48,E50<"+inc+nextAlph+"48))),D50,0)"
	else:
		s+=" ; =IF(AND(C50=\"Inflow\", OR(AND("+inc+incAlph+"48>=E50,F50=\"Y\"),AND(E50>="+inc+incAlph+"48,E50<"+inc+nextAlph+"48))),D50,0)"

	if cusp:
		s+=" ; =IF(AND(C50=\"Outflow\", OR(AND("+incAlph+"48>=E50,F50=\"Y\"),AND(E50>="+incAlph+"48,E50<"+inc+nextAlph+"48))),D50,0)"
	else:
		s+=" ; =IF(AND(C50=\"Outflow\", OR(AND("+inc+incAlph+"48>=E50,F50=\"Y\"),AND(E50>="+inc+incAlph+"48,E50<"+inc+nextAlph+"48))),D50,0)"

	incAlph = nextAlph
	cusp = False

print(s)

# =L2+IF(AND(A80 >= Summary!C7,OR(Summary!E7="All",REGEXMATCH(Summary!E7,"Most Likely"))),Summary!B7,0)