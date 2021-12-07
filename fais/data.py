import pandas as pd
import io


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
