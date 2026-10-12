"""Day 4-A: Find open reading frames (ORFs) in all six reading frames.
Input: FASTA file and optional minimum protein length (default 10)
Output: one line per ORF with strand, frame, DNA start/end and protein."""
import sys
from day02_translate import CODON_TABLE
from day03_fasta_parser import read_fasta

COMPLEMENT = str.maketrans("ACGTN", "TGCAN")

def find_orfs(dna, min_aa=10):
    """Return a list of ORFs as (strand, frame, start, end, protein). An ORF runs from an ATG to the next stop codon. Start and end are 1-based positions on the original sequence."""
    orfs = []
    length =len(dna)
    for strand, seq in (("+", dna), ("-", dna.translate(COMPLEMENT)[::-1])):
        for frame in range(3):
            start = None
            protein = ""
            for i in range(frame, length - 2, 3):
                codon = seq[i:i + 3]
                amino_acid = CODON_TABLE.get(codon, "X")
                if start is None:
                    if codon == "ATG":
                        start = i
                        protein = "M"
                elif amino_acid == "*":
                    if len(protein) >= min_aa:
                        end = i+3
                        if strand == "+":
                            orfs.append((strand, frame + 1, start + 1, end, protein))
                        else:
                            orfs.append((strand, frame +1, length - end + 1, length - start, protein))
                    start = None
                    protein = ""
                else:
                    protein += amino_acid
    return orfs
if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: python3 day04_orf_finder.py <file.fasta> [min_aa]")

    min_aa = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    records = read_fasta(sys.argv[1])

    print(f"{'ID':<8} {'Strand':>6} {'Frame':>5} {'Start':>6} {'End':>6} {'AA':>4} Protein")
    found = 0
    for seq_id, dna in records.items():
        for strand, frame, start, end, protein in find_orfs(dna, min_aa):
            preview = protein if len(protein) <= 20 else protein[:20] + "..."
            print(f"{seq_id:<8} {strand:>6} {frame:>5} {start:>6} {end:>6} {len(protein):>4}  {preview}")
            found += 1
    print(f"ORFs found (at least {min_aa} aa): {found}")

