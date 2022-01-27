import os
import fais
import inspect

import pandas as pd

# Determine package install location and assume data
# available there! TODO Need to orchestrate this for
# package install -through pip3 - currently works with
# pip install -e .

PKG = os.path.dirname(inspect.getfile(fais))
DATA = os.path.join(PKG, 'dataset')


def read_dataset(f):
    PATH = os.path.join(DATA, f)
    df = pd.read_csv(PATH)
    return (df)


def student(uid):
    """
    CSV filenames to be used here start with
    the respective function name. Function name here
    is "student", hence the corresponding csv files to choose
    from the "dataset/" folder are: -
    1. "student-data1.csv"
    2. "student-data2.csv"
    """
    return read_dataset('student-data2.csv')


def students():
    """
    Respective csv data files to choose from:
    1. students-data.csv
    """
    return read_dataset('students-data.csv')
    

def programs():
    """
    Respective csv data files to choose from:
    1. programs-data.csv
    """
    return read_dataset('programs-data.csv')      #TODO change programs-data.csv contents with the original ones.

def courses():
    """
    Respective csv data files to choose from:
    1. courses-data1.csv
    2. courses-data2.csv
    3. courses-actual.csv
    """
    return read_dataset('courses-actual.csv')


def final(unitid):
    """
    Respective csv data files to choose from:
    1. final-data.csv
    """
    return read_dataset('final-data.csv')
