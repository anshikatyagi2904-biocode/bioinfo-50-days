"""Day 5-A: Biopython SeqIO basics - read, filter and write a FASTA file.
Input: FASTA file, optional minimum length (default 30), optional output file
Output: a table of every record and a new FASTA file with the records kept."""
import os
import sys
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("USage: python3 day05_seqio_basics.py <file.fasta> [min_length] [out.fasta]")

    min_length = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    out_path = sys.argv[3] if len(sys.argv) > 3 else "results/filtered.fasta"

    kept = []
    total = 0
    print(f"{'ID':<8} {'Length':>7} {'GC%' :>7} Decision")
    print("-" * 33)
    for record in SeqIO.parse(sys.argv[1], "fasta"):
        total += 1
        gc = gc_fraction(record.seq) * 100
        keep = len(record.seq) >= min_length
        print(f"{record.id:<8} {len(record.seq):>7} {gc:>7.2f} {'keep' if keep else 'too short'}")
        if keep:
            kept.append(record)
    
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    count = SeqIO.write(kept, out_path, "fasta")
    print("-" * 33)
    print(f"Kept {count} of {total} records (minimum length {min_length} bp)")
    print(f"written to {out_path}")
    if kept: 
        first = kept[0]
        print(f"{first.id} reverse complement: {first.seq.reverse_complement()[:30]}...")

