"""Day 4-B: Count k-mers (all overlapping words of length k) in a FASTA file.
Input: FASTA file, optional k (default 3), optional top N (default 10)
Output: the most frequent k-mers with their counts and percentages."""
import sys
from collections import Counter
from day03_fasta_parser import read_fasta

def count_kmers(sequence, k):
    """ Count every overlapping k-mer. Words containing N are skipped."""
    counts = Counter()
    for i in range(len(sequence) -k +1):
        kmer = sequence[i:i + k]
        if set(kmer) <= set("ACGT"):
            counts[kmer] += 1
    return counts

if __name__ == "__main__":
    if len(sys.argv) < 2:
       sys.exit("Usage: python1 day)4_kmer_counter.py <file.fasta> [k] [top]")

    k = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    top = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    records = read_fasta(sys.argv[1])

    total = Counter()
    for sequence in records.values():
        total.update(count_kmers(sequence, k))

    grand_total = sum(total.values())
    if grand_total == 0:
        sys.exit("No k-mers found.Is k larger than the sequences?")
    
    print(f"k = {k} | distinct k-mers: {len(total)} | counted: {grand_total}")
    print(f"{'K-mer':<10} {'Count':>6} {'Freq %':>7}")
    print("-" * 25)
    for kmer, count in total.most_common(top):
        print(f"{kmer:<10} {count:>6} {count / grand_total * 100:>7.2f}")
