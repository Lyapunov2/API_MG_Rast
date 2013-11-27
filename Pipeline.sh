#!/bin/bash

for file in $(ls -f *.faa) ;
		do 
		#echo $file;
		compseq $file -word 4 $file.comp;
done;


