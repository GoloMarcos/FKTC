import pandas as pd
import os
from pathlib import Path
from os.path import isfile

def load(path_files=''):

  '''
  this function download and load all datasets and return a dictionary in which any key represent the dataset
  
  if the files already exist, to load them, pass the path where the files are through the path_files parameter
  '''

  if not isfile(path_files + 'fakebr.plk'):
    cmd = 'gdown --id 1TfBnP4-fUsIZtvDKtqXpUb4NvKLS5Kkz -O ' + path_files + 'fakebr.plk'
    os.system(cmd) # FakeBr

  if not isfile(path_files + 'fcn.plk'):
    cmd = 'gdown --id 1-1GRgEOqAl46WX9yVLE6WEyDLtljVz7B -O ' + path_files + 'fcn.plk'
    os.system(cmd) # FCN
  
  if not isfile(path_files + 'fnn.plk'):
    cmd = 'gdown --id 1--GbGtCP3OCExNmdlgU-M7BHa9FMIHaA -O ' + path_files + 'fnn.plk'
    os.system(cmd)  # FNN

  bases = {
    'fcn' : pd.read_pickle(path_files + 'fcn.plk'),
    'fakebr' : pd.read_pickle(path_files + 'fakebr.plk'),
    'fnn' : pd.read_pickle(path_files + 'fnn.plk')
  }

  return bases
