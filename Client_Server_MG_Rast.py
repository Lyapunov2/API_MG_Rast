#!/usr/bin/python

import urllib2
import json
import zlib
import re

#url = 'http://api.metagenomics.anl.gov/1/download/mgm4447943.3?file=650.3'
#req = urllib2.Request(url)
#req.add_header("Accept-Encoding", "gzip")

#response = urllib2.urlopen(req)
#json_data = response.read()

#data = zlib.decompress(json_data, 16+zlib.MAX_WBITS)
#data = json.loads(data)

#print json_data
#print data[1]["featureId"]
#print data

#fileOut = open ("Expand_protein.txt", "w")
#for line in data :
	#fileOut.write ("%s" %line)

#fileOut.close()



#url = 'http://api.metagenomics.anl.gov/1/download/mgm4447943.3?file=350.3'
#req = urllib2.Request(url)
#req.add_header("Accept-Encoding", "gzip")

#response = urllib2.urlopen(req)
#json_data = response.read()

#data = zlib.decompress(json_data, 16+zlib.MAX_WBITS)
	
#fileOut = open ("Sequences.txt", "w")
#for line in data :
	#fileOut.write ("%s" %line)

#fileOut.close()


tableRead = open ("Expand_protein.txt", "r")
seqID = []

for line in tableRead:
	line = line.split ("\t")
	if line [7] == 'KEGG' :
		if re.search ("EC:2.4.2.10", line [5]):	
			seqID.append (line [1])
			print line

	
tableRead.close () 


seqRead = open ("Sequences.txt", "r")
aux = 0
auxID = ""
outFile = open ("Sequence_By_EC.txt", "w")
for line in seqRead :
	if line [0] == ">" and aux == 0:
		for i in range ( len (seqID ) ) :
			if line [ 1: len (line) - 1 ] == seqID [i]:
				aux = 1
				auxID = seqID [i]		
	if line [0] != ">" and aux == 1 :
		line = line [:len (line) - 1]
		outFile.write (">%s\n" %auxID )
		outFile.write ("%s\n" %line)
		aux = 0 
		auxID = ""

outFile.close ()





