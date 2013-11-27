

x <- getwd()

listCsv <- dir(x, pattern="*comp.csv")

print (listCsv)

table <- c ()

for (g in listCsv)
{ 	
	arch <- paste (x, "/", g, sep = "")	
	f0 <- read.csv(arch, header = FALSE )
	y <- t (f0)
	y <- as.data.frame (y)
	table <- rbind (table, y [2,]) 
}


write.table (table, file = "PCoA_Genomes.csv", sep = ",")




names <- c ()


for (g in listCsv)
{ 	
	aux <- nchar (g) #length of a string
	auxName <- substr (g, 1, aux - 13 )
	names <-c (names, auxName) #Append the string to a vector
	

}

#Principal components Analysis


x <- read.csv ("PCoA_Genomes.csv", header = TRUE)

x.pca <- prcomp (x , scale = FALSE , center = TRUE)


write.table (x.pca$x [ ,1:2], file = "PCoA_MachineLearning.csv", sep = ",")
 


#Containing el names' vector all names samples

pdf ("PCoA_Genomes.pdf")
plot (x.pca$x)
text (x.pca$x, labels = names, cex = .6, pos = 4 )
dev.off()

#variacion.total <- sum (x.pca$sdev^2)

#x.pca$sdev^2/variacion.total

