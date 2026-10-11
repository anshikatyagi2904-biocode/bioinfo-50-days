"""Day 3-B: Statistics for every sequence in a FASTA file.
Input: path to a FASTA file | Output: table of length and GC% per record,
plus a summary with total length, longest, shortest, mean length and N50."""
import sys
from day03_fasta_parser import read_fasta

def gc_content(sequence):
    valid = sum(sequence.count(base) for base in "ACGT")
    if valid == 0:
        return 0.0
    gc = sequence.count("G") + sequence.count("C")
    return gc / valid * 100

def n50(lengths):
    """Sort lengths from longest to shortest and add them up. N50  is the length at which the running total first reaches half of the grand total."""
    total = sum(lengths)
    running = 0
    for length in sorted(lengths, reverse=True):
        running += length
        if running >= total/2:
            return length
    return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
       sys.exit("Usage: python3 day03_fasta_stats.py <file.fasta>")

    records = read_fasta(sys.argv[1])
    if not records:
        sys.exit("No sequences found in the file.")

    print (f"{'ID':<8} {'Length':>7} {'GC%':>7} {'N count':>8}")
    print("-" * 33)
    lengths = []
    for seq_id, sequence in records.items():
        lengths.append(len(sequence))
        print(f"{seq_id:<8} {len(sequence):>7} {gc_content(sequence):>7.2f} {sequence.count('N'):>8}")
          
   
    print("-" * 33)
    print(f"Records       : {len(lengths)}")
    print(f"Total length  : {sum(lengths)} bp")
    print(f"Longest       : {max(lengths)} bp")
    print(f"Shortest      : {min(lengths)} bp")
    print(f"Mean length   : {sum(lengths) / len(lengths):.1f} bp")
    print(f"N50           : {n50(lengths)} bp")
