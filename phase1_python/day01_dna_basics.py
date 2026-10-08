"""Day 1-B: Basic statistics of a DNA sequence.
Input: DNA string (edit below or pass as argument) | Output: printed summary"""

import sys
dna =sys.argv[1].upper() if len(sys.argv) > 1 else "ATGCGTACGTTAGCCGATAGCTAGCTAGGCTA"

#Validate : only A, T, G, C
invalid = set(dna) - set("ATGC")
if invalid:
    sys.exit (f"Invalid characters in sequence: {invalid}")
length = len(dna)
counts = {base: dna.count(base) for base in "ATGC"}
gc_percent = (counts ["G"] +counts["C"])/length*100

print (f"sequence : {dna}")
print (f"length : {length} bp")
for base, n in counts.items():
  print (f"{base}:{n} ({n/length*100:.1f}%)")
print (f"GC content: {gc_percent:.2f}%")
