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
    return read_dataset('student.csv')


def students():
    return read_dataset('students.csv')
    

def programs():
    return read_dataset('programs.csv')      #TODO change programs-data.csv contents with the original ones.

def courses():
    return read_dataset('courses.csv')


def final(unitid):
    return read_dataset('final.csv')
