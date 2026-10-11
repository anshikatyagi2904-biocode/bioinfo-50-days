"""Day 3-A: Read a FASTA file into a dictionary {sequence id: sequence}.
Input: path to a FASTA file | Output: records printed with length and preview
read_fasta() is reused on later days, so keep this file."""
import sys
 
def read_fasta(path):
    """Read a FASTA file and return a dictionary {id: sequence}.
    The id is the first word after '>'. Sequences are joined into one
    capital-letter string, even when they span several lines."""
    records = {}
    current_id = None
    pieces = []
    
    with open(path) as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if current_id is not None:
                    records[current_id] = "".join(pieces).upper()
                current_id = line[1:].split()[0]
                pieces = []
            else:
                 pieces.append(line)

    if current_id is not None:
        records[current_id] = "".join(pieces).upper()
    return records

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: python3 day03_fasta_parser.py <file.fasta>")

    records = read_fasta(sys.argv[1])
    print(f"Records found: {len(records)}")
    for seq_id, sequence in records.items():
        print(f"{seq_id:<8} {len(sequence):5} bp {sequence[:30]}")
