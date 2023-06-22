#forecast_script.py

for i in range(22,74):
	s = "=H22/26"
	for j in range(4,17):
		if j == 4:
			s += "+IF(A"+str(i)+">=A"+str(j)+",(M4*31/2),0)"
		else:
			s += "+IF(A"+str(i)+">=A"+str(j)+",ABS((J"+str(j)+"-E"+str(j)+")*L"+str(j)+"*24*31/2),0)"

	print(s)
#=IF(A17>A4,H4*14,0)+IF(A17>A5,H5*14,0)