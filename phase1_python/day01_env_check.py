"""Day 1-A: Check that the Python environment is ready.
Input: none | Output: printed versions"""
import sys

print(f"Python: {sys.version.split()[0]}")

for pkg in ["numpy", "pandas", "matplotlib", "Bio"]:
    try:
        module = __import__(pkg)
        print(f"{pkg}: OK (version {getattr(module, '__version__', 'n/a')})")
    except ImportError:
        print(f"{pkg}: MISSING -> run: pip3 install numpy pandas matplotlib biopython")
