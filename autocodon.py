#Automatic Codon Chart
#Author: Carter Turnbaugh
#Last Modified: 5/25/2015

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

codontoaa = {'UUU':'phe' , 'UUC':'phe' , 'UUA':'leu' , 'UUG':'leu' , 'UCU':'ser' , 'UCC':'ser' , 'UCA':'ser' , 'UCG':'ser' , 'UAU':'tyr' , 'UAC':'tyr' , 'UAA':'stop' , 'UAG':'stop' , 'UGU':'cys' , 'UGC':'cys' , 'UGA':'stop' , 'UGG':'trp' , 'CUU':'leu' , 'CUC':'leu' , 'CUA':'leu' , 'CUG':'leu' , 'CCU':'pro' , 'CCC':'pro' , 'CCA':'pro' , 'CCG':'pro' , 'CAU':'his' , 'CAC':'his' , 'CAA':'gin' , 'CAG':'gin' , 'CGU':'arg' , 'CGC':'arg' , 'CGA':'arg' , 'CGG':'arg' , 'AUU':'ile' , 'AUC':'ile' , 'AUA':'ile' , 'AUG':'met' , 'ACU':'thr' , 'ACC':'thr' , 'ACA':'thr' , 'ACG':'thr' , 'AAU':'asn' , 'AAC':'asn' , 'AAA':'lys' , 'AAG':'lys' , 'AGU':'ser' , 'AGC':'ser' , 'AGA':'arg' , 'AGG':'arg' , 'GUU':'val' , 'GUC':'val' , 'GUA':'val' , 'GUG':'val' , 'GCU':'ala' , 'GCC':'ala' , 'GCA':'ala' , 'GCG':'ala' , 'GAU':'asp' , 'GAC':'asp' , 'GAG':'glu' , 'GAA':'glu' , 'GGU':'gly' , 'GGC':'gly' , 'GGG':'gly' , 'GGA':'gly'}

i = 0
length = len(codons)
while i < length:
	
	amino_acids += codontoaa[codons[i]] + " "
		
	i += 1
	
print amino_acids.strip()
