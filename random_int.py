# save this file as random_int.py
from random import randint
def randlist(r,usedlist):
	sum = 0
	alpha = ["a","b","c","d","e","f"]
	usedlist[r] = 1
	c = alpha[r]
	print (len(usedlist))
	for i in range (len(usedlist)):
		sum = sum + usedlist[r]
	#print (usedlist)
	return c,usedlist
	
def main():
	# initial variables
	uses = [0,0,0,0,0,0]
	done = False #boolean
	######################
	while done == False:
		r = randint(0,5) # make a random number
		c = randlist(r, used)
		#print(c,end="")
		#print (used)
		
main()
