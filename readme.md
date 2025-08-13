Files Structure

sample.json - Sample JSON file with raw document data
index.py - Pure Python implementation for data transformation
utils.pyx - Cython implementation of text normalization function
ython.py - Document processor using Cython functions
setup.py - Build configuration for Cython compilation

Setup Instructions
1. Install Dependencies
```bash 
pip install cython
```

2. Compile Cython Module
```bash
python setup.py build_ext --inplace
```

3. Run the Scripts

Pure Python version:
```bash
python index_python.py
```
Cython version:
```bash
python index_cython.py
```