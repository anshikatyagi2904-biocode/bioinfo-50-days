"""Day 2-B: Translate a DNA coding sequence into a protein.
Input: DNA string (argument or default) | Output: codons and protein"""
import sys
# The standard genetic code. Codons are built from bases in the order T, C, A, g.
# The 64 amino acids below line up with the 64 codons TTT, TTC, TTA, TTG, TCT, ...
# "*" means a STOP codon.
BASES ="TCAG"
AMINO_ACIDS = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
CODONS = [a + b + c for a in BASES for b in BASES for c in BASES]
CODON_TABLE = dict(zip(CODONS, AMINO_ACIDS))
def translate(dna):
    """Read the sequence three bases at a time, starting at position 0.
    Stops at the first stop codon. returns the protein string."""
    protein = ""
    for i in range(0, len(dna) -2,3):
        codon = dna[i:i +3]
        amino_acid = CODON_TABLE[codon]
        if amino_acid == "*":
            break   
        protein += amino_acid 
    return protein
if __name__ == "__main__":
    dna = (sys.argv[1] if len(sys.argv) >1 else "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG").upper()
    invalid = set(dna) - set("ATGC")
    if invalid: 
        sys.exit(f"Invalid characters in sequence: {invalid}")
    codons = [dna[i:i + 3] for i in range(0, len(dna) - 2, 3)]
    print(f"DNA     : {dna}")
    print(f"Codons : {' '.join(codons)}")
    print(f"Protein : { translate(dna)}")
    print(f"length : {len(translate(dna))} amino acids")
