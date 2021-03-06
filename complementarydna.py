"""
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

If you want to know more http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

More similar exercise are found here http://rosalind.info/problems/list-view/ (source)

DNA_strand ("ATTGC") # return "TAACG"

DNA_strand ("GTAT") # return "CATA"

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TESTS:

Test.assert_equals(DNA_strand("AAAA"),"TTTT","String AAAA is")
Test.assert_equals(DNA_strand("ATTGC"),"TAACG","String ATTGC is")
Test.assert_equals(DNA_strand("GTAT"),"CATA","String GTAT is")

"""

def DNA_strand(dna):
	new_dna = []
	for each_item in dna:
		if each_item == "A":
			new_dna.append("T")
		elif each_item == "T":
			new_dna.append("A")
		elif each_item == "C":
			new_dna.append("G")
		else:
			new_dna.append("C")
	else:
		return "".join(new_dna)

if __name__ == "__main__":
	print(DNA_strand("AAAA"))
	print(DNA_strand("ATTGC"))
	print(DNA_strand("GTAT"))