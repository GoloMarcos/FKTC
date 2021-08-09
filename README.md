# FakeNews text collections (FKTC)

# FakeNewsTextCollections
Library to use fakenews text collections

# How To use

!pip install git+https://github.com/GoloMarcos/FKTC/

from FakeNewsTextCollections import datasets

datasets_dictionary = datasets.load()

dataset_dictionaty[base name] return a DataFrame

# Datasets
- Fact Checked News (fcn) : RIBEIRO, V. H. P. Identificação de notícias falsas em língua portuguesa. Monografia (TCC). Universidade Federal de Mato Grosso do Sul, 2019.

- Fake News Net (fnn): Fakenewsnet: A data repository with news content, social context, and spatiotemporal information for studying fake news on social media. Big Data, v. 8, n. 3, p. 171–188, 2020.

- Fake BR (fakebr): MONTEIRO, R.; SANTOS, R.; PARDO, T.; ALMEIDA, T. de; RUIZ, E.; VALE, O. Contributions to the study of fake news in portuguese: New corpus and automatic detection results. In: PROPOR 2018: International Conference on Computational Processing of the Portuguese Language. [S.l.]: Springer, 2018. p. 324–334.

# Columns from DataFrame
- Index 
- Text
- Class
- Folds
- Features from LIWC
- Features Normalized from LIWC
- Embedding from BERT
- Embedding from DistilBERT
- Embeddings from Multilingual DistilBERT 
- Embedding from RoBERTa

# We obtain the embeddings with the library sentence_tranformers
- BERT model: bert-large-nli-stsb-mean-tokens
  -  Devlin, Jacob, et al. "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding." Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers). 2019.
- DistilBERT model: distilbert-base-nli-stsb-mean-tokens
  -  Sanh, Victor, et al. "DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter." arXiv preprint arXiv:1910.01108 (2019).
- RoBERTa model: roberta-large-nli-stsb-mean-tokens
  - Liu, Yinhan, et al. "Roberta: A robustly optimized bert pretraining approach." arXiv preprint arXiv:1907.11692 (2019).
- DistilBERT Multilingual model: distiluse-base-multilingual-cased
  - Sanh, Victor, et al. "DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter." arXiv preprint arXiv:1910.01108 (2019).
