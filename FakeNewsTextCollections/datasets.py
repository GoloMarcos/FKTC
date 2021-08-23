import pandas as pd
import os
from os.path import isdir, isfile
from pathlib import Path

def load(path_files='', only_download = False, dataset = 'All'):

  '''
  this function download and load all datasets, and return a dictionary in which any key represent the dataset
  
  if the directory already exist, to load them, pass the path where the directory are through the path_files parameter
  
  '''
  if not isdir(path_files + 'News/'):
    if not isfile(path_files + 'News.zip'):
      print('Download News.zip')
      cmd = 'gdown --id -O 14myhLA6c-T2wsf8Q8wkSGq2kbTvRAdF4' + path_files + 'News.zip'
      print(cmd)
      os.system(cmd)
      print('Download Finished!')
      
    cmd2 = 'unzip ' + path_files + 'News.zip'
    print('Unzip News.zip')
    os.system(cmd2)
    print('Unzip Finished!')
    
  if not only_download:
    if dataset == 'All':
      basepath = Path(path_files + 'News/')
      files_in_basepath = basepath.iterdir()
      datasets = {}
      for item in files_in_basepath:
        if item.is_file():
          df = pd.read_pickle(path_files + 'News/' + item.name)
          datasets[item.name.replace('.plk','')] = df
    
    else:
      datasets = {}
      datasets[dataset] = pd.read_pickle(path_files + 'News/' + dataset + '.plk')

    return datasets
