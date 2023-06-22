#forecast_script.py

for i in range(20,44):
	s = "=0"
	for j in range(6,16):
		if j == 6:
			s += "+IF(A"+str(i)+">=A"+str(j)+",L6*31/2,0)"
		else:
			s += "+IF(A"+str(i)+">=A"+str(j)+",ABS((G"+str(j)+"-D"+str(j)+")*K"+str(j)+"*24*31/2),0)"

	print(s)
#=IF(A17>A4,H4*14,0)+IF(A17>A5,H5*14,0)