

#30/07/13 Perez Villarroya, David. Python script for transform compseq tables to csv format. 

def readFiles (files):
	arch = open ( files, "r")
	listLines = []	
	x = 0 
	for line in arch :
		x = x + 1
		if x > 16 :	
			div = "\t"
			line = line [:len (line) -1 ]
			line = line.split (div)
			listLines.append (line)

	del listLines [len (listLines)-1 ]
	del listLines [len (listLines)-1 ]
	listCSV = []
	for i in range (len (listLines)):
		aux = listLines[i][0]+","+listLines [i][3]
		listCSV.append (aux)
	nombArchOut = files + ".csv"
	archOut = open ( nombArchOut, "w")
	for i in range ( len ( listCSV) ) :
		archOut.write ("%s\n" %listCSV [i])
	archOut.close ()
		
		
		

import os	

x = os.getcwd ()#Obtain path directory 



for files in os.listdir ("."):	
	if files.endswith (".comp"):
	 	readFiles (files)




