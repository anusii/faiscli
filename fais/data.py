import pandas as pd
import io


def student(uid):
    data1 = """Course,Description,Sem/Year,Enrol.,Status,Grade,Final,Comment,Sp
COMP7230,Programming for Data Scientists,Sum/2021,details,,D,74,,Sp
COMP6240,Relational Databases,S2/2021,details,,CR,62,,Sp
COMP2700,Cyber Security Fundamentals,S2/2021,details,,HD,89,,SP
COMP4550,Advanced Computing Research Project,S2/2021,details,,KU,0,,Sp
COMP3600,Algorithms,S2/2021,details,,CR,61,,Sp
COMP2400,Relational Databases,S2/2021,details,UN,,0,,Sp
COMP3310,Computer Networks,S1/2021,details,,CR,61,,Sp
COMP4450,Advanced Computing Research Methods,S1/2021,details,,D,72,,Sp
"""
    data2 = """Course,Description,Sem/Year,Enrol.,Status,Grade,Final,Comment,Sp
COMP8410,Data Mining,Win/2021,details,,NCN,30,,Sp
COMP8430,Data Wrangling,Sum/2021,details,,PS,50,,Sp
COMP8410,Data Mining,S1/2021,details,UN,,,,Sp
COMP8430,Data Wrangling,S2/2020,details,UN,,,,Sp
COMP6730,Programming for Scientists,S1/2020,details,,PS,50,,Sp
COMP7240,Introduction to Database Concepts,Aut/2020,details,,CR,61,,Sp
COMP6730,Programming for Scientists,S1/2019,details,,N,28,,Sp
"""
    data = data2
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
    data1 = """Unitid,Course,Description,Sem/Year
12886,COMP7230,Programming for Data Scientists,Sum/2021
12715,COMP6240,Relational Databases,S2/2021
12252,COMP2700,Cyber Security Fundamentals,S2/2021
11960,COMP4550,Advanced Computing Research Project,S2/2021
12887,COMP3600,Algorithms,S2/2021
12716,COMP2400,Relational Databases,S2/2021
12253,COMP3310,Computer Networks,S1/2021
11961,COMP4450,Advanced Computing Research Methods,S1/2021
    """
    data2 = """Unitid,Course,Description,Sem/Year
12886,COMP8410,Data Mining,Win/2021
12886,COMP8430,Data Wrangling,Sum/2021
12886,COMP8410,Data Mining,S1/2021
12886,COMP8430,Data Wrangling,S2/2020
12886,COMP6730,Programming for Scientists,S1/2020
12886,COMP7240,Introduction to Database Concepts,Aut/2020
12886,COMP6730,Programming for Scientists,S1/2019
    """
    data = data2
    with io.StringIO(data) as f:
        df = pd.read_csv(f)
    return(df)


def final(unitid):
    data = """Student,Fore/Last Names,Degree,Ass1,Ass2,Ass3,Ass4,FinalExam,\
Quiz1,Quiz2,Quiz3,Wattle,New Mark,New Grade,FAIS Mark,FAIS Grade,Seq.,Sp
u1234567,Mary Smithers,InfTech,9.10,10.95,19.00,none,44.38,4.00,4.50,5.00,\
none, , ,92,HD,21,
u1234568,Howard Miller,InfTech,8.23,11.50,17.50,none,34.25,5.00,2.75,2.00,\
none, , ,87,HD,63,
u1234569,Sally Meakiner,BADAN,3.22,12.00,11.00,none,35.90,4.00,4.50,4.00,\
none, , ,81,HD,36,
    """

    with io.StringIO(data) as f:
        df = pd.read_csv(f)
    return(df)
