import pandas as pd


def read_dataset(f):
    folder_name = 'dataset/'
    df = pd.read_csv(f'./{folder_name}{f}')
    return (df)


def student(uid):
    """
    CSV filenames to be used here start with
    the respective function name. Here- function name 
    is "student" hence, corresponding csv files to choose
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
    return read_dataset('programs-data.csv')

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

