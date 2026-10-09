"""Day 2-A: DNA toolkit - validate, complement, reverse complement, transcribe.
Input: DNA string (argument or default) | Output: printed results
These functions are reused on later days, so keep this file."""
import sys

COMPLEMENT = {"A": "T", "T": "A", "G": "C", "C": "G"}


def validate(dna):
    """Return the sequence in capitals, or stop if it has letters other than A, T, G, C."""
    dna = dna.upper()
    invalid = set(dna) - set("ATGC")
    if invalid:
        sys.exit(f"Invalid characters in sequence: {invalid}")
    return dna


def complement(dna):
    """Swap each base for its partner: A<->T, G<->C."""
    return "".join(COMPLEMENT[base] for base in dna)


def reverse_complement(dna):
    """The opposite strand, read 5' to 3'."""
    return complement(dna)[::-1]


def transcribe(dna):
    """DNA coding strand -> mRNA: replace T with U."""
    return dna.replace("T", "U")


if __name__ == "__main__":
    seq = validate(sys.argv[1] if len(sys.argv) > 1 else "ATGCGTACGTTAGC")
    print(f"DNA (5'->3')        : {seq}")
    print(f"Complement (3'->5') : {complement(seq)}")
    print(f"Reverse complement  : {reverse_complement(seq)}")
    print(f"mRNA                : {transcribe(seq)}")
