#save file as input3.py
print("INPUT THREE NUMBER")
A = float(input ("A: "))
B = float(input ("B: "))
C = float(input ("C: "))
x = -5
while True:
		y = A*x*x + B*x + C
		print(x,y) 
		x = x + 1
		if(x > 5):
			break
