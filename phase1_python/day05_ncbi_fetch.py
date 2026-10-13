"""Day 5-B: Download a GenBank record from NCBI with Entrez and summarise it.
Input: an accession (e.g. NM_000546, human TP53 mRNA) and your e-mail address
Output: a summary on screen, plus the record saved as GenBank and FASTA files."""
import os 
import sys
import truststore
truststore.inject_into_ssl()
from Bio import Entrez, SeqIO

def fetch_record(accession, email):
    """Download one nucleotide record from NCBI and return it as a SeqRecord."""
    Entrez.email = email
    handle = Entrez.efetch(db="nucleotide", id=accession, rettype="gb", retmode="text")
    record = SeqIO.read(handle, "genbank")
    handle.close()
    return record

def summarise(record):
    """Print the main facts about a GenBank record."""
    print(f"Accession   : {record.id}")
    print(f"Description : {record.description}")
    print(f"Organism     : {record.annotations.get('organism', 'unknown')}")
    print(f"Length       : {len(record.seq)} bp")
    print(f"Features     : {len(record.features)}")
    for feature in record.features:
        if feature.type == "CDS":
            protein = feature.qualifiers.get("gene", ["?"])[0]
            gene = feature.qualifiers.get("gene", ["?"])[0]
            start = int(feature.location.start) + 1
            end = int(feature.location.end)
            print(f"CDS          : gene {gene}, positions {start}-{end}, {len(protein)} amino acids")
            print(f"Protein      : {protein[:30]}...")
            break

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("Usage: python3 day05_ncbi_fetch.py <accession> <your_email>")

    try:
        record = fetch_record(sys.argv[1], sys.argv[2])
    except Exception as error:
        sys.exit(f"Could not download the record: {error}")

    summarise(record)
    os.makedirs("data", exist_ok=True)
    SeqIO.write(record, f"data/{record.id}.gb", "genbank")
    SeqIO.write(record, f"data/{record.id}.fasta", "fasta")
    print(f"Saved data/{record.id}.gb and data/{record.id}.fasta")
