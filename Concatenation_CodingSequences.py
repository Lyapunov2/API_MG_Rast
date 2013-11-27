

def readFile (files):
	
	codSeq = []
	arch = open ( files , "r")
	for line in arch : 
		if line [0] != ">" :
				line = line [ : len ( line ) - 1]
				line = list (line)
				for i in range ( len ( line ) ) :
					codSeq.append (line [i])
	arch.close ()
	return codSeq

def outFile (seq, files) :
		files2 = files [: len (files) - 4 ]
		aux2 = list (files2)
		for i in range ( len ( aux2 )):
			if aux2 [i] == " ":
				aux2 [i] = "_"
		sep = ""		
		files2 = sep.join (aux2)
		nombArchOut = files2 + "_ConcatenatedCodingSeq" + ".faa"
		archOut = open ( nombArchOut , "w")
		auxHeader = files2 + "_Concatenated_Coding_Sequences"
		archOut.write (">%s\n" %auxHeader)
		i = 0 
		aux = "" 
		for i in range ( len ( seq ) ) : 		
			if len ( aux ) < 70 :
				aux = aux + seq [i]
			else :	
				archOut.write ( "%s\n" %aux)
				aux = ""
		archOut.write ( "%s\n" %aux)
		archOut.close ()	
		return archOut
			 

import os


for files in os.listdir ("."):	
	if files.endswith (".faa"):
		seq = readFile (files)
		outFile (seq, files)
		
