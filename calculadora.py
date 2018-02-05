#!/usr/bin/python3

import sys

if sys.argv[1] == 'sumar' :
	print (float(sys.argv[2]) + float(sys.argv[3]))
	
elif sys.argv[1] == 'restar' :
	print (float(sys.argv[2]) - float(sys.argv[3]))
	
elif sys.argv[1] == 'multiplicar' :
	print (float(sys.argv[2]) * float(sys.argv[3]))


elif sys.argv[1] == 'dividir' :
	try:	
		print (float(sys.argv[2]) / float(sys.argv[3]))
	except ZeroDivisionError:
			print ('Estas dividiendo entre cero')
	
else :
	print ('No esta esa función pon otra')

sys.exit()
	
