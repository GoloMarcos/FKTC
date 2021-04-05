# FakeNews text collections (FKTC)

# FakeNewsTextCollections
Library to use fakenews text collectins

# How To use

!pip install git+https://github.com/GoloMarcos/FKTC/

from FakeNewsTextCollections import datasets

datasets_dictionary = datasets.load()

dataset_dictionaty[base name] return a DataFrame

# Datasets
- Fake Checked News (fcn)
- Fake (fnn)
- Fake BR (fakebr)

# Columns from DataFrame
- Index 
- Text
- Class
- Folds
- Features
- Features Normalized
- Embedding from BERT
- Embedding from DistilBERT
- Embeddings from Multilingual DistilBERT 
- Embedding from RoBERTa
