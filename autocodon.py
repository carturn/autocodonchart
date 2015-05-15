#Automatic Codon Chart
#Author: Carter Turnbaugh
#Last Modified: 5/14/2015

#Usage: python autocodon.py
#Modify the file to change the DNA

#Replace the DNA string with the DNA to analyze
dna = "atgttgactc taactcgcat ccgcactgtg tcctatgaag tcaggagtac atttctgttc atttcagtcc tggagtttgc agtggggttt ctgaccaatg ccttcgtttt cttggtgaat ttttgggatg tagtgaagag gcagccactg agcaacagtg attgtgtgct gctgtgtctc agcatcagcc ggcttttcct gcatggactg ctgttcctga gtgctatcca gcttacccac ttccagaagt tgagtgaacc actgaaccac agctaccaag ccatcatcat gctatggatg attgcaaacc aagccaacct ctggcttgct gcctgcctca gcctgcttta ctgctccaag ctcatccgtt tctctcacac cttcctgatc tgcttggcaa gctgggtctc caggaagatc tcccagatgc tcctgggtat tattctttgc tcctgcatct gcactgtcct ctgtgtttgg tgctttttta gcagacctca cttcacagtc acaactgtgc tattcatgaa taacaataca aggctcaact ggcagattaa agatctcaat ttattttatt cctttctctt ctgctatctg tggtctgtgc ctcctttcct attgtttctg gtttcttctg ggatgctgac tgtctccctg ggaaggcaca tgaggacaat gaaggtctat accagaaact ctcgtgaccc cagcctggag gcccacatta aagccctcaa gtctcttgtc tcctttttct gcttctttgt gatatcatcc tgtgctgcct tcatctctgt gcccctactg attctgtggc gcgacaaaat aggggtgatg gtttgtgttg ggataatggc agcttgtccc tctgggcatg cagccgtcct gatctcaggc aatgccaagt tgaggagagc tgtgatgacc attctgctct gggctcagag cagcctgaag gtaagagccg accacaaggc agattcccgg acactgtgct ga"

rna = dna.upper().replace("T", "U").replace(" ", "")

split_rna = ""

i = 0
length = len(rna)
while i < length:
	
	if i > 0 and i % 3 == 0: #Add space every third character
		
		split_rna += " "
	
	split_rna += rna[i]
	
	i += 1
	
codons = split_rna.split(" ") #Split by spaces to get codons

print codons

amino_acids = ""

i = 0
length = len(codons)
while i < length:
	
	#First Letter U
	#Second Letter U
	if codons[i] == "UUU":
		amino_acids += "phe "
	elif codons[i] == "UUC":
		amino_acids += "phe "
	elif codons[i] == "UUA":
		amino_acids += "leu "
	elif codons[i] == "UUG":
		amino_acids += "leu "
	#Second Letter C
	elif codons[i] == "UCU":
		amino_acids += "ser "
	elif codons[i] == "UCC":
		amino_acids += "ser "
	elif codons[i] == "UCA":
		amino_acids += "ser "
	elif codons[i] == "UCG":
		amino_acids += "ser "
	#Second Letter A
	elif codons[i] == "UAU":
		amino_acids += "tyr "
	elif codons[i] == "UAC":
		amino_acids += "tyr "
	elif codons[i] == "UAA":
		amino_acids += "stop"
	elif codons[i] == "UAG":
		amino_acids += "stop"
	#Second Letter G
	elif codons[i] == "UGU":
		amino_acids += "cys "
	elif codons[i] == "UGC":
		amino_acids += "cys "
	elif codons[i] == "UGA":
		amino_acids += "stop"
	elif codons[i] == "UGG":
		amino_acids += "trp "
	#First Letter C
	#Second Letter U
	elif codons[i] == "CUU":
		amino_acids += "leu "
	elif codons[i] == "CUC":
		amino_acids += "leu "
	elif codons[i] == "CUA":
		amino_acids += "leu "
	elif codons[i] == "CUG":
		amino_acids += "leu "
	#Second Letter C
	elif codons[i] == "CCU":
		amino_acids += "pro "
	elif codons[i] == "CCC":
		amino_acids += "pro "
	elif codons[i] == "CCA":
		amino_acids += "pro "
	elif codons[i] == "CCG":
		amino_acids += "pro "
	#Second Letter A
	elif codons[i] == "CAU":
		amino_acids += "his "
	elif codons[i] == "CAC":
		amino_acids += "his "
	elif codons[i] == "CAA":
		amino_acids += "gin "
	elif codons[i] == "CAG":
		amino_acids += "gin "
	#Second Letter G
	elif codons[i] == "CGU":
		amino_acids += "arg "
	elif codons[i] == "CGC":
		amino_acids += "arg "
	elif codons[i] == "CGA":
		amino_acids += "arg "
	elif codons[i] == "CGG":
		amino_acids += "arg "
	#First Letter A
	#Second Letter U
	elif codons[i] == "AUU":
		amino_acids += "ile "
	elif codons[i] == "AUC":
		amino_acids += "ile "
	elif codons[i] == "AUA":
		amino_acids += "ile "
	elif codons[i] == "AUG":
		amino_acids += "met "
	#Second Letter C
	elif codons[i] == "ACU":
		amino_acids += "thr "
	elif codons[i] == "ACC":
		amino_acids += "thr "
	elif codons[i] == "ACA":
		amino_acids += "thr "
	elif codons[i] == "ACG":
		amino_acids += "thr "
	#Second Letter A
	elif codons[i] == "AAU":
		amino_acids += "asn "
	elif codons[i] == "AAC":
		amino_acids += "asn "
	elif codons[i] == "AAA":
		amino_acids += "lys "
	elif codons[i] == "AAG":
		amino_acids += "lys "
	#Second Letter G
	elif codons[i] == "AGU":
		amino_acids += "ser "
	elif codons[i] == "AGC":
		amino_acids += "ser "
	elif codons[i] == "AGA":
		amino_acids += "arg "
	elif codons[i] == "AGG":
		amino_acids += "arg "
	#First Letter G
	#Second Letter U
	elif codons[i] == "GUU":
		amino_acids += "val "
	elif codons[i] == "GUC":
		amino_acids += "val "
	elif codons[i] == "GUA":
		amino_acids += "val "
	elif codons[i] == "GUG":
		amino_acids += "val "
	#Second Letter C
	elif codons[i] == "GCU":
		amino_acids += "ala "
	elif codons[i] == "GCC":
		amino_acids += "ala "
	elif codons[i] == "GCA":
		amino_acids += "ala "
	elif codons[i] == "GCG":
		amino_acids += "ala "
	#Second Letter A
	elif codons[i] == "GAU":
		amino_acids += "asp "
	elif codons[i] == "GAC":
		amino_acids += "asp "
	elif codons[i] == "GAG":
		amino_acids += "glu "
	elif codons[i] == "GAA":
		amino_acids += "glu "
	#Second Letter G
	elif codons[i] == "GG":
		amino_acids += "gly "
	elif codons[i] == "GG":
		amino_acids += "gly "
	elif codons[i] == "GG":
		amino_acids += "gly "
	elif codons[i] == "GG":
		amino_acids += "gly "
		
	i += 1
	
print amino_acids.strip()
