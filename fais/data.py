import pandas as pd


def read_data_csv(f):
    # folder_name = 'dataset/'
    df = pd.read_csv(f)
    return (df)


def student(uid):
    return read_data_csv('./dataset/student-data2.csv')


def students():
    return read_data_csv('./dataset/students-data.csv')
    

def courses():
    return read_data_csv('./dataset/courses-actual.csv')


def final(unitid):
    return read_data_csv('./dataset/final-data.csv')

