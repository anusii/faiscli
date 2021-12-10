import pandas as pd
import io


def student(uid):
    data = """Course,Description,Sem/Year,Enrol.,Status,Grade,Final,Comment,Sp
COMP7230,Programming for Data Scientists,Sum/2021,details,,D,74,,Sp
COMP6240,Relational Databases,S2/2021,details,,CR,62,,Sp
COMP2700,Cyber Security Fundamentals,S2/2021,details,,HD,89,,SP
COMP4550,Advanced Computing Research Project,S2/2021,details,,KU,0,,Sp
COMP3600,Algorithms,S2/2021,details,,CR,61,,Sp
COMP2400,Relational Databases,S2/2021,details,UN,,0,,Sp
COMP3310,Computer Networks,S1/2021,details,,CR,61,,Sp
COMP4450,Advanced Computing Research Methods,S1/2021,details,,D,72,,Sp
"""
    with io.StringIO(data) as f:
        df = pd.read_csv(f)
    return(df)


def students():
    data = """Student ID,Fore/Last name(s),Initial(s),Degree
u1234567,Deshayla Chaniah,,MADAN
u1234568,Adelya Lilias,,InfTech
u1234569,Myiesha Quillian,,Engineer
u1234560,Sailee Darsy,,FDD Eng. & Adv. Comp.
u1234561,Artia Jaysson,,BPPE
u1234562,Kyniah Avontae,,FDD Eng. & Adv. Comp.
u1234570,Adabella Sheryce,,Engineer
u1234571,Ludy Shalva,,CADAN
u6543432,Xyriah Barris,,
u4546332,Yangqi Yu,,BIT
u7543364,Norden,,MADAN
u4323445,Alexander Watt,,BA/BSc
"""
    with io.StringIO(data) as f:
        df = pd.read_csv(f)
    return(df)

def courses():
    data = """Unitid,Course,Description,Sem/Year
12886,COMP7230,Programming for Data Scientists,Sum/2021
12715,COMP6240,Relational Databases,S2/2021
12252,COMP2700,Cyber Security Fundamentals,S2/2021
11960,COMP4550,Advanced Computing Research Project,S2/2021
12887,COMP3600,Algorithms,S2/2021
12716,COMP2400,Relational Databases,S2/2021
12253,COMP3310,Computer Networks,S1/2021
11961,COMP4450,Advanced Computing Research Methods,S1/2021
    """
    with io.StringIO(data) as f:
        df = pd.read_csv(f)
    return(df)
