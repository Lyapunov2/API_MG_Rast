


def outFiles (files) :
	cont = 0 
	nombFile = ""
	arch = open ( files , "r" ) 
	for line in arch : 
		if line [0] == ">":
			if cont == 0 :
				seq = []
				nombFile = line [1: len (line) - 1]
				cont = 1
			else :
				nombFile2 = nombFile + ".faa"
				archOut = open ( nombFile2 , "w")
				archOut.write ( ">%s\n" %nombFile )
				for i in range ( len ( seq ) ) :
					archOut.write ("%s" %seq[i] )
				archOut.close () 
				seq = []
				nombFile = line [1: len (line) - 1]
		else :
			line = list ( line ) 
			for i in range ( len ( line ) ) :
				seq.append ( line [i] ) 
	
	nombFile2 = nombFile + ".faa"
	archOut = open ( nombFile2 , "w")
	archOut.write ( ">%s\n" %nombFile )
	for i in range ( len ( seq ) ) :
		archOut.write ("%s" %seq[i] )
	archOut.close () 		
	arch.close ()

	
import os


for files in os.listdir ("."):	
	if files.endswith (".faa"):
		outFiles (files)
		
