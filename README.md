# FakeNews text collections (FKTC)

# FakeNewsTextCollections
Library to use fakenews text collectins

# How To use

!pip install git+https://github.com/GoloMarcos/FKTC/

from FakeNewsTextCollections import datasets

datasets_dictionary = datasets.load()

dataset_dictionaty[base name] return a DataFrame

# Datasets
- Fact Checked News (fcn) : RIBEIRO, V. H. P. Identificação de notícias falsas em língua portuguesa. Monografia (TCC). Universidade Federal de Mato Grosso do Sul, 2019. Citado nas páginas 34 e 96.

- Fake News Net (fnn): Fakenewsnet: A data repository with news content, social context, and spatiotemporal information for studying fake news on social media. Big Data, v. 8, n. 3, p. 171–188, 2020.

- Fake BR (fakebr): MONTEIRO, R.; SANTOS, R.; PARDO, T.; ALMEIDA, T. de; RUIZ, E.; VALE, O. Contributions to the study of fake news in portuguese: New corpus and automatic detection results. In: PROPOR 2018: International Conference on Computational Processing of the Portuguese Language. [S.l.]: Springer, 2018. p. 324–334.

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
