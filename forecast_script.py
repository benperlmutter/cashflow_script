#forecast_script.py

for i in range(2,53):
	s = "=L2"
	if (i==77) or (i==63) or (i==56) or (i==42) or (i==28) or (i==14):
		s += "+Summary!B6"
	for j in range(7,22):
		s += "+IF(A" + str(i) + " >= Summary!C" + str(j) + ",Summary!B" + str(j) + ",0)"

	print(s)