# Fake News Text Collections (FNTC)
Library to use fakenews text collections

# How To use

!pip install git+https://github.com/GoloMarcos/FKTC/

from FakeNewsTextCollections import datasets

datasets_dictionary = datasets.load()

dataset_dictionaty[base name] return a DataFrame

# Datasets
- **Fact Checked News (fcn)** : RIBEIRO, V. H. P. Identificação de notícias falsas em língua portuguesa. Monografia (TCC). Universidade Federal de Mato Grosso do Sul, 2019.

- **Fake News Net (fnn)** : Fakenewsnet: A data repository with news content, social context, and spatiotemporal information for studying fake news on social media. Big Data, v. 8, n. 3, p. 171–188, 2020.

- **Fake BR (fakebr)** : MONTEIRO, R.; SANTOS, R.; PARDO, T.; ALMEIDA, T. de; RUIZ, E.; VALE, O. Contributions to the study of fake news in portuguese: New corpus and automatic detection results. In: PROPOR 2018: International Conference on Computational Processing of the Portuguese Language. [S.l.]: Springer, 2018. p. 324–334.

- **Fake News Corpus 0 (fnc0)** : collection derived from https://github.com/several27/FakeNewsCorpus

- **Fake News Corpus 1 (fnc1)** : collection derived from https://github.com/several27/FakeNewsCorpus

- **Fake News Corpus 2 (fnc2)** : collection derived from https://github.com/several27/FakeNewsCorpus

# Datasets Characteristics

| - | fcn | fnn | fakebr | fnc0 | fnc1 | fnc2 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Language | pt | pt | en | en | en | en |
| Fake News | 1,044 | 3,598 | 1,705 | 3,000 | 3,000 | 3,000 |
| Real News | 1,020 | 3,598 | 5,298 | 3,000 | 3,000 | 3,000 |
| Total News | 2,064 | 7,196 | 7,003 | 3,000 | 3,000 | 3,000 |

# Columns from DataFrame
- **index**: id
- **text**: content of the news
- **class**: fake (1) | real (-1)
- **folds**: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
- **features**: 63 features extracted using Linguistic Inquiry and Word Count (LIWC)
- **features_normalized**: 63 features with normalization extracted using LIWC
- **BERT**: embedding with 1024 real values
- **DistilBERT**: embedding with 512 real values
- **Multilingual DistilBERT**: embedding with 512 real values
- **RoBERTa**: embedding with 724 real values


# Linguistic Inquiry and Word Count (LIWC)
- Pennebaker, James W., et al. The development and psychometric properties of LIWC2015. 2015.

# We obtain the embeddings with the library sentence_tranformers (v==1.0.4) (https://www.sbert.net/)
- **BERT model**: bert-large-nli-stsb-mean-tokens
  -  Devlin, Jacob, et al. "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding." Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers). 2019.
- **DistilBERT model**: distilbert-base-nli-stsb-mean-tokens
  -  Sanh, Victor, et al. "DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter." arXiv preprint arXiv:1910.01108 (2019).
- **RoBERTa model**: roberta-large-nli-stsb-mean-tokens
  - Liu, Zhuang, et al. "A Robustly Optimized BERT Pre-training Approach with Post-training." China National Conference on Chinese Computational Linguistics. Springer, Cham, 2021.
- **DistilBERT Multilingual model**: distiluse-base-multilingual-cased
  - Reimers, Nils, and Iryna Gurevych. "Making Monolingual Sentence Embeddings Multilingual Using Knowledge Distillation." Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP). 2020.
