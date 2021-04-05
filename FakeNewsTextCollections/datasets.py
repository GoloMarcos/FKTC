import pandas as pd
import os
from pathlib import Path

def load(path_files=''):

  '''
  this function download and load all datasets and return a dictionary in which any key represent the dataset
  
  if the files already exist, to load them, pass the path where the files are through the path_files parameter
  
  this function changes the current directory, remember to go back to the directory you were in
  '''

  if path_files != '':
    os.chdir(path_files)

  if not Path('fakebr.plk').is_file():
    os.system('gdown --id 1TfBnP4-fUsIZtvDKtqXpUb4NvKLS5Kkz') # FakeBr

  if not Path('fcn.plk').is_file():
    os.system('gdown --id 1-1GRgEOqAl46WX9yVLE6WEyDLtljVz7B') # FCN
  
  if not Path('fnn.plk').is_file():
    os.system('gdown --id 1--GbGtCP3OCExNmdlgU-M7BHa9FMIHaA')  # FNN

  bases = {
    'fcn' : pd.read_pickle('fcn.plk'),
    'fakebr' : pd.read_pickle('fakebr.plk'),
    'fnn' : pd.read_pickle('fnn.plk')
  }

  return bases