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
COMP3600,Algorithms,S2/2021,details,,CR,61,,Sp
COMP2400,Relational Databases,S2/2021,details,UN,,0,,Sp
COMP8410,Data Mining,Win/2021,details,,NCN,,,Sp
COMP8430,Data Wrangling,S1/2021,details,,PS,50,,Sp
COMP3310,Computer Networks,S1/2021,details,,CR,61,,Sp
COMP4450,Advanced Computing Research Methods,S1/2021,details,,D,72,,Sp
COMP8410,Data Mining,S1/2021,details,UN,,,,Sp
COMP7230,Programming for Data Scientists,Sum/2021,details,,D,74,,Sp
COMP6240,Relational Databases,Win/2020,details,,CR,62,,Sp
COMP2700,Cyber Security Fundamentals,S2/2020,details,,HD,89,,SP
COMP4550,Advanced Computing Research Project,S2/2020,details,,KU,0,,Sp
COMP8430,Data Wrangling,S1/2020,details,UN,,,,Sp
COMP6730,Programming for Scientists,S1/2020,details,,PS,50,,Sp
COMP7240,Introduction to Database Concepts,S1/2020,details,,HD,100,,Sp
COMP6730,Programming for Scientists,S1/2020,details,,N,28,,Sp
"""
    data = data2
    with io.StringIO(data) as f:
        df = pd.read_csv(f)
    return(df)


def students():
    data = """Student ID,Fore/Last name(s),Initial(s),Degree
u1234567,Deshayla Frederica Chaniah,,MADAN
u1234568,Adelya Lilias,,InfTech
u1234569,Myiesha Quillian,,Engineer
u1234560,Sailee Darsy,,FDD Eng. & Adv. Comp.
u1234561,Adelya Jaysson,,BPPE
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
12886,COMP7230,Programming for Data Scientists,Sum/2021
12715,COMP6240,Relational Databases,S2/2021
12252,COMP2700,Cyber Security Fundamentals,S2/2021
11960,COMP4550,Advanced Computing Research Project,S2/2021
12887,COMP3600,Algorithms,S2/2021
12716,COMP2400,Relational Databases,S2/2021
12253,COMP3310,Computer Networks,S1/2021
11961,COMP4450,Advanced Computing Research Methods,S1/2021
12886,COMP8410,Data Mining,Win/2021
12886,COMP8430,Data Wrangling,Sum/2021
12886,COMP8410,Data Mining,S1/2021
12886,COMP8430,Data Wrangling,S2/2020
12886,COMP6730,Programming for Scientists,S1/2020
12886,COMP7240,Introduction to Database Concepts,Aut/2020
12886,COMP6730,Programming for Scientists,S1/2019
    """
    # 20220114 Dump from `fais courses` = 2090 lines
    # Need quotes around the description column.
    actual = """Unitid,Course,Description,Sem/Year
13157,COMP8539,Advvanced Topics in Computer Vision,S2/2022
13156,ENGN8536,Adv Topics in Mechatronics Systems,S2/2022
13155,COMP8536,Advanced Topics in Deep Learning for Computer Vision,S2/2022
13154,COMP4610,Computer Graphics,S2/2022
13153,COMP6461,Computer Graphics,S2/2022
13152,COMP8880,Computational Methods for Network Science,S2/2022
13151,COMP8830,Computer Internship,S2/2022
13150,COMP8800,Computing Research Project,S2/2022
13149,COMP8755,Individual Computing Project,S2/2022
13148,COMP8715,Computing Project,S2/2022
13147,COMP8670,Advanced Topics in Logic and Computation,S2/2022
13146,COMP8650,Advanced Topics in Machine Learning,S2/2022
13145,COMP8620,Advanced Topics in Artificial Intelligence,S2/2022
13144,COMP6490,Document Analysis,S2/2022
13143,COMP6466,Algorithms,S2/2022
13142,COMP6464,High Performance Scientific Computation,S2/2022
13141,COMP6442,Software Construction,S2/2022
13140,COMP6390,HCI Human-Computer Interaction,S2/2022
13139,COMP6361,Principles of Programming Languages,S2/2022
13138,COMP6330,Operating Systems Implementation,S2/2022
13137,COMP6310,"Systems, Networks and Concurrency",S2/2022
13136,COMP6261,Information Theory,S2/2022
13135,COMP6260,Foundations of Computing,S2/2022
13134,COMP6240,Relational Databases,S2/2022
13133,COMP6120,Software Engineering,S2/2022
13132,COMP4880,Computational Methods for Network Science,S2/2022
13131,COMP4680,Advanced Topics in Statistical Machine Learning,S2/2022
13130,COMP4650,Document Analysis,S2/2022
13129,COMP4630,Overview of Logic and Computation,S2/2022
13128,COMP4620,Advanced Topics in Artificial Intelligence,S2/2022
13127,COMP4560,Advanced Computing Project,S2/2022
13126,COMP4550,Advanced Computing Research Project,S2/2022
13125,COMP4540,Software Engineering Research Project,S2/2022
13124,COMP8430,Data Wrangling,S2/2022
13123,COMP4500,Software Engineering Practice,S2/2022
13122,COMP8200,Master of Computing Honours Results,S2/2022
13121,COMP7230,Introduction to Programming for Data Scientists,Win/2022
13120,COMP6780,Web Development and Design,S2/2022
13119,COMP6730,Programming for Scientists,S2/2022
13118,COMP6720,Art and Interaction Computing,S2/2022
13117,COMP6710,Structured Programming,S2/2022
13116,COMP6670,Introduction to Machine Learning,S2/2022
13115,COMP8410,Data Mining,Win/2022
13114,COMP3670,Introduction to Machine Learning,S2/2022
13113,COMP3610,Principles of Programming Languages,S2/2022
13112,COMP3600,Algorithms,S2/2022
13111,COMP3550,Advanced Computing R&amp;D Project,S2/2022
13110,COMP3500,Software Engineering Project (Part B),S2/2022
13109,COMP3430,Data Wrangling,S2/2022
13108,COMP3320,High Performance Scientific Computation,S2/2022
13107,COMP3300,Operating Systems Implementation,S2/2022
13106,COMP2700,Cyber Security Fundamentals,S2/2022
13105,COMP2610,Information Theory,S2/2022
13104,COMP2560,Studies in Advanced Computing R&amp;D,S2/2022
13103,COMP2400,Relational Databases  ,S2/2022
13102,COMP2120,Software Engineering,S2/2022
13101,COMP2100,Software Design Methodologies,S2/2022
13100,COMP3900,HCI Human-Computer Interaction,S2/2022
13099,COMP1730,Programming for Scientists,S2/2022
13098,COMP1720,Art and Interaction Computing,S2/2022
13097,COMP1710,Web Development and Design,S2/2022
13096,COMP1600,Foundations of Computing,S2/2022
13095,COMP1140,Structured Programming (Advanced),S2/2022
13094,COMP3820,Computing Internship,S2/2022
13093,COMP1110,Structured Programming,S2/2022
13092,COMP3770,Individual Research Project,S2/2022
13091,COMP1100,Programming as Problem Solving,S2/2022
13090,COMP3740,Project Work in Computing,S2/2022
13089,COMP8420,"Neural Networks, Deep Learning and Bio-inspired Computing",Aut/2022
13088,COMP7240,Introduction to Database Concepts,Aut/2022
13087,COMP6490,Document Analysis,Aut/2022
13086,EXTN1019B,ANU Extension Creative Computing B,Aut/2022
13085,EXTN1019A,Creative Computing,Aut/2022
13084,COMP3710,LENS Topics in Computer Science,S2/2022
13083,COMP3704,Network Security,S2/2022
13082,EXTN1019A,Creative Computing,none/0
13081,EXTN1019B,ANU Extension Creative Computing B,S1/2022
13080,EXTN1019A,Creative Computing,S1/2022
13079,COMP8420,"Neural Networks, Deep Learning and Bio-inspired Computing",S1/2022
13078,COMP6490,Document Analysis,S1/2022
13077,COMP8830,Computer Science Internship,S1/2022
13076,COMP8800,Computing Research Project,S1/2022
13075,COMP8755,Individual Computing Project,S1/2022
13074,COMP8715,Computing Project,S1/2022
13073,COMP8600,Statistical Machine Learning,S1/2022
13072,PHIL2080,Logic,S1/2022
13071,COMP3550,Advanced Computing R&D Project,S1/2022
13070,COMP3500,Software Engineering Project (Part A),S1/2022
13069,COMP3310,Computer Networks,S1/2022
13068,COMP3120,Managing Software Development,S1/2022
13067,COMP2620,Logic,S1/2022
13066,COMP2550,Advanced Computing R&amp;D Methods,S1/2022
13065,COMP2420,"Introduction to Data Management, Analysis and Security",S1/2022
13064,COMP2410,Networked Information Systems,S1/2022
13063,COMP2300,Computer Organisation and Program Execution,S1/2022
13062,ENGN2219,Computer Architecture and Simulation,S1/2022
13061,COMP2100,Software Design Methodologies,S1/2022
13060,COMP1730,Programming for Scientists,S1/2022
13059,COMP1130,Programming as Problem Solving (Advanced),S1/2022
13058,COMP8300,Parallel Systems,S1/2022
13057,COMP8110,Managing Software Projects in a System Context,S1/2022
13056,COMP6730,Programming for Scientists,S1/2022
13055,COMP6719,Computer Systems &amp; Organisation,S1/2022
13054,COMP6710,Structured Programming,S1/2022
13053,COMP8410,Data Mining,S1/2022
13052,COMP8430,Data Wrangling,S1/2022
13051,COMP3820,Computing Internship,S1/2022
13050,COMP6442,Software Construction,S1/2022
13049,COMP6420,"Introduction to Data Management, Analysis and Security",S1/2022
13048,COMP6363,Theory of Computation,S1/2022
13047,COMP6340,Networked Information Systems,S1/2022
13046,COMP6331,Computer Networks,S1/2022
13045,COMP6320,Artificial Intelligence,S1/2022
13044,COMP6300,Computer Organisation and Program Execution,S1/2022
13043,COMP4670,Statistical Machine Learning,S1/2022
13042,COMP4560,Advanced Computing Project,S1/2022
13041,COMP4550,Advanced Computing Research Project,S1/2022
13040,COMP4540,Software Engineering Research Project,S1/2022
13039,COMP4500,Software Engineering Practice,S1/2022
13038,COMP4450,Advanced Computing Research Methods,S1/2022
13037,COMP4300,Parallel Systems,S1/2022
13036,COMP4130,Managing Software Quality and Process,S1/2022
13035,COMP3770,Individual Research Project,S1/2022
13034,COMP3740,Project Work in Computing,S1/2022
13033,COMP3703,Software Security,S1/2022
13032,COMP3630,Theory of Computation,S1/2022
13031,COMP3620,Artificial Intelligence,S1/2022
13030,ENGN6528,Computer Vision,S1/2022
13029,COMP6528,Computer Vision,S1/2022
13028,COMP6445,Advanced Computing Research Methods,S1/2022
13027,COMP6262,Logic,none/0
13026,COMP1110,Structured Programming,none/0
13025,COMP1100,Programming as Problem Solving,none/0
13024,COMP1110,Structured Programming,S1/2022
13023,COMP1100,Programming as Problem Solving,S1/2022
13022,COMP8430,Data Wrangling,S1/2021
13021,COMP6262,Logic,S1/2022
13020,COMP8430,Data Wrangling,Sum/2022
13018,COMP6470 MTLModal and Temporal Logistics,S2/2021
13017,COMP6470 QCQuantum Computing,S2/2021
13016,COMP8410,Data Mining,Win/2021
13015,COMP1140,Structured Programming (Advanced),S2/2021
13014,COMP6715,Project Work in Computing,S2/2021
13013,COMP8830,Computer Science Internship,S2/2021
13012,COMP3820,Software Engineering Internship,S2/2021
13011,COMP2100,Software Design Methodologies,S2/2021
13010,COMP1730,Programming for Scientists,S2/2021
13009,COMP3710 MTLModal and Temporal Logics,S2/2021
13008,COMP3710 QCQuantum Computing,S2/2021
13005,COMP4330,Real-Time and Embedded Systems,S2/2021
13004,EXTN1019A,Creative Computing,Aut/2021
13002,COMP6715,Project Work in Computing,S1/2021
13000,COMP6470,Laptop Ensemble (Special Topics in Computer Science),S1/2021
12950,COMP3300,Operating Systems Implementation,S2/2021
12913,COMP8880,Computational Methods for Network Science,S1/2021
12912,COMP4880,Computational Methods for Network Science,S1/2021
12911,COMP8691,Optimisation,S2/2021
12910,COMP4691,Optimisation,S2/2021
12909,COMP8650,Advanced Topics in Statistical Machine Learning,S2/2021
12908,COMP4680,Advanced Topics in Statistical Machine Learning,S2/2021
12907,COMP6490,Document Analysis,S2/2021
12906,COMP4650,Document Analysis,S2/2021
12905,COMP8670,Advanced Topics in Logic and Computation,S2/2021
12904,COMP4630,Overview of Logic and Computation,S2/2021
12903,COMP8620,Advanced Topics in Artificial Intelligence,S2/2021
12902,COMP4620,Advanced Topics in Artificial Intelligence,S2/2021
12901,COMP6461,Computer Graphics,S2/2021
12900,COMP4610,Computer Graphics,S2/2021
12899,COMP6390,HCI Design and Evaluation,S2/2021
12898,COMP3900,HCI Design and Evaluation,S2/2021
12897,COMP6470,"Topics in Computer Science,Computer Architecture",S2/2021
12896,COMP3710,Computer Microarchitecture,S2/2021
12895,COMP3704,Network Security,S2/2021
12894,COMP6670,Introduction to Machine Learning,S2/2021
12893,COMP3670,Introduction to Machine Learning,S2/2021
12892,COMP6361,Principles of Programming Languages,S2/2021
12891,COMP3610,Principles of Programming Languages,S2/2021
12890,COMP3610,Principles of Programming Languages,S2/2020
12889,COMP6466,Algorithms,S2/2021
12888,COMP3600,Algorithms,S2/2021
12887,COMP8430,Data Wrangling,S2/2021
12886,COMP3430,Data Wrangling,S2/2021
12885,COMP6464,High Performance Scientific Computation,S2/2021
12884,COMP3320,High Performance Scientific Computation,S2/2021
12883,COMP2700,Cyber Security Fundamentals,S2/2021
12882,COMP6261,Information Theory,S2/2021
12881,COMP2610,Information Theory,S2/2021
12880,COMP6240,Relational Databases,S2/2021
12879,COMP2400,Relational Databases  ,S2/2021
12878,COMP6310,Concurrent &amp; Distributed Systems,S2/2021
12877,COMP2310,Systems Networks and Concurrency,S2/2021
12876,COMP6120,Software Engineering,S2/2021
12875,COMP2120,Software Engineering,S2/2021
12874,COMP6720,Art and Interaction Computing,S2/2021
12873,COMP1720,Art and Interaction Computing,S2/2021
12872,COMP6260,Foundations of Computing,S2/2021
12871,COMP1600,Foundations of Computing,S2/2021
12870,COMP8260,Professional Practice 2,S2/2021
12869,COMP8260,Professional Practice 2,S1/2021
12868,COMP6250,Professional Practice 1,S2/2021
12867,COMP6250,Professional Practice 1,S1/2021
12866,COMP4800,Industrial Experience,S2/2021
12865,COMP4800,Industrial Experience,S1/2021
12864,COMP3560,Advanced Computing R&amp;D Industry Experience,S2/2021
12863,COMP3560,Advanced Computing R&amp;D Industry Experience,S1/2021
12862,COMP8755,Individual Computing Project,S2/2021
12861,COMP8755,Individual Computing Project,S1/2021
12860,COMP4560,Advanced Computing Project,S2/2021
12859,COMP4560,Advanced Computing Project,S1/2021
12858,COMP3770,Individual Research Project,S2/2021
12857,COMP3770,Individual Research Project,S1/2021
12856,COMP3740,Project Work in Computing,S2/2021
12855,COMP3740,Project Work in Computing,S1/2021
12854,COMP8800,Computing Research Project,S2/2021
12853,COMP8800,Computing Research Project,S1/2021
12852,COMP4550,Advanced Computing Research Project,S2/2021
12851,COMP4550,Advanced Computing Research Project,S1/2021
12850,COMP4540,Software Engineering Research Project,S2/2021
12849,COMP4540,Software Engineering Research Project,S1/2021
12848,COMP2560,Studies in Advanced Computing R&amp;D,S2/2021
12847,COMP2560,Studies in Advanced Computing R&amp;D,S1/2021
12846,COMP8715,Computing Project,S2/2021
12845,COMP8715,Computing Project,S1/2021
12844,COMP4500,Software Engineering Practice,S2/2021
12843,COMP4500,Software Engineering Practice,S1/2021
12842,COMP3550,Advanced Computing R&amp;D Project,S2/2021
12841,COMP3550,Advanced Computing R&amp;D Project,S1/2021
12840,COMP3500,Software Engineering Project (Part B),S2/2021
12839,COMP3500,Software Engineering Project (Part A),S1/2021
12838,COMP4801,Honours Result,S2/2021
12837,COMP4801,Honours Result,S1/2021
12836,COMP8420,"Neural Networks, Deep Learning and Bio-inspired Computing",Aut/2021
12835,COMP8410,Data Mining,none/0
12834,COMP7240,Introduction to Database Concepts,Aut/2021
12833,COMP7230,Introduction to Programming for Data Scientists,Win/2021
12832,COMP6490,Document Analysis,Aut/2021
12831,COMP6719,Computer Architecture and  Simulation,S1/2021
12830,ENGN2219,Computer Architecture and Simulation,S1/2021
12829,COMP8600,Statistical Machine Learning,S1/2021
12828,COMP4670,Statistical Machine Learning,S1/2021
12827,COMP8420,"Neural Networks, Deep Learning and Bio-inspired Computing",S1/2021
12826,COMP4660,"Neural Networks, Deep Learning and Bio-inspired Computing",S1/2021
12825,COMP8300,Parallel Systems,S1/2021
12824,COMP4300,Parallel Systems,S1/2021
12823,COMP4130,Managing Software Quality and Process,S1/2021
12822,COMP3703,Software Security,S1/2021
12821,COMP6363,Theory of Computation,S1/2021
12820,COMP3630,Theory of Computation,S1/2021
12819,COMP6320,Artificial Intelligence,S1/2021
12818,COMP3620,Artificial Intelligence,S1/2021
12817,COMP8410,Data Mining,S1/2021
12816,COMP3425,Data Mining,S1/2021
12815,COMP6331,Computer Networks,S1/2021
12814,COMP3310,Computer Networks,S1/2021
12813,COMP8110,Managing Software Projects in a System Context,S1/2021
12812,COMP3120,Managing Software Development,S1/2021
12811,COMP2710,Laptop Ensemble (Special Topics in Computer Science),S1/2021
12810,PHIL2080,Logic,S1/2021
12809,COMP6262,Logic,S1/2021
12808,COMP2620,Logic,S1/2021
12807,COMP6445,Advanced Computing Research Methods,S1/2021
12806,COMP4450,Advanced Computing Research Methods,S1/2021
12805,COMP2550,Advanced Computing R&amp;D Methods,S1/2021
12804,COMP6420,"Introduction to Data Management, Analysis and Security",S1/2021
12803,COMP2420,"Introduction to Data Management, Analysis and Security",S1/2021
12802,COMP6340,Networked Information Systems,S1/2021
12801,COMP2410,Networked Information Systems,S1/2021
12800,COMP6300,Computer Organisation and Program Execution,S1/2021
12799,COMP2300,Computer Organisation and Program Execution,S1/2021
12798,COMP6780,Web Development and Design,S1/2021
12797,COMP6442,Software Construction,S2/2021
12796,COMP6442,Software Construction,S1/2021
12795,COMP6730,Programming for Scientists,S1/2021
12794,COMP6730,Programming for Scientists,S2/2021
12793,COMP6710,Structured Programming,S2/2021
12792,COMP1110,Structured Programming,S2/2021
12791,COMP1100,Programming as Problem Solving,S2/2021
12790,COMP6710,Structured Programming,S1/2021
12789,COMP1730,Programming for Scientists,S1/2021
12788,COMP1710,Web Development and Design,S1/2021
12787,COMP2100,Software Design Methodologies,S1/2021
12786,COMP1110,Structured Programming,S1/2021
12785,COMP1130,Programming as Problem Solving (Advanced),S1/2021
12784,COMP1100,Programming as Problem Solving,S1/2021
12783,COMP8430,Data Wrangling,Sum/2021
12782,COMP3710,Topics in Computer Science,Win/2020
12781,COMP7230,Introduction to Programming for Data Scientists GCDE Intensive,Spr/2020
12779,COMP7240,"Introduction to Database Concepts,GCDE Intensive",Win/2020
12778,COMP8410,"Data Mining,GCDE Intensive",Spr/2020
12777,COMP8430,"Data Wrangling,GCDE Intensive",Spr/2020
12776,COMP8620,Advanced Topics in Artificial Intelligence,S2/2020
12774,ANUC2400,Relational Databases,S1/2020
12772,COMP4620,Advanced Topics in Artifical Intelligence,S2/2020
12771,COMP8420,"Neural Networks, Deep Learning and Bio-inspired Computing",Aut/2020
12770,COMP6461,Computer Graphics,S2/2020
12769,COMP4610,Computer Graphics,S2/2020
12768,COMP3320,High Performance Scientific Computation,S2/2020
12767,PHIL2080,Logic,S1/2020
12765,COMP8830,Computer Science Internship,S2/2020
12764,COMP8800,Computing Research Project,S2/2020
12763,COMP8755,Individual Computing Project,S2/2020
12762,COMP8715,Computing Project,S2/2020
12761,COMP8691,Optimisation,S2/2020
12760,COMP8650,Advanced Topics in Statistical Machine Learning,S2/2020
12759,COMP8460,Advanced Algorithms,S2/2020
12758,COMP8430,Data Wrangling,S2/2020
12757,COMP8260,Professional Practice 2,S2/2020
12756,COMP8190,Model-Driven Software Development,S2/2020
12755,COMP6730,Programming for Scientists,S2/2020
12754,COMP6720,Art Interaction and New Media,S2/2020
12753,COMP6710,Structured Programming,S2/2020
12752,COMP6670,Introduction to Machine Learning,S2/2020
12751,COMP6490,Document Analysis,S2/2020
12750,COMP6470,Special topics for postgraduate study,S2/2020
12749,COMP6466,Algorithms,S2/2020
12748,COMP6464,High Performance Scientific Computation,S2/2020
12747,COMP6442,Software Construction,S2/2020
12746,COMP6390,HCI Design and Evaluation,S2/2020
12745,COMP6353,Systems Engineering for Software Engineers,S2/2020
12744,COMP6330,Operating Systems Implementation,S2/2020
12743,COMP6310,Concurrent &amp; Distributed Systems,S2/2020
12742,COMP6260,Foundations of Computing,S2/2020
12741,COMP6250,Professional Practice 1,S2/2020
12740,COMP6240,Relational Databases,S2/2020
12739,COMP6261,Information Theory,S2/2020
12738,COMP6120,Software Engineering,S2/2020
12737,COMP4801,Honours Result,S2/2020
12736,COMP4800,Industrial Experience,S2/2020
12735,COMP4691,Optimisation,S2/2020
12734,COMP4680,Advanced Topics in Statistical Machine Learning,S2/2020
12733,COMP4650,Document Analysis,S2/2020
12732,COMP4600,Advanced Algorithms,S2/2020
12731,COMP4560,Advanced Computing Project,S2/2020
12730,COMP4550,Advanced Computing Research Project,S2/2020
12729,COMP4540,Software Engineering Research Project,S2/2020
12728,COMP4500,Software Engineering Practice,S2/2020
12727,COMP3900,HCI Design and Evaluation,S2/2020
12726,COMP3820,Software Engineering Internship,S2/2020
12725,COMP3770,Individual Research Project,S2/2020
12724,COMP3740,Project Work in Computing,S2/2020
12723,COMP3710,Topics in Computer Science,S2/2020
12722,COMP3701,Defensive Cyber Security Operations,S2/2020
12721,COMP3670,Introduction to Machine Learning,S2/2020
12720,COMP3600,Algorithms,S2/2020
12719,COMP3560,Advanced Computing R&amp;D Industry Experience,S2/2020
12718,COMP3550,Advanced Computing R&amp;D Project,S2/2020
12717,COMP3530,System Engineering for Software Engineers,S2/2020
12716,COMP3500,Software Engineering Project (Part A),S2/2020
12715,COMP3430,Data Wrangling,S2/2020
12714,COMP3300,Operating Systems Implementation,S2/2020
12713,COMP2700,Cyber Security Fundamentals,S2/2020
12712,COMP2610,Information Theory,S2/2020
12711,COMP2560,Studies in Advanced Computing R&amp;D,S2/2020
12710,COMP2400,Relational Databases  ,S2/2020
12709,COMP2710,Special Topics in Computer Science,S2/2020
12708,COMP2310,Systems Networks and Concurrency,S2/2020
12707,COMP2120,Software Engineering,S2/2020
12706,COMP2100,Software Design Methodologies,S2/2020
12705,COMP1730,Programming for Scientists,S2/2020
12704,COMP1720,Art and Interaction in New Media,S2/2020
12703,COMP1600,Foundations of Computing,S2/2020
12702,COMP1140,Structured Programming (Advanced),S2/2020
12701,COMP1110,Structured Programming,S2/2020
12700,COMP1100,Programming as Problem Solving,S2/2020
12699,COMP8830,Computer Science Internship,S1/2020
12698,COMP8800,Computing Research Project,S1/2020
12697,COMP8755,Individual Computing Project,S1/2020
12696,COMP8715,Computing Project,S1/2020
12695,COMP8600,Statistical Machine Learning,S1/2020
12694,COMP8420,"Neural Networks, Deep Learning and Bio-inspired Computing",S1/2020
12693,COMP8410,Data Mining,S1/2020
12692,COMP8300,Parallel Systems,S1/2020
12691,COMP8260,Professional Practice 2,S1/2020
12690,COMP8110,Managing Software Projects in a System Context,S1/2020
12689,COMP6780,Web Development and Design,S1/2020
12688,COMP6730,Programming for Scientists,S1/2020
12687,COMP6719,Computer Architecture and  Simulation,S1/2020
12686,COMP6710,Structured Programming,S1/2020
12685,COMP6470,Special topics for postgraduate study,S1/2020
12684,COMP6445,Advanced Computing Research Methods,S1/2020
12683,COMP6442,Software Construction,S1/2020
12682,COMP6420,"Introduction to Data Management, Analysis and Security",S1/2020
12681,COMP6363,Theory of Computation,S1/2020
12680,COMP6340,Networked Information Systems,S1/2020
12679,COMP6331,Computer Networks,S1/2020
12678,COMP6320,Artificial Intelligence,S1/2020
12677,COMP6300,Computer Organisation and Program Execution,S1/2020
12676,COMP6262,Logic,S1/2020
12675,COMP6250,Professional Practice 1,S1/2020
12674,COMP4801,Honours Result,S1/2020
12673,COMP4800,Industrial Experience,S1/2020
12672,COMP4670,Statistical Machine Learning,S1/2020
12671,COMP4660,"Neural Networks, Deep Learning and Bio-inspired Computing",S1/2020
12670,COMP4560,Advanced Computing Project,S1/2020
12669,COMP4550,Advanced Computing Research Project,S1/2020
12668,COMP4540,Software Engineering Research Project,S1/2020
12667,COMP4500,Software Engineering Practice,S1/2020
12666,COMP4450,Advanced Computing Research Methods,S1/2020
12665,COMP4300,Parallel Systems,S1/2020
12664,COMP4130,Managing Software Quality and Process,S1/2020
12663,COMP3820,Software Engineering Internship,S1/2020
12662,COMP3770,Individual Research Project,S1/2020
12661,COMP3740,Project Work in Computing,S1/2020
12660,COMP3710,Topics in Computer Science,S1/2020
12659,COMP3702,Offensive Cyber Security Operations,S1/2020
12658,COMP3630,Theory of Computation,S1/2020
12657,COMP3620,Artificial Intelligence,S1/2020
12656,COMP3560,Advanced Computing R&amp;D Industry Experience,S1/2020
12655,COMP3550,Advanced Computing R&amp;D Project,S1/2020
12654,COMP3500,Software Engineering Project (Part A),S1/2020
12653,COMP3425,Data Mining,S1/2020
12652,COMP3320,High Performance Scientific Computation,S1/2020
12651,COMP3310,Computer Networks,S1/2020
12650,COMP3120,Managing Software Development,S1/2020
12649,COMP2710,Special Topics in Computer Science,S1/2020
12648,COMP2620,Logic,S1/2020
12647,COMP2550,Advanced Computing R&amp;D Methods,S1/2020
12646,COMP2420,"Introduction to Data Management, Analysis and Security",S1/2020
12645,COMP2410,Networked Information Systems,S1/2020
12644,COMP2300,Computer Organisation and Program Execution,S1/2020
12643,COMP2100,Software Design Methodologies,S1/2020
12642,COMP1730,Programming for Scientists,S1/2020
12641,COMP1710,Web Development and Design,S1/2020
12640,COMP1130,Programming as Problem Solving (Advanced),S1/2020
12639,COMP1110,Structured Programming,S1/2020
12638,COMP1100,Programming as Problem Solving,S1/2020
12637,COMP6470,Special Topics in Computing,Spr/2020
12636,COMP3710,Topics in Computer Science,Spr/2020
12635,COMP8410,Data Mining,Win/2020
12634,COMP7230,Introduction to Programming for Data Scientists,Win/2020
12633,COMP6490,Document Analysis,Aut/2020
12632,COMP8430,Data Wrangling,Sum/2020
12631,COMP7240,Introduction to Database Concepts,Sum/2022
12630,COMP3710,Topics in Computer Science,Sum/2020
12493,ENGN2219,Computer Architecture and Simulation,S1/2020
12489,VCUG3100,Group Research and Innovation Project (GRIP),S2/2019
12485,COMP8330,Real-Time Embedded Systems,S2/2019
12484,COMP8691,Optimisation,S2/2019
12483,COMP8670,Advanced Topics in Logic and Computation,S2/2019
12482,COMP8173,Software Engineering Processes,Win/2019
12481,COMP6461,Computer Graphics,S2/2019
12480,COMP4610,Computer Graphics,S2/2019
12479,VCUG3100,Group Research and Innovation Project (GRIP),S1/2019
12476,COMP6490,Document Analysis,Aut/2019
12475,COMP3710 PROJECTCS Project,Sum/2019
12474,COMP3710 PROJECTCS Project,Spr/2018
12473,COMP3710,Topics in Computer Science,Spr/2019
12472,COMP4630,Overview of Logic and Computation,S2/2019
12467,COMP2710,Special Topics in Computer Science,S1/2019
12330,COMP8180,Systems and Software Safety,Aut/2019
12329,COMP4650,Document Analysis,S1/2019
12328,COMP8650,Advanced Topics in Statistical Machine Learning,S1/2019
12327,COMP4680,Advanced Topics in Statistical Machine Learning,S1/2019
12326,HONS4700,Honours,S1/2019
12325,COMP6470,Special Topics in Computing,Spr/2018
12324,COMP4330,Real-Time and Embedded Systems,S2/2019
12323,VCUG3100,Group Research and Innovation Project (GRIP),S2/2018
12322,COMP3100,Software Engineering Group Project,S2/2018
12321,COMP8100,Requirements Elicitation and Analysis Techniques,S1/2019
12320,COMP8620,Advanced Topics in Artificial Intelligence,S2/2019
12319,COMP4620,Advanced Topics in Artifical Intelligence,S2/2019
12318,COMP8410,Data Mining,Win/2019
12317,COMP7230,Introduction to Programming for Data Scientists,Win/2019
12316,COMP8430,Data Wrangling,Sum/2019
12315,COMP3710,Hacker Exchange,Spr/2018
12314,COMP4691,Optimisation,S2/2019
12313,COMP6670,Introduction to Machine Learning,S2/2019
12312,COMP3670,Introduction to Machine Learning,S2/2019
12311,COMP8880,Computational Methods for Network Science,S1/2019
12310,COMP4880,Computational Methods for Network Science,S1/2019
12309,COMP3710_1,Compiler Construction,S1/2019
12308,COMP2710_1,Laptop Ensemble,S2/2019
12307,COMP3710_1,Laptop Ensemble,Sum/2019
12305,VCUG3200,Innovation and Professional Practice Internship,S2/2019
12304,COMPSPPC,South Pacific Programming Contest,S2/2019
12303,COMPCHST,China Study Tour,S2/2019
12302,COMP8830,Computer Science Internship,S2/2019
12301,COMP8800,Computing Research Project,S2/2019
12300,COMP8755I,Internship,S2/2019
12299,COMP8755,Individual Computing Project,S2/2019
12298,COMP8715,Computing Project,S2/2019
12297,COMP8650,Advanced Topics in Statistical Machine Learning,S2/2019
12296,COMP8460,Advanced Algorithms,S2/2019
12295,COMP8430,Data Wrangling,S2/2019
12294,COMP8260,Professional Practice 2,S2/2019
12293,COMP8190,Model-Driven Software Development,S2/2019
12292,COMP6730,Programming for Scientists,S2/2019
12291,COMP6720,Art Interaction and New Media,S2/2019
12290,COMP6710,Structured Programming,S2/2019
12289,COMP6490,Document Analysis,S2/2019
12288,COMP6470,Special topics for postgraduate study,S2/2019
12287,COMP6466,Algorithms,S2/2019
12286,COMP6442,Software Construction,S2/2019
12285,COMP6390,HCI Design and Evaluation,S2/2019
12284,COMP6361,Principles of Programming Languages,S2/2019
12283,COMP6353,Systems Engineering for Software Engineers,S2/2019
12282,COMP6330,Operating Systems Implementation,S2/2019
12281,COMP6310,Concurrent &amp; Distributed Systems,S2/2019
12280,COMP6261,Information Theory,S2/2019
12279,COMP6260,Foundations of Computing,S2/2019
12278,COMP6250,Professional Practice 1,S2/2019
12277,COMP6240,Relational Databases,S2/2019
12276,COMP6120,Software Engineering,S2/2019
12275,COMP4801,Honours Result,S2/2019
12274,COMP4800,Industrial Experience,S2/2019
12273,COMP4680,Advanced Topics in Statistical Machine Learning,S2/2019
12272,COMP4650,Document Analysis,S2/2019
12271,COMP4560,Advanced Computing Project,S2/2019
12270,COMP4550,Advanced Computing Research Project,S2/2019
12269,COMP4540,Software Engineering Research Project,S2/2019
12268,COMP4500,Software Engineering Practice,S2/2019
12267,COMP4006,Computer Science Honours,S2/2019
12266,COMP4005P,Computer Science IV Honours,S2/2019
12265,COMP4005F,Computer Science IV Honours,S2/2019
12264,COMP3900,HCI Design and Evaluation,S2/2019
12263,COMP3820,Software Engineering Internship,S2/2019
12262,COMP3770,Individual Research Project,S2/2019
12261,COMP3740,Project Work in Computing,S2/2019
12260,COMP3710,Topics in Computer Science,S2/2019
12259,COMP3701,Defensive Cyber Security Operations,S2/2019
12258,COMP3610,Principles of Programming Languages,S2/2019
12257,COMP3600,Algorithms,S2/2019
12256,COMP3560,Advanced Computing R&amp;D Industry Experience,S2/2019
12255,COMP3550,Advanced Computing R&amp;D Project,S2/2019
12254,COMP3530,System Engineering for Software Engineers,S2/2019
12253,COMP3500,Software Engineering Project (Part B),S2/2019
12252,COMP3430,Data Wrangling,S2/2019
12251,COMP3300,Operating Systems Implementation,S2/2019
12250,COMP2710,Special Topics in Computer Science,S2/2019
12249,COMP2700,Cyber Security Fundamentals,S2/2019
12248,COMP2610,Information Theory,S2/2019
12247,COMP2560,Studies in Advanced Computing R&amp;D,S2/2019
12246,COMP2400,Relational Databases  ,S2/2019
12245,COMP2310,Systems Networks and Concurrency,S2/2019
12244,COMP2120,Software Engineering,S2/2019
12243,COMP2100,Software Design Methodologies,S2/2019
12242,COMP1730,Programming for Scientists,S2/2019
12241,COMP1720,Art and Interaction in New Media,S2/2019
12240,COMP1600,Foundations of Computing,S2/2019
12239,COMP1140,Structured Programming (Advanced),S2/2019
12238,COMP1110,Structured Programming,S2/2019
12237,COMP1100,Programming as Problem Solving,S2/2019
12236,COMP4801,Honours Result,S2/2018
12235,COMP4800,Industrial Experience,S2/2018
12233,COMPCHST,China Study Tour,Sum/2019
12232,COMPSPPC,South Pacific Programming Contest,S2/2018
12231,COMP4600,Advanced Algorithms,S2/2019
12229,COMP7240,Introduction to Database Concepts,Sum/2019
12228,COMP6470,Special Topics in Computing,Sum/2019
12227,COMP3820,Software Engineering Internship,Sum/2019
12226,COMP3710,Topics in Computer Science,Sum/2019
12225,VCUG3001,Unravelling Complexity,S1/2019
12224,VCUG2004,Creating Impact,S1/2019
12223,VCPG6004,Creating Impact,S1/2019
12222,PHIL2080,Logic,S1/2019
12221,ENGN2219,Computer Architecture and Simulation,S1/2019
12220,COMP8830,Computer Science Internship,S1/2019
12219,COMP8800,Computing Research Project,S1/2019
12218,COMP8755I,Internship,S1/2019
12217,COMP8755,Individual Computing Project,S1/2019
12216,COMP8715,Computing Project,S1/2019
12215,COMP8600,Introduction to Statistical Machine Learning,S1/2019
12214,COMP8420,"Neural Networks, Deep Learning and Bio-inspired Computing",S1/2019
12213,COMP8410,Data Mining,S1/2019
12212,COMP8260,Professional Practice 2,S1/2019
12211,COMP8110,Managing Software Projects in a System Context,S1/2019
12210,COMP7310,ICT Sustainability,S1/2019
12209,COMP6780,Web Development and Design,S1/2019
12208,COMP6730,Programming for Scientists,S1/2019
12207,COMP6719,Computer Architecture and  Simulation,S1/2019
12206,COMP6710,Structured Programming,S1/2019
12205,COMP6470,Special Topics,S1/2019
12204,COMP6464,High Performance Scientific Computation,S1/2019
12203,COMP6445,Advanced Computing Research Methods,S1/2019
12202,COMP6442,Software Construction,S1/2019
12201,COMP6420,"Introduction to Data Management, Analysis and Security",S1/2019
12200,COMP6363,Theory of Computation,S1/2019
12199,COMP6340,Networked Information Systems,S1/2019
12198,COMP6331,Computer Networks,S1/2019
12197,COMP6320,Artificial Intelligence,S1/2019
12196,COMP6300,Computer Organisation and Program Execution,S1/2019
12195,COMP6262,Logic,S1/2019
12194,COMP6250,Professional Practice 1,S1/2019
12193,COMP4801,Honours Result,S1/2019
12192,COMP4800,Industrial Experience,S1/2019
12191,COMP4670,Introduction to Statistical Machine Learning,S1/2019
12190,COMP4660,"Neural Networks, Deep Learning and Bio-inspired Computing",S1/2019
12189,COMP4560,Advanced Computing Project,S1/2019
12188,COMP4550,Advanced Computing Research Project,S1/2019
12187,COMP4540,Software Engineering Research Project,S1/2019
12186,COMP4500,Software Engineering Practice,S1/2019
12185,COMP4450,Advanced Computing Research Methods,S1/2019
12184,COMP4130,Managing Software Quality and Process,S1/2019
12183,COMP4006,Computer Science Honours,S1/2019
12182,COMP4005F,Computer Science IV Honours,S1/2019
12181,COMP3820,Software Engineering Internship,S1/2019
12180,COMP3770,Individual Research Project,S1/2019
12179,COMP3740,Project Work in Computing,S1/2019
12178,COMP3710,Topics in Computer Science,S1/2019
12177,COMP3702,Offensive Cyber Security Operations,S1/2019
12176,COMP3630,Theory of Computation,S1/2019
12175,COMP3620,Artificial Intelligence,S1/2019
12174,COMP3560,Advanced Computing R&amp;D Industry Experience,S1/2019
12173,COMP3550,Advanced Computing R&amp;D Project,S1/2019
12172,COMP3500,Software Engineering Project (Part A),S1/2019
12171,COMP3425,Data Mining,S1/2019
12170,COMP3320,High Performance Scientific Computation,S1/2019
12169,COMP3310,Computer Networks,S1/2019
12168,COMP3120,Managing Software Development,S1/2019
12167,COMP2710,Special Topics in Computer Science,Sum/2019
12166,COMP2620,Logic,S1/2019
12165,COMP2550,Advanced Computing R&amp;D Methods,S1/2019
12164,COMP2420,"Introduction to Data Management, Analysis and Security",S1/2019
12163,COMP2410,Networked Information Systems,S1/2019
12162,COMP2300,Computer Organisation and Program Execution,S1/2019
12161,COMP2100,Software Design Methodologies,S1/2019
12160,COMP1730,Programming for Scientists,S1/2019
12159,COMP1710,Web Development and Design,S1/2019
12158,COMP1130,Programming as Problem Solving (Advanced),S1/2019
12157,COMP1110,Structured Programming,S1/2019
12156,COMP1100,Programming as Problem Solving,S1/2019
12155,COMP1007,Basics of Computer Science,S1/2019
12154,ANUC2400,Relational Databases,S1/2019
12151,VCUG3200,Innovation and Professional Practice Internship,S2/2018
12150,COMP8410,Data Mining,Win/2018
12149,VCUG3001,Unravelling Complexity,S1/2018
12148,COMP4801,Honours Result,S1/2018
12147,COMP6470,Special Topics in Computing,Aut/2018
12146,COMP6120,Software Engineering,S2/2018
12145,COMP8190,Model-Driven Software Development,S2/2018
12143,COMP8430,Data Wrangling,S2/2018
12140,COMP6470,Deffensive Cyber Security Operations,S2/2018
12139,COMP8420,Bio-inspired Computing: Applications and Interfaces,Aut/2018
12138,COMP3820,Software Engineering Internship,Sum/2018
12136,COMP6445,Advanced Computing Research Methods,S1/2018
12134,COMP8800,Computing Research Project,S2/2018
12133,COMP8800,Computing Research Project,S1/2018
12132,COMP8180,Systems and Software Safety,Aut/2018
12131,COMP8830,Computer Science Internship,S2/2018
12130,COMP8830,Computer Science Internship,S1/2018
12129,ANUC2400,Relational Databases,S1/2018
12128,COMP2710,Special Topics in Computer Science,Spr/2017
12127,COMP4800,Industrial Experience,S1/2018
12126,COMP8460,Advanced Algorithms,S2/2018
12125,COMP4600,Advanced Algorithms,S2/2018
12124,COMP8440,Free &amp; Open Source Software Development,Aut/2018
12123,COMP7230,Introduction to Programming for Data Scientists,Win/2018
12122,COMP4005P,Computer Science IV Honours,S2/2018
12121,COMP4005F,Computer Science IV Honours,S2/2018
12120,COMP4005F,Computer Science IV Honours,S1/2018
12119,COMP7310,ICT Sustainability,S1/2018
12118,COMP7240,Introduction to Database Concepts,Sum/2018
12117,COMP3710,"Topics in Computer Science,Offensive Cyber Operations",Aut/2018
12116,COMP6470,Special Topics in Computing,Sum/2018
12115,COMP3710,Topics in Computer Science,Sum/2018
12114,COMP6710,Structured Programming,S1/2018
12113,VCPG6004,Creating Impact,S1/2018
12112,VCUG2004,Creating Impact,S1/2018
12111,DESN6006,Front-End Web: Crafting Online Experience,S2/2017
12110,DESN2006,Front-End Web: Crafting Online Experience,S2/2017
12109,COMP8755I,Internship,S2/2018
12108,COMP8755I,Internship,S1/2018
12107,COMP3710,Topics in Computer Science,S2/2018
12106,COMP4550,Advanced Computing Research Project,S2/2018
12105,COMP4540,Software Engineering Research Project,S2/2018
12104,COMP4006,Computer Science Honours,S2/2018
12103,COMP8755,Individual Computing Project,S2/2018
12102,COMP4560,Advanced Computing Project,S2/2018
12101,COMP3770,Individual Research Project,S2/2018
12100,COMP3740,Project Work in Computing,S2/2018
12099,COMP8715,Computing Project,S2/2018
12098,COMP4500,Software Engineering Practice,S2/2018
12097,COMP3550,Advanced Computing R&amp;D Project,S2/2018
12096,COMP3500,Software Engineering Project (Part B),S2/2018
12095,COMP6353,Systems Engineering for Software Engineers,S2/2018
12094,COMP3530,System Engineering for Software Engineers,S2/2018
12093,COMP8260,Professional Practice II,S2/2018
12092,COMP6250,Professional Practice I,S2/2018
12091,COMP8650,Advanced Topics in Statistical Machine Learning,S2/2018
12090,COMP4680,Advanced Topics in Statistical Machine Learning,S2/2018
12089,COMP6490,Document Analysis,S2/2018
12088,COMP4650,Document Analysis,S2/2018
12087,COMP6390,HCI Design and Evaluation,S2/2018
12086,COMP3900,HCI Design and Evaluation,S2/2018
12085,COMP3820,Software Engineering Internship,S2/2018
12084,COMP3701,Defensive Cyber Security Operations,S2/2018
12083,COMP6361,Principles of Programming Languages,S2/2018
12082,COMP3610,Principles of Programming Languages,S2/2018
12081,COMP6466,Algorithms,S2/2018
12080,COMP3600,Algorithms,S2/2018
12079,COMP3560,Advanced Computing R&amp;D Industry Experience,S2/2018
12078,COMP6330,Operating Systems Implementation,S2/2018
12077,COMP3300,Operating Systems Implementation,S2/2018
12076,COMP2700,Cyber Security Fundamentals,S2/2018
12075,COMP6261,Information Theory,S2/2018
12074,COMP2610,Information Theory,S2/2018
12073,COMP2560,Studies in Advanced Computing R&amp;D,S2/2018
12072,COMP6240,Relational Databases,S2/2018
12071,COMP2400,Relational Databases  ,S2/2018
12070,COMP6310,Concurrent &amp; Distributed Systems,S2/2018
12069,COMP2310,Systems Networks and Concurrency,S2/2018
12068,COMP2120,Software Engineering,S2/2018
12067,COMP6442,Software Construction,S2/2018
12066,COMP2100,Software Design Methodologies,S2/2018
12065,COMP6720,Art Interaction and New Media,S2/2018
12064,COMP1720,Art and Interaction in New Media,S2/2018
12063,COMP6260,Foundations of Computing,S2/2018
12062,COMP1600,Foundations of Computing,S2/2018
12061,COMP6710,Structured Programming,S2/2018
12060,COMP1140,Structured Programming (Advanced),S2/2018
12059,COMP1110,Structured Programming,S2/2018
12058,COMP1100,Programming as Problem Solving,S2/2018
12057,COMP4006,Computer Science Honours,S1/2018
12056,COMP4550,Advanced Computing Research Project,S1/2018
12055,COMP4540,Software Engineering Research Project,S1/2018
12054,COMP8755,Individual Computing Project,S1/2018
12053,COMP4560,Advanced Computing Project,S1/2018
12052,COMP3770,Individual Research Project,S1/2018
12051,COMP3740,Project Work in Computing,S1/2018
12050,COMP8715,Computing Project,S1/2018
12049,COMP4500,Software Engineering Practice,S1/2018
12048,COMP3550,Advanced Computing R&amp;D Project,S1/2018
12047,COMP3500,Software Engineering Project (Part A),S1/2018
12046,COMP8260,Professional Practice 2,S1/2018
12045,COMP6250,Professional Practice 1,S1/2018
12044,COMP8600,Introduction to Statistical Machine Learning,S1/2018
12043,COMP4670,Introduction to Statistical Machine Learning,S1/2018
12042,COMP8420,Bio-inspired Computing: Applications and Interfaces,S1/2018
12041,COMP4660,Bio-inspired Computing: Applications and Interfaces,S1/2018
12040,COMP4130,Managing Software Quality and Process,S1/2018
12039,COMP3820,Software Engineering Internship,S1/2018
12038,COMP6470,Offensive Cyber Security Operations,S1/2018
12037,COMP3710,Topics in Computer Science,S1/2018
12036,COMP3702,Offensive Cyber Security Operations,S1/2018
12035,COMP6363,Theory of Computation,S1/2018
12034,COMP6363,Theory of Computation,S1/2017
12033,COMP3630,Theory of Computation,S1/2018
12032,COMP6320,Artificial Intelligence,S1/2018
12031,COMP3620,Artificial Intelligence,S1/2018
12030,COMP3560,Advanced Computing R&amp;D Industry Experience,S1/2018
12029,COMP8410,Data Mining,S1/2018
12028,COMP6464,High Performance Scientific Computation,S1/2018
12027,COMP3320,High Performance Scientific Computation,S1/2018
12026,COMP6331,Computer Networks,S1/2018
12025,COMP3310,Computer Networks,S1/2018
12024,COMP8110,Managing Software Projects in a System Context,S1/2018
12023,COMP3120,Managing Software Development,S1/2018
12022,COMP6719,Computing for Engineering Simulation,S1/2018
12021,ENGN2219,Computing for Engineering Simulation,S1/2018
12020,COMP2710,Special Topics in Computer Science,S2/2018
12019,COMP2710,Special Topics in Computer Science,S1/2018
12018,PHIL2080,Logic,S1/2018
12017,COMP6262,Logic,S1/2018
12016,COMP2620,Logic,S1/2018
12015,COMP4450,Advanced Computing Research Methods,S1/2018
12014,COMP2550,Advanced Computing R&amp;D Methods,S1/2018
12013,COMP6420,"Introduction to Data Management, Analysis and Security",S1/2018
12012,COMP6340,Networked Information Systems,S1/2018
12011,COMP2410,Networked Information Systems,S1/2018
12010,COMP6300,Computer Organisation and Program Execution,S1/2018
12009,COMP2300,Computer Organisation and Program Execution,S1/2018
12008,COMP6442,Software Construction,S1/2018
12007,COMP2100,Software Design Methodologies,S1/2018
12006,COMP6730,Programming for Scientists,S2/2018
12005,COMP6730,Programming for Scientists,S1/2018
12004,COMP1730,Programming for Scientists,S2/2018
12003,COMP1730,Programming for Scientists,S1/2018
12002,COMP6780,Web Development and Design,S1/2018
12001,COMP1710,Web Development and Design,S1/2018
12000,COMP1110,Structured Programming,S1/2018
11999,COMP1130,Programming as Problem Solving (Advanced),S1/2018
11998,COMP1100,Programming as Problem Solving,S1/2018
11997,COMP1007,Basics of Computer Science,S1/2018
11992,ANUC1710,Web Development and Design,S2/2017
11991,ANUC2400,Relational Databases,S2/2017
11990,COMP6470,"Special Topics in Computing,Defensive Cyber Operations",Win/2017
11989,COMP3770,Individual Research Project,S2/2017
11988,COMP3710,"Topics in Computer Science,Defensive Cyber Operations",Win/2017
11987,COMP4560,Advanced Computing Project,S2/2017
11985,COMP8755I,Internship,S2/2017
11984,COMP8755,Individual Computing Project,S2/2017
11983,COMP8173,Software Engineering Processes,Win/2017
11982,COMP6470,"Special Topics in Computing,Offensive Cyper Operations",Aut/2017
11981,COMP4801,Honours Result,Sum/2017
11979,COMP2550,Advanced Computing R&amp;D Methods,none/0
11974,COMP6470,Special Topics in Computing,Sum/2016
11973,COMP3710,"Topics in Computer Science,Offensive Cyber Operations",Aut/2017
11972,VCPG6004,Creating Impact,S1/2017
11970,COMP8110,Managing Software Projects in a System Context,S1/2017
11969,COMP3100,Software Engineering Group Project,S1/2017
11968,COMP8260,Professional Practice II,S2/2017
11967,COMP8260,Professional Practice 2,S1/2017
11966,COMP6250,Professional Practice I,S2/2017
11965,COMP6250,Professional Practice 1,S1/2017
11964,COMP2710,Special Topics in Computer Science,Spr/2016
11963,COMP7230,Introduction to Programming for Data Scientists,Win/2017
11962,COMP4450,Advanced Computing Research Methods,S1/2017
11961,COMP3560,Advanced Computing R&amp;D Industry Experience,S1/2017
11960,COMP3430,Data Wrangling,S2/2018
11959,COMP3425,Datamining,S1/2018
11958,COMP2710,Special Topics in Computer Science,S2/2017
11957,COMP2710,Special Topics in Computer Science,S1/2017
11956,VCUG2004,Creating Impact,S1/2017
11955,ANUC2400,Relational Databases,S1/2017
11954,ANUC1110,Introduction to Software Systems,S2/2017
11953,COMP1100,Programming as Problem Solving,S2/2017
11952,INFT4005P,"Information Technology Honours,Parttime",S2/2017
11951,INFT4005F,"Information Technology Honours,Fulltime",S2/2017
11950,COMPSPPC,South Pacific Programming Contest,S2/2017
11949,COMP9000P,(Unknown),S2/2017
11948,COMP9000F,(Unknown),S2/2017
11947,COMP8900P,(Unknown),S2/2017
11946,COMP8900F,(Unknown),S2/2017
11945,COMP8800,Computing Research Project,S2/2017
11944,COMP8790,Software Engineering Project,S2/2017
11943,COMP8780,Information &amp; Human Centred Computer Project,S2/2017
11942,COMP8750,Computer Systems Project,S2/2017
11941,COMP8740,Artificial Intelligence Project,S2/2017
11940,COMP8715,Computing Project,S2/2017
11939,COMP8705,Communication for Computing Professionals,S2/2017
11938,COMP8701,Communication for Computing Professionals I,S2/2017
11937,COMP8670,Advanced Topics in Logic and Computation,S2/2017
11936,COMP8620,Advanced Topics in Artificial Intelligence,S2/2017
11935,COMP8330,Real-Time Embedded Systems,S2/2017
11934,COMP8200,Master of Computing Honours Results,S2/2017
11933,COMP6730,Programming for Scientists,S2/2017
11932,COMP6720,Art Interaction and New Media,S2/2017
11931,COMP6710,Structured Programming,S2/2017
11930,COMP6490,Document Analysis,S2/2017
11929,COMP6470,Special Topics in Computing,S2/2017
11928,COMP6466,Algorithms,S2/2017
11927,COMP6461,Computer Graphics,S2/2017
11926,COMP6433,Real-time Embedded Systems,S2/2017
11925,COMP6390,HCI Design and Evaluation,S2/2017
11924,COMP6361,Principles of Programming Languages,S2/2017
11923,COMP6311,Software Analysis and Design,S2/2017
11922,COMP6310,Concurrent &amp; Distributed Systems,S2/2017
11921,COMP6261,Information Theory,S2/2017
11920,COMP6260,Foundations of Computing,S2/2017
11919,COMP6240,Relational Databases,S2/2017
11918,COMP4801,Software Engineering Honours Results,S2/2017
11917,COMP4800,Industrial Experience,S2/2017
11916,COMP4710,Topics in Software Engineering III ,S2/2017
11915,COMP4650,Document Analysis,S2/2017
11914,COMP4630,Overview of Logic and Computation,S2/2017
11913,COMP4620,Advanced Topics in Artifical Intelligence,S2/2017
11912,COMP4610,Computer Graphics,S2/2017
11911,COMP4560,Advanced Computing Project,Sum/2016
11910,COMP4550,Advanced Computing Research Project,S2/2017
11909,COMP4540,Software Engineering Research Project,S2/2017
11908,COMP4500,Software Engineering Practice,S2/2017
11907,COMP4330,Real-Time and Embedded Systems,S2/2017
11906,COMP4006,Computer Science Honours,S2/2017
11905,COMP4005P,Computer Science IV Honours,S2/2017
11904,COMP4005F,Computer Science IV Honours,S2/2017
11903,COMP3900,HCI Design and Evaluation,S2/2017
11902,COMP3820,Software Engineering Internship,S2/2017
11901,COMP3740,Project Work in Computing,S2/2017
11900,COMP3710,Topics in Computer Science,S2/2017
11899,COMP3700,Topics in Software Engineering,S2/2017
11898,COMP3610,Principles of Programming Languages,S2/2017
11897,COMP3600,Algorithms,S2/2017
11896,COMP3560,Advanced Computing R&amp;D Industry Experience,S2/2017
11895,COMP3550,Advanced Computing R&amp;D Project,S2/2017
11894,COMP3500,Software Engineering Project (Part B),S2/2017
11893,COMP3100,Software Engineering Group Project,S2/2017
11892,COMP3006,Computer Science Research Project,S2/2017
11891,COMP2610,Information Theory,S2/2017
11890,COMP2600,Formal Methods in Software Engineering,none/0
11889,COMP2560,Studies in Advanced Computing R&amp;D,S2/2017
11888,COMP2400,Relational Databases  ,S2/2017
11887,COMP2310,Systems Networks and Concurrency,S2/2017
11886,COMP2130,Software Analysis &amp; Design,S2/2017
11885,COMP1730,Programming for Scientists,S2/2017
11884,COMP1720,Art and Interaction in New Media,S2/2017
11883,COMP1510,Introduction to Software Engineering ,none/0
11882,COMP1140,Structured Programming (Advanced),S2/2017
11881,COMP1110,Structured Programming,S2/2017
11880,COMP1040,The Craft of Computing,S2/2017
11879,ANUC1100,Introduction to Programming and Algorithms,S2/2017
11878,COMP3820,Software Engineering Internship,S1/2017
11877,COMP2140,Java Programming,S1/2017
11876,ANUC1710,Web Development and Design,S1/2017
11875,ANUC1110,Introduction to Software Systems,S1/2017
11874,ANUC1100,Introduction to Programming and Algorithms,S1/2017
11873,COMP1030,Art of Computing,S1/2017
11872,VCUG3001,Unravelling Complexity,S1/2017
11871,VCUG1001,The Art of Computing,S1/2017
11870,PHIL2080,Logic,S1/2017
11869,LAWS3001,Unravelling Complexity,S1/2017
11868,INFT4005P,"Information Technology Honours,Parttime",none/0
11867,INFT4005F,"Information Technology Honours,Fulltime",none/0
11866,ENGN2219,Computing for Engineering Simulation,S1/2017
11865,DART8004,Formal Structures for New Media 1,S1/2017
11864,COMP9000P,(Unknown),S1/2017
11863,COMP9000F,(Unknown),S1/2017
11862,COMP8900P,(Unknown),S1/2017
11861,COMP8900F,(Unknown),S1/2017
11860,COMP8800,Computing Research Project,S1/2017
11858,COMP8780,Information &amp;Human Centered Computing Project,none/0
11855,COMP8715,Computing Project,S1/2017
11854,COMP8705,Communication for Computing Professionals,none/0
11853,COMP8701,Communication for Computing Professionals I,none/0
11852,COMP8600,Introduction to Statistical Machine Learning,S1/2017
11851,COMP8410,Data Mining,Aut/2017
11850,COMP8300,Parallel Systems,S1/2017
11849,COMP8200,Master of Computing Honours Results,S1/2017
11848,COMP8100,Requirements Elicitation and Analysis Techniques,S1/2017
11847,COMP7310,ICT Sustainability,S1/2017
11846,COMP6780,Web Development and Design,S1/2017
11845,COMP6719,Computing for Engineering Simulation,S1/2017
11844,COMP6700,Introductory Programming,S1/2017
11843,COMP6470,Special Topics in Computing,S1/2017
11842,COMP6442,Software Construction,S1/2017
11841,COMP6365,System Architectural Understanding &amp; the Human Brain,S1/2017
11840,COMP6353,Systems Engineering for Software Engineers,S1/2017
11839,COMP6340,Networked Information Systems,S1/2017
11838,COMP6320,Artificial Intelligence,S1/2017
11837,COMP6300,Introduction to Computer Systems,S1/2017
11836,COMP6262,Logic,S1/2017
11835,COMP4801,Honours Result,S1/2017
11834,COMP4800,Industrial Experience,S1/2017
11833,COMP4670,Introduction to Statistical Machine Learning,S1/2017
11832,COMP4560,Advanced Computing Project,S1/2017
11831,COMP4550,Advanced Computing Research Project,S1/2017
11830,COMP4540,Software Engineering Research Project,S1/2017
11829,COMP4500,Software Engineering Practice,S1/2017
11828,COMP4300,Parallel Systems,S1/2017
11827,COMP4130,Managing Software Quality and Process,S1/2017
11826,COMP4006,Computer Science Honours,S1/2017
11825,COMP4005P,"Computing Science Honours,Parttime",none/0
11824,COMP4005F,Computer Science Honours,none/0
11823,COMP3740,Project Work in Computing,S1/2017
11822,COMP3710,Topics in Computer Science,S1/2017
11821,COMP3700,Topics in Software Engineering,S1/2017
11820,COMP3650,System Architectural Understanding &amp; the Human Brain,S1/2017
11819,COMP3620,Artificial Intelligence,S1/2017
11818,COMP3550,Advanced Computing R&amp;D Project,S1/2017
11817,COMP3530,System Engineering for Software Engineers,S1/2017
11816,COMP3500,Software Engineering Project (Part A),S1/2017
11815,COMP3420,Advanced Databases and Data Mining,none/0
11814,COMP3120,Managing Software Development,S1/2017
11813,COMP3100,Software Engineering Group Project,none/0
11812,COMP2620,Logic,S1/2017
11811,COMP2550,Advanced Computing R&amp;D Methods,S1/2017
11810,COMP2500,Software Construction for Software Engineers,none/0
11809,COMP2410,Networked Information Systems,S1/2017
11808,COMP2300,Computer Organisation and Program Execution,S1/2017
11807,COMP2100,Software Design Methodologies,S1/2017
11806,COMP1710,Web Development and Design,S1/2017
11805,COMP1130,Programming as Problem Solving (Advanced),S1/2017
11804,COMP1100,Programming as Problem Solving,S1/2017
11803,ASGS1017,"New Media, the Web &amp; its tools",none/0
11802,COMP8430,Data Wrangling,Sum/2017
11801,COMP7240,Introduction to Database Concepts,Sum/2017
11799,COMPSPPC,South Pacific Programming Contest,S2/2016
11798,COMP3560,Advanced Computing R&amp;D Industry Experience,S1/2016
11797,COMP2420,"Introduction to Data Management, Analysis and Security",S1/2018
11796,COMP3770,Individual Research Project,S1/2017
11795,COMP8755,Individual Computing Project,S1/2017
11794,COMP1600,Foundations of Computing,S2/2017
11791,COMP3560,Advanced Computing R&amp;D Industry Experience,S2/2016
11790,ENGN8160,Professional Communication II,S1/2016
11788,COMP8705,Communication for Computing Professionals II,S2/2016
11787,COMP8701,Communication for Computing Professionals I,S2/2016
11786,COMP3710,Topics in Computer Science,Spr/2015
11785,COMP8715,Computing Project,S2/2016
11784,COMP7230,Introduction to Programming for Data Scientists,Win/2016
11783,COMP8715,Computing Project,Sum/2016
11782,EXTN1005A,ANU Extension Engineering,Aut/2016
11781,COMP1040,The Craft of Computing,S2/2016
11780,ANUC1710,Web Development and Design,S1/2016
11779,ANUC1110,Introduction to Software Systems,S1/2016
11778,ANUC1100,Introduction to Programming and Algorithms,S1/2016
11777,COMP6470,Special Topics in Computing,Sum/2015
11776,COMP8715,Computing Project,Sum/2015
11774,COMP3710,Topics in Computer Science,S1/2016
11773,ANUC2400,Relational Databases,S1/2016
11772,COMP4450,Advanced Computing Research Methods,S2/2016
11771,COMP4450,Advanced Computing R&amp;D Methods,S1/2016
11769,COMP8440,Free &amp; Open Source Software Development,Aut/2016
11768,COMP2140,Java Programming,S1/2016
11767,COMP1030,Art of Computing,S1/2016
11766,COMP3560,Advanced Computing R&amp;D Industry Experience,S2/2015
11764,COMPSPPC,South Pacific Programming Contest,S2/2015
11763,COMP8701,Communication for Computing Professionals I,S2/2015
11760,ANUC1100,Introduction to Programming and Algorithms,S2/2015
11759,COMP3550,Advanced Computing R&amp;D Project,S2/2015
11758,COMP8715,Computing Project,S2/2015
11756,COMP1040,The Craft of Computing,S2/2015
11755,COMP8180,Systems and Software Safety,Aut/2016
11754,COMP3560,Advanced Computing R&amp;D Industry Experience,Sum/2016
11753,COMP8900P,(Unknown),S1/2016
11752,COMP8900F,(Unknown),S1/2016
11751,COMP8715,Computing Project,S1/2016
11750,COMP8705,Communication for Computing Professionals II,S1/2016
11749,COMP8701,Communication for Computing Professionals I,S1/2016
11748,COMP6780,Web Development and Design,S1/2016
11747,INFT4005P,"Information Technology Honours,Parttime",S2/2016
11746,INFT4005F,"Information Technology Honours,Fulltime",S2/2016
11745,ENGN8160,Professional Communication II,S2/2016
11744,COMP8800,Computing Research Project,S2/2016
11739,COMP8650,Advanced Topics in Statistical Machine Learning,S2/2016
11738,COMP8460,Advanced Algorithms,S2/2016
11737,COMP8200,Master of Computing Honours Results,S2/2016
11736,COMP8190,Model-Driven Software Development,S2/2016
11735,COMP8110,Managing Software Projects in a System Context,S2/2016
11734,COMP6730,Introductory Programming for Scientists,S2/2016
11733,COMP6720,Art and Interaction in New Media,S2/2016
11732,COMP6710,Structured Programming,S2/2016
11731,COMP6490,Document Analysis,S2/2016
11730,COMP6470,Special Topics in Computing,S2/2016
11729,COMP6466,Algorithms,S2/2016
11728,COMP6390,HCI and Usability Engineering,S2/2016
11727,COMP6330,Operating Systems Implementation,S2/2016
11726,COMP6311,Software Analysis and Design,S2/2016
11725,COMP6310,"Systems, Networks and Concurrency",S2/2016
11724,COMP6261,Information Theory,S2/2016
11723,COMP6260,Formal Methods in Software Engineering,S2/2016
11722,COMP6240,Relational Databases,S2/2016
11721,COMP4801,Honours Result,S2/2016
11720,COMP4800,Industrial Experience,S2/2016
11719,COMP4710,Topics in Software Engineering III ,S2/2016
11718,COMP4680,Advanced Topics in Statistical Machine Learning,S2/2016
11717,COMP4650,Document Analysis,S2/2016
11716,COMP4600,Advanced Algorithms,S2/2016
11715,COMP4560,Advanced Computing Project,S2/2016
11714,COMP4550,Advanced Computing Research Project,S2/2016
11713,COMP4540,Software Engineering Research Project,S2/2016
11712,COMP4500,Software Engineering Practice,S2/2016
11711,COMP4006,Computer Science Honours,S2/2016
11710,COMP4005P,Computer Science IV Honours,S2/2016
11709,COMP4005F,Computer Science IV Honours,S2/2016
11708,COMP3900,HCI and Usability Engineering,S2/2016
11707,COMP3820,Software Engineering Internship,S2/2016
11706,COMP3740,Project Work in Computing,S2/2016
11705,COMP3710,Topics in Computer Science,S2/2016
11703,COMP3600,Algorithms,S2/2016
11702,COMP3550,Advanced Computing R&amp;D Project,S2/2016
11701,COMP3500,Software Engineering Project,S2/2016
11700,COMP3300,Operating Systems Implementation,S2/2016
11699,COMP3100,Software Engineering Group Project,S2/2016
11698,COMP2610,Information Theory,S2/2016
11697,COMP2600,Formal Methods in Software Engineering,S2/2016
11696,COMP2560,Studies in Advanced Computing R&amp;D,S2/2016
11695,COMP2400,Relational Databases  ,S2/2016
11694,COMP2310,"Systems, Networks and Concurrency",S2/2016
11693,COMP2130,Software Analysis &amp; Design,S2/2016
11692,COMP1730,Programming for Scientists,S2/2016
11691,COMP1720,Art and Interaction in New Media,S2/2016
11690,COMP1510,Introduction to Software Engineering ,S2/2016
11689,COMP1140,Structured Programming (Advanced),S2/2016
11688,COMP1110,Structured Programming,S2/2016
11687,PHIL2080,Logic,S1/2016
11686,INFT4005P,"Information Technology Honours,Parttime",S1/2016
11685,INFT4005F,"Information Technology Honours,Fulltime",S1/2016
11684,ENGN2219,Computing for Engineering Simulation,S1/2016
11683,DART8004,Formal Structures for New Media 1,S1/2016
11682,COMP8800,Computing Research Project,S1/2016
11681,COMP8790,Software Engineering Project,S1/2016
11680,COMP8780,Information &amp;Human Centered Computing Project,S1/2016
11679,COMP8750,Computer &amp; Programming Language Systems Project,S1/2016
11678,COMP8740,Artificial Intelligence Project,S1/2016
11677,COMP8600,Introduction to Statistical Machine Learning,S1/2016
11676,COMP8420,Bio-inspired Computing: Applications and Interfaces,S1/2016
11675,COMP8400,Algorithms for Data Mining,S1/2016
11674,COMP8200,Master of Computing Honours Results,S1/2016
11673,COMP7310,ICT Sustainability,S1/2016
11672,COMP6719,Computing for Engineering Simulation,S1/2016
11671,COMP6700,Introductory Programming,S1/2016
11670,COMP6470,Special Topics in Computing,S1/2016
11669,COMP6464,High Performance Scientific Computation,S1/2016
11668,COMP6442,Software Design Methodologies,S1/2016
11667,COMP6363,Theory of Computation,S1/2016
11666,COMP6353,Systems Engineering for Software Engineers,S1/2016
11665,COMP6340,Networked Information Systems,S1/2016
11664,COMP6331,Computer Networks,S1/2016
11663,COMP6320,Artificial Intelligence,S1/2016
11662,COMP6300,Computer Organisation and Program Execution,S1/2016
11661,COMP6262,Logic,S1/2016
11660,COMP4801,Honours Result,S1/2016
11659,COMP4800,Industrial Experience,S1/2016
11658,COMP4670,Introduction to Statistical Machine Learning,S1/2016
11657,COMP4660,Bio-inspired Computing: Applications and Interfaces,S1/2016
11656,COMP4560,Advanced Computing Project,S1/2016
11655,COMP4550,Advanced Computing Research Project,S1/2016
11654,COMP4540,Software Engineering Research Project,S1/2016
11653,COMP4500,Software Engineering Practice,S1/2016
11652,COMP4130,Managing Software Quality and Process,S1/2016
11651,COMP4006,Computer Science Honours,S1/2016
11650,COMP4005P,"Computing Science Honours,Parttime",S1/2016
11649,COMP4005F,Computer Science Honours,S1/2016
11648,COMP3740,Project Work in Computing,S1/2016
11647,COMP3630,Theory of Computation,S1/2016
11646,COMP3620,Artificial Intelligence,S1/2016
11645,COMP3550,Advanced Computing R&amp;D Project,S1/2016
11644,COMP3530,Systems Engineering for Software Engineers,S1/2016
11643,COMP3500,Software Engineering Project (Part A),S1/2016
11642,COMP3420,Advanced Databases and Data Mining,S1/2016
11641,COMP3320,High Performance Scientific Computation,S1/2016
11640,COMP3310,Computer Networks,S1/2016
11639,COMP3120,Managing Software Development,S1/2016
11638,COMP3100,Software Engineering Group Project,S1/2016
11637,COMP2620,Logic,S1/2016
11636,COMP2550,Advanced Computing R&amp;D Methods,S1/2016
11635,COMP2500,Software Construction for Software Engineers,S1/2016
11634,COMP2410,Networked Information Systems,S1/2016
11633,COMP2300,Computer Organisation and Program Execution,S1/2016
11632,COMP2100,Software Design Methodologies,S1/2016
11631,COMP1710,Web Development and Design,S1/2016
11630,COMP1130,Programming as Problem Solving (Advanced),S1/2016
11629,COMP1100,Programming as Problem Solving,S1/2016
11628,ASGS1017,"New Media, the Web &amp; its tools",S1/2016
11627,COMP8701,Communication for Computing Professionals I,S1/2015
11625,COMP9000P,(Unknown),S2/2015
11624,COMP9000F,(Unknown),S2/2015
11623,COMP8900P,(Unknown),S2/2015
11622,COMP8900F,(Unknown),S2/2015
11621,COMP3710,Topics in Computer Science,Sum/2015
11620,COMP3560,Advanced Computing R&amp;D Industry Experience,Sum/2015
11619,COMP8715,Computing Project,S1/2015
11618,COMP3550,Advanced Computing R&amp;D Project,S1/2015
11617,COMP6780,Web Development and Design,S1/2015
11616,COMP8670,Advanced Topics in Logic and Computation,S2/2015
11615,COMP8330,Real-Time Embedded Systems,S2/2015
11614,COMP8300,Parallel Systems,S1/2015
11613,COMP4650,Document Analysis,S2/2015
11612,COMP6461,Computer Graphics,S2/2015
11611,COMP8705,Communication for Computing Professionals,S2/2015
11610,VCUG1001,The Art of Computing,S1/2015
11609,COMP8173,Software Engineering Processes,Win/2015
11608,COMP4610,Computer Graphics,S2/2015
11607,COMP4610,Computer Graphics,S2/2012
11606,COMP6262,Logic,S1/2015
11605,COMP6261,Information Theory,S2/2015
11604,COMP8600,Introduction to Statistical Machine Learning,S1/2015
11603,ENGN8160,Professional Communication II,S2/2014
11600,COMP6261,Information Theory,S2/2014
11599,COMP8190,Model-Driven Software Development,S2/2014
11598,COMP3710,Topics in Computer Science,Spr/2013
11597,COMP6330,Operating Systems Implementation,S2/2014
11596,COMP3300,Operating Systems Implementation,S2/2014
11594,INFT4005P,"Information Technology Honours,Parttime",S2/2015
11593,INFT4005F,"Information Technology Honours,Fulltime",S2/2015
11592,COMP8800,Computing Research Project,S2/2015
11591,COMP8790,Software Engineering Project,S2/2015
11590,COMP8780,Information &amp; Human Centred Computer Project,S2/2015
11589,COMP8750,Computer Systems Project,S2/2015
11588,COMP8740,Artificial Intelligence Project,S2/2015
11587,COMP8650,Advanced Topics in Statistical Machine Learning,S1/1992
11586,COMP8200,Master of Computing Honours Results,S2/2015
11584,COMP6730,Introductory Programming for Scientists,S2/2015
11583,COMP6720,Art Interaction and New Media,S2/2015
11582,COMP6710,Introduction to Software Systems,S2/2015
11581,COMP6490,Document Analysis,S2/2015
11580,COMP6470,Special Topics in Computing,S2/2015
11579,COMP6466,Algorithms,S2/2015
11577,COMP6390,HCI Design and Evaluation,S2/2015
11576,COMP6311,Software Analysis and Design,S2/2015
11575,COMP6310,Concurrent &amp; Distributed Systems,S2/2015
11574,COMP6260,Formal Methods in Software Engineering,S2/2015
11573,COMP6240,Relational Databases,S2/2015
11572,COMP4801,Software Engineering Honours Results,S2/2015
11571,COMP4800,Industrial Experience,S2/2015
11570,COMP4710,Topics in Software Engineering III ,S2/2015
11566,COMP4630,Advanced Topics in Logic and Computation,S2/2015
11563,COMP4560,Advanced Computing Project,S2/2015
11562,COMP4550,Advanced Computing Research Project,S2/2015
11561,COMP4540,Software Engineering Research Project,S2/2015
11560,COMP4500,Software Engineering Practice,S2/2015
11559,COMP4006,Computer Science Honours,S2/2015
11558,COMP4005P,Computer Science IV Honours,S2/2015
11557,COMP4005F,Computer Science IV Honours,S2/2015
11556,COMP3900,HCI Design and Evaluation,S2/2015
11555,COMP3820,Software Engineering Internship,S2/2015
11554,COMP3740,Project Work in Computing,S2/2015
11553,COMP3710,Topics in Computer Science,S2/2015
11552,COMP3700,Topics in Software Engineering,S2/2015
11550,COMP3600,Algorithms,S2/2015
11549,COMP3500,Software Engineering Project (Part B),S2/2015
11548,COMP3100,Software Engineering Group Project,S2/2015
11547,COMP3006,Computer Science Research Project,S2/2015
11546,COMP2610,Information Theory,S2/2015
11545,COMP2600,Formal Methods in Software Engineering,S2/2015
11544,COMP2560,Studies in Advanced Computing R&amp;D,S2/2015
11543,COMP2400,Relational Databases  ,S2/2015
11542,COMP2310,Concurrent and Distributed Systems,S2/2015
11541,COMP2130,Software Analysis &amp; Design,S2/2015
11540,COMP1730,Introductory Programming for Scientists,S2/2015
11539,COMP1720,Art and Interaction in New Media,S2/2015
11538,COMP1510,Introduction to Software Engineering ,S2/2015
11537,COMP1140,Introduction to Software Systems (Advanced),S2/2015
11536,COMP1110,Introduction to Software Systems,S2/2015
11534,COMP8180,Systems and Software Safety,S1/1992
11533,PHIL2080,Logic,S1/2015
11532,INFT4005P,"Information Technology Honours,Parttime",S1/2015
11531,INFT4005F,"Information Technology Honours,Fulltime",S1/2015
11530,ENGN2219,Computing for Engineering Simulation,S1/2015
11529,DART8004,Formal Structures for New Media 1,S1/2015
11528,COMP8800,Computing Research Project,S1/2015
11527,COMP8790,Software Engineering Project,S1/2015
11526,COMP8780,Information &amp;Human Centered Computing Project,S1/2015
11525,COMP8750,Computer &amp; Programming Language Systems Project,S1/2015
11524,COMP8740,Artificial Intelligence Project,S1/2015
11521,COMP8400,Algorithms for Data Mining,S1/2015
11520,COMP8200,Master of Computing Honours Results,S1/2015
11519,COMP7310,Green Information Technology Strategies,S1/2015
11518,COMP6719,Computing for Engineering Simulation,S1/2015
11517,COMP6700,Introductory Programming In Java,S1/2015
11516,COMP6470,Special Topics in Computing,S1/2015
11514,COMP6442,Software Construction,S1/2015
11512,COMP6353,Systems Engineering for Software Engineers,S1/2015
11511,COMP6340,Networked Information Systems,S1/2015
11509,COMP6320,Artificial Intelligence,S1/2015
11508,COMP6300,Introduction to Computer Systems,S1/2015
11507,COMP4801,Honours Result,S1/2015
11506,COMP4800,Industrial Experience,S1/2015
11504,COMP4670,Introduction to Statistical Machine Learning,S1/2015
11501,COMP4560,Advanced Computing Project,S1/2015
11500,COMP4550,Advanced Computing Research Project,S1/2015
11499,COMP4540,Software Engineering Research Project,S1/2015
11498,COMP4500,Software Engineering Practice,S1/2015
11496,COMP4130,Managing Software Quality and Process,S1/2015
11495,COMP4006,Computer Science Honours,S1/2015
11494,COMP4005P,"Computing Science Honours,Parttime",S1/2015
11493,COMP4005F,Computer Science Honours,S1/2015
11492,COMP3740,Project Work in Computing,S1/2015
11489,COMP3620,Artificial Intelligence,S1/2015
11488,COMP3530,System Engineering for Software Engineers,S1/2015
11487,COMP3500,Software Engineering Project (Part A),S1/2015
11486,COMP3420,Advanced Databases and Data Mining,S1/2015
11485,COMP3120,Managing Software Development,S1/2015
11484,COMP3100,Software Engineering Group Project,S1/2015
11483,COMP2620,Logic,S1/2015
11482,COMP2550,Advanced Computing R&amp;D Methods,S1/2015
11481,COMP2500,Software Construction for Software Engineers,S1/2015
11480,COMP2410,Networked Information Systems,S1/2015
11479,COMP2300,Introduction to Computer Systems,S1/2015
11478,COMP2100,Software Construction,S1/2015
11477,COMP1710,Web Development and Design,S1/2015
11476,COMP1130,Introduction to Programming and Algorithms (Advanced),S1/2015
11475,COMP1100,Introduction to Programming and Algorithms,S1/2015
11474,ASGS1017,"New Media, the Web &amp; its tools",S1/2015
11472,COMP8705,Communication for Computing Professionals,S1/2015
11471,COMP8180,Systems and Software Safety,Aut/2014
11470,COMP8460,Advanced Algorithms,S2/2014
11469,COMP8440,Free &amp; Open Source Software Development,Aut/2014
11468,INFT4005P,"Information Technology Honours,Parttime",S2/2014
11467,INFT4005F,"Information Technology Honours,Fulltime",S2/2014
11465,COMP8800,Computing Research Project,S2/2014
11464,COMP8790,Software Engineering Project,S2/2014
11463,COMP8780,Information &amp; Human Centred Computer Project,S2/2014
11462,COMP8750,Computer Systems Project,S2/2014
11461,COMP8740,Artificial Intelligence Project,S2/2014
11460,COMP8650,Advanced Topics in Statistical Machine Learning,S2/2014
11459,COMP8620,Advanced Topics in Artificial Intelligence,S2/2015
11458,COMP8200,Master of Computing Honours Results,S2/2014
11457,COMP8110,Managing Software Projects in a System Context,S2/2014
11456,COMP6730,Introductory Programming for Scientists,S2/2014
11455,COMP6720,Art Interaction and New Media,S2/2014
11454,COMP6710,Introduction to Software Systems,S2/2014
11453,COMP6490,Document Analysis,S2/2014
11452,COMP6470,Special Topics in Computing,S2/2014
11451,COMP6466,Algorithms,S2/2014
11450,COMP6463,Overview of Logic &amp; Computation,S1/1992
11449,COMP6433,Real-time Embedded Systems,S2/2015
11448,COMP6390,HCI Design and Evaluation,S2/2014
11447,COMP6361,Principles of Programming Languages,S2/2015
11446,COMP6311,Software Analysis and Design,S2/2014
11445,COMP6310,Concurrent &amp; Distributed Systems,S2/2014
11444,COMP6260,Formal Methods in Software Engineering,S2/2014
11443,COMP6240,Relational Databases,S2/2014
11442,COMP4801,Honours Result,S2/2014
11441,COMP4800,Industrial Experience,S2/2014
11440,COMP4710,Topics in Software Engineering III ,S2/2014
11439,COMP4680,Advanced Topics in Statistical Machine Learning,S2/2014
11438,COMP4650,Document Analysis,S2/2014
11435,COMP4620,Advanced Topics in Artifical Intelligence,S2/2015
11433,COMP4600,Advanced Algorithms,S2/2014
11432,COMP4560,Advanced Computing Project,S2/2014
11431,COMP4550,Advanced Computing Research Project,S2/2014
11430,COMP4540,Software Engineering Research Project,S2/2014
11429,COMP4500,Software Engineering Practice,S2/2014
11428,COMP4330,Real-Time and Embedded Systems,S2/2015
11427,COMP4006,Computer Science Honours,S2/2014
11426,COMP4005P,Computer Science IV Honours,S2/2014
11425,COMP4005F,Computer Science IV Honours,S2/2014
11424,COMP3900,HCI Design and Evaluation,S2/2014
11423,COMP3820,Software Engineering Internship,S2/2014
11422,COMP3740,Project Work in Computing,S2/2014
11421,COMP3710,Topics in Computer Science,S2/2014
11420,COMP3700,Topics in Software Engineering,S2/2014
11418,COMP3610,Principles of Programming Languages,S2/2015
11417,COMP3600,Algorithms,S2/2014
11416,COMP3500,Software Engineering Project (Part B),S2/2014
11415,COMP3100,Software Engineering Group Project,S2/2014
11413,COMP2610,Information Theory,S2/2014
11412,COMP2600,Formal Methods in Software Engineering,S2/2014
11411,COMP2560,Studies in Advanced Computing R&amp;D,S2/2014
11410,COMP2400,Relational Databases  ,S2/2014
11409,COMP2310,Concurrent and Distributed Systems,S2/2014
11408,COMP2130,Software Analysis &amp; Design,S2/2014
11407,COMP1730,Introductory Programming for Scientists,S2/2014
11406,COMP1720,Art and Interaction in New Media,S2/2014
11405,COMP1510,Introduction to Software Engineering ,S2/2014
11404,COMP1140, Introduction to Advanced Computing II,S2/2014
11403,COMP1110,Introduction to Software Systems,S2/2014
11402,COMP3550,Advanced Computing R&amp;D Project,S2/2014
11401,COMP3550,Advanced Computing R&amp;D Project,S1/2014
11400,COMP6262,Logic,S1/2014
11398,COMP8600,Introduction to Statistical Machine Learning,S1/2014
11397,VCUG3001,Unravelling Complexity,S1/2015
11395,PHIL2080,Logic,S1/2014
11394,LAWS3001,Unravelling Complexity,S1/2015
11393,INFT4005P,"Information Technology Honours,Parttime",S1/2014
11392,INFT4005F,"Information Technology Honours,Fulltime",S1/2014
11391,ENGN2219,Computing for Engineering Simulation,S1/2014
11390,DART8004,Formal Structures for New Media 1,S1/2014
11389,COMP9000P,(Unknown),S1/2015
11388,COMP9000F,(Unknown),S1/2015
11387,COMP8900P,(Unknown),S1/2015
11386,COMP8900F,(Unknown),S1/2015
11385,COMP8800,Computing Research Project,S1/2014
11384,COMP8790,Software Engineering Project,S1/2014
11383,COMP8780,Information &amp;Human Centered Computing Project,S1/2014
11382,COMP8750,Computer &amp; Programming Language Systems Project,S1/2014
11381,COMP8740,Artificial Intelligence Project,S1/2014
11380,COMP8420,Bio-inspired Computing,S1/2014
11378,COMP8400,Algorithms for Data Mining,S1/2014
11377,COMP8200,Master of Computing Honours Results,S1/2014
11376,COMP8100,Requirements Elicitation and Analysis Techniques,S1/2015
11375,COMP7310,Green Information Technology Strategies,S1/2014
11374,COMP6719,Computing for Engineering Simulation,S1/2014
11373,COMP6700,Introductory Programming In Java,S1/2014
11372,COMP6470,Special Topics in Computing,S1/2014
11370,COMP6442,Software Construction,S1/2014
11368,COMP6363,Theory of Computation,S1/2014
11367,COMP6353,Systems Engineering for Software Engineers,S1/2014
11366,COMP6340,Networked Information Systems,S1/2014
11364,COMP6320,Artificial Intelligence,S1/2014
11363,COMP6300,Introduction to Computer Systems,S1/2014
11362,COMP4801,Honours Result,S1/2014
11361,COMP4800,Industrial Experience,S1/2014
11358,COMP4670,Introduction to Statistical Machine Learning,S1/2014
11356,COMP4660,Bio-Inspired Computing,S1/2014
11355,COMP4560,Advanced Computing Project,S1/2014
11354,COMP4550,Advanced Computing Research Project,S1/2014
11353,COMP4540,Software Engineering Research Project,S1/2014
11352,COMP4500,Software Engineering Practice,S1/2014
11350,COMP4300,Parallel Systems,S1/2015
11348,COMP4130,Managing Software Quality and Process,S1/2014
11347,COMP4006,Computer Science Honours,S1/2014
11346,COMP4005P,"Computing Science Honours,Parttime",S1/2014
11345,COMP4005F,Computer Science Honours,S1/2014
11344,COMP3740,Project Work in Computing,S1/2014
11342,COMP3710,Topics in Computer Science,S1/2015
11341,COMP3700,Topics in Software Engineering,S1/2015
11340,COMP3630,Theory of Computation,S1/2014
11338,COMP3620,Artificial Intelligence,S1/2014
11337,COMP3530,System Engineering for Software Engineers,S1/2014
11336,COMP3500,Software Engineering Project (Part A),S1/2014
11335,COMP3420,Advanced Databases and Data Mining,S1/2014
11333,COMP3120,Managing Software Development,S1/2014
11332,COMP3100,Software Engineering Group Project,S1/2014
11331,COMP2620,Logic,S1/2014
11330,COMP2550,Advanced Computing R&amp;D Methods,S1/2014
11329,COMP2500,Software Construction for Software Engineers,S1/2014
11328,COMP2410,Networked Information Systems,S1/2014
11327,COMP2300,Introduction to Computer Systems,S1/2014
11326,COMP2100,Software Construction,S1/2014
11325,COMP1710,Web Development and Design,S1/2014
11324,COMP1130,Introduction to Advanced Computing I,S1/2014
11323,COMP1100,Introduction to Programming and Algorithms,S1/2014
11322,ASGS1017,"New Media, the Web &amp; its tools",S1/2014
11321,COMPSPPC,South Pacific Programming Contest,S2/2013
11319,COMP3610H,Principles of Programming Languages,S2/2013
11318,COMP4630H,Overview of Logic &amp; Computation (HONS),S2/2013
11317,COMP4600H,Advanced Algorithms (HONS),S2/2013
11315,COMP1510,Introduction to Software Engineering ,S2/2013
11314,COMP1140, Introduction to Advanced Computing II,S2/2013
11313,COMP1110,Introduction to Software Systems,S2/2013
11310,COMP4130H,"Managing Software Quality and Process,Honours",S1/2013
11309,COMP4660H,"Bio Inspired Computing,Honours",S1/2013
11307,COMP8400H,"Algorithms and Techniques for Data Mining,Honours",S1/2013
11306,COMP4300H,"Parallel Systems,Honours",S1/2013
11305,COMP6353,Systems Engineering for Software Engineers,S1/2013
11304,COMP8800,Computing Research Project,S2/2013
11303,COMP8790,Software Engineering Project,S2/2013
11302,COMP8780,Information &amp; Human Centred Computer Project,S2/2013
11301,COMP8750,Computer Systems Project,S2/2013
11300,COMP8740,Artificial Intelligence Project,S2/2013
11299,COMP8650,Advanced Topics in Statistical Machine Learning,S2/2013
11298,COMP8620,Advanced Topics in Artificial Intelligence,S2/2013
11297,COMP8200,Master of Computing Honours Results,S2/2013
11296,COMP8173,Software Engineering Processes,Win/2013
11295,COMP8110,Managing Software Projects in a System Context,S2/2013
11294,COMP6730,Introductory Programming for Scientists,S2/2013
11293,COMP6720,Art Interaction and New Media,S2/2013
11292,COMP6710,Introduction to Software Systems,S2/2013
11291,COMP6490,Document Analysis,S2/2013
11290,COMP6470,Special Topics in Computing,S2/2013
11289,COMP6466,Algorithms,S2/2013
11288,COMP6463,Overview of Logic &amp; Computation,S2/2013
11287,COMP6433,Real-time Embedded Systems,S2/2013
11286,COMP6390,HCI Design and Evaluation,S2/2013
11285,COMP6361,Principles of Programming Languages,S2/2013
11284,COMP4801,Software Engineering Honours Results,S2/2013
11283,COMP4800,Industrial Experience,S2/2013
11282,COMP4710,Topics in Software Engineering III ,S2/2013
11281,COMP4680,Advanced Topics in Statistical Machine Learning,S2/2013
11280,COMP4650,Document Analysis,S2/2013
11279,COMP4630,Overview of Logic &amp; Computation,S2/2013
11278,COMP4620,Advanced Topics in Artifical Intelligence,S2/2013
11277,COMP4600,Advanced Algorithms,S2/2013
11276,COMP4560,Advanced Computing Project,S2/2013
11275,COMP4550,Advanced Computing Research Project,S2/2013
11274,COMP4540,Software Engineering Research Project,S2/2013
11273,COMP4500,Software Engineering Practice,S2/2013
11272,COMP4330,Real-Time and Embedded Systems,S2/2013
11271,COMP4006,Computer Science Honours,S2/2013
11270,COMP3820,Software Engineering Internship,S2/2013
11269,COMP3740,Project Work in Computing,S2/2013
11268,COMP3700,Topics in Software Engineering,S2/2013
11267,COMP3610,Principles of Programming Languages,S2/2013
11266,COMP3600,Algorithms,S2/2013
11265,COMP3100,Software Engineering Group Project,S2/2013
11264,COMP3500,Software Engineering Project (Part B),S2/2013
11263,COMP3006,Computer Science Research Project,S2/2013
11262,COMP2610,Information Theory,S2/2013
11261,COMP2600,Formal Methods in Software Engineering,S2/2013
11260,COMP2400,Relational Databases  ,S2/2013
11259,COMP2310,Concurrent and Distributed Systems,S2/2013
11258,COMP2130,Software Analysis &amp; Design,S2/2013
11257,COMP1730,Introductory Programming for Scientists,S2/2013
11256,COMP1720,Art and Interaction in New Media,S2/2013
11255,COMP6430,Parallel Systems,S1/2013
11254,INFT4005P,"Information Technology Honours,Parttime",S2/2013
11253,INFT4005F,"Information Technology Honours,Fulltime",S2/2013
11252,COMP4005P,Computer Science IV Honours,S2/2013
11251,COMP4005F,Computer Science IV Honours,S2/2013
11250,COMP3710,Topics in Computer Science,Sum/2013
11249,COMP3710,Topics in Computer Science,S2/2013
11248,COMP6330,Operating Systems Implementation,S1/1992
11247,COMP6311,Software Analysis and Design,S2/2013
11246,COMP6310,Concurrent &amp; Distributed Systems,S2/2013
11245,COMP6260,Formal Methods in Software Engineering,S2/2013
11244,COMP6240,Relational Databases,S2/2013
11243,COMP2560,Studies in Advanced Computing R&amp;D,S2/2013
11242,COMP2550,Advanced Computing R&amp;D Methods,S1/2013
11241,COMP3900,HCI Design and Evaluation,S2/2013
11240,COMP8180,Systems and Software Safety,Aut/2013
11239,COMP8440,Free &amp; Open Source Software Development,Aut/2013
11238,VCPG6001,Unravelling Complexity,S1/2013
11237,LAWS3001,Unravelling Complexity,S1/2013
11236,VCUG3001,Unravelling Complexity,S1/2013
11235,COMP4300,Parallel Systems,S1/2013
11234,COMP6719,Computing for Engineering Simulation,S1/2013
11233,ENGN2219,Computing for Engineering Simulation,S1/2013
11232,PHIL2080,Logic,S1/2013
11231,INFT4005P,"Information Technology Honours,Parttime",S1/2013
11230,INFT4005F,"Information Technology Honours,Fulltime",S1/2013
11229,DART8004,Formal Structures for New Media 1,S1/2013
11228,COMP9000P,(Unknown),S1/2013
11227,COMP9000F,(Unknown),S1/2013
11226,COMP8900P,(Unknown),S1/2013
11225,COMP8900F,(Unknown),S1/2013
11224,COMP8800,Computing Research Project,S1/2013
11223,COMP8790,Software Engineering Project,S1/2013
11222,COMP8780,Information &amp;Human Centered Computing Project,S1/2013
11221,COMP8750,Computer &amp; Programming Language Systems Project,S1/2013
11220,COMP8740,Artificial Intelligence Project,S1/2013
11219,COMP8420,Bio-inspired Computing,S1/2013
11218,COMP8400,Algorithms for Data Mining,S1/2013
11217,COMP8200,Master of Computing Honours Results,S1/2013
11216,COMP8100,Requirements Elicitation and Analysis Techniques,S1/2013
11215,COMP7310,Green Information Technology Strategies,S1/2013
11214,COMP6700,Introductory Programming In Java,S1/2013
11213,COMP6470,Special Topics in Computing,S1/2013
11212,COMP6467,Introduction to Statistical Machine Learning,S1/2013
11211,COMP6464,High Performance Scientific Computation,S1/2014
11210,COMP6442,Software Construction,S1/2013
11209,COMP6363,Theory of Computation,S1/2013
11208,COMP6340,Networked Information Systems,S1/2013
11207,COMP6331,Computer Networks,S1/2014
11206,COMP6320,Artificial Intelligence,S1/2013
11205,COMP6300,Introduction to Computer Systems,S1/2013
11204,COMP4801,Honours Result,S1/2013
11203,COMP4800,Industrial Experience,S1/2013
11202,COMP4710,Topics in Software Engineering III,S1/2013
11200,COMP4670,Introduction to Statistical Machine Learning,S1/2013
11199,COMP4660,Bio-Inspired Computing,S1/2013
11198,COMP4560,Advanced Computing Project,S1/2013
11197,COMP4550,Advanced Computing Research Project,S1/2013
11196,COMP4540,Software Engineering Research Project,S1/2013
11195,COMP4500,Software Engineering Practice,S1/2013
11194,COMP4130,Managing Software Quality and Process,S1/2013
11193,COMP4006,Computer Science Honours,S1/2013
11192,COMP4005P,"Computing Science Honours,Parttime",S1/2013
11191,COMP4005F,Computer Science Honours,S1/2013
11188,COMP3740,Project Work in Computing,S1/2013
11187,COMP3710,Topics in Computer Science,S1/2013
11186,COMP3700,Topics in Software Engineering,S1/2013
11185,COMP3630,Theory of Computation,S1/2013
11184,COMP3620,Artificial Intelligence,S1/2013
11183,COMP3530,System Engineering for Software Engineers,S1/2013
11182,COMP3500,Software Engineering Project (Part A),S1/2013
11181,COMP3420,Advanced Databases and Data Mining,S1/2013
11180,COMP3320,High Performance Scientific Computation,S1/2014
11179,COMP3310,Computer Networks,S1/2014
11178,COMP3130,Computer Science Group Project,S1/2013
11177,COMP3120,Managing Software Development,S1/2013
11176,COMP3100,Software Engineering Group Project,S1/2013
11175,COMP2620,Logic,S1/2013
11174,COMP2500,Software Construction for Software Engineers,S1/2013
11173,COMP2410,Networked Information Systems,S1/2013
11172,COMP2300,Introduction to Computer Systems,S1/2013
11171,COMP2100,Software Construction,S1/2013
11170,COMP1710,Web Development and Design,S1/2013
11169,COMP1130,Introduction to Advanced Computing I,S1/2013
11168,COMP1100,Introduction to Programming and Algorithms,S1/2013
11167,ASGS1017,"New Media, the Web &amp; its tools",S1/2013
11166,COMP6390H,HCI Design and Evaluation (Hons),S2/2012
11165,COMP6463H,Overview of Logic &amp; Computation (HONS),S2/2012
11162,COMP4650H,Document Analysis (Hons),S2/2012
11161,COMP4630H,Overview of Logic &amp; Computation (HONS),S2/2012
11159,COMP9000P,(Unknown),S2/2012
11158,COMP8900P,(Unknown),S2/2012
11157,COMP8900F,(Unknown),S2/2012
11156,COMP9000F,(Unknown),S2/2012
11155,COMP6330H,Operating Systems Implementation (HONS),S2/2012
11154,COMP4620H,Advanced Topics in Artificial Intelligence (HONS),S2/2012
11153,COMP4600H,Advanced Algorithms (HONS),S2/2012
11152,COMP8650H,Statistical Machine Learning (hons),S2/2012
11151,LAWS3001,Unravelling Complexity,S2/2012
11150,VCPG6001,Unravelling Complexity,S2/2012
11149,VCUG3001,Unravelling Complexity,S2/2012
11148,COMP8620,Advanced Topics in Artificial Intelligence,S2/2012
11147,COMP3710,Topics in Computer Science,Sum/2012
11146,COMP8900P,(Unknown),S1/2012
11145,COMP8900F,(Unknown),S1/2012
11144,COMP4630,Overview of Logic &amp; Computation,S2/2012
11143,COMP6490,Document Analysis,S2/2012
11142,ENGN2219,Computing for Engineering Simulation,S2/2012
11135,COMP4560,Advanced Computing Project,S2/2012
11134,COMP4550,Advanced Computing Research Project,S2/2012
11133,COMP4550,Advanced Computing Research Project,S1/2012
11132,COMP4560,Advanced Computing Project,S1/2012
11131,COMP6470,Special Topics in Computing,Sum/2012
11130,COMP6470,Special Topics in Computing,S2/2012
11129,COMP6470,Special Topics in Computing,S1/2012
11128,INFT4005P,"Information Technology Honours,Parttime",S2/2012
11127,COMP4005P,Computer Science IV Honours,S2/2012
11126,COMP1110,Introduction to Software Systems,S2/2012
11125,COMP1140, Introduction to Advanced Computing II,S2/2012
11124,COMP1510,Introduction to Software Engineering ,S2/2012
11123,COMP1720,Art and Interaction in New Media,S2/2012
11122,COMP1730,Introductory Programming for Scientists,S2/2012
11121,COMP2130,Software Analysis &amp; Design,S2/2012
11120,COMP2310,Concurrent and Distributed Systems,S2/2012
11119,COMP2400,Relational Databases  ,S2/2012
11118,COMP2600,Formal Methods in Software Engineering,S2/2012
11117,COMP2610,Information Theory,S2/2012
11116,COMP3006,Computer Science Research Project,S2/2012
11115,COMP3100,Software Engineering Group Project,S2/2012
11114,COMP6330,Operating Systems Implementation,S2/2012
11113,COMP3300,Operating Systems Implementation,S2/2012
11112,COMP3410,Information Technology in Electronic Commerce,S2/2012
11111,COMP3500,Software Engineering Project (Part B),S2/2012
11110,COMP3600,Algorithms,S2/2012
11109,COMP3700,Topics in Software Engineering,S2/2012
11108,COMP3710,Topics in Computer Science,S2/2012
11107,COMP3740,Project Work in Computing,S2/2012
11106,COMP6390,HCI Design and Evaluation,S2/2012
11105,COMP3900,HCI Design and Evaluation,S2/2012
11104,COMP4006,Computer Science Honours,S2/2012
11103,COMP4500,Software Engineering Practice,S2/2012
11102,COMP4540,Software Engineering Research Project,S2/2012
11100,COMP4600,Advanced Algorithms,S2/2012
11099,COMP4620,Advanced Topics in Artifical Intelligence,S2/2012
11098,COMP4650,Document Analysis,S2/2012
11097,COMP4710,Topics in Software Engineering III ,S2/2012
11096,COMP4800,Industrial Experience,S2/2012
11095,COMP4801,Software Engineering Honours Results,S2/2012
11094,COMP6240,Relational Databases,S2/2012
11093,COMP6310,Concurrent &amp; Distributed Systems,S2/2012
11092,COMP6341,Information Technology in Electronic Commerce,S2/2012
11091,COMP6463,Overview of Logic &amp; Computation,S2/2012
11090,COMP6466,Algorithms,S2/2012
11089,COMP6719,Computing for Engineering Simulation,S2/2012
11088,COMP6720,Art Interaction and New Media,S2/2012
11087,COMP6730,Introductory Programming for Scientists,S2/2012
11086,COMP8110,Managing Software Projects in a System Context,S2/2012
11085,COMP8200,Master of Computing Honours Results,S2/2012
11084,COMP8650,Advanced Topics in Statistical Machine Learning,S2/2012
11081,COMP8740,Artificial Intelligence Project,S2/2012
11080,COMP8750,Computer Systems Project,S2/2012
11078,COMP8780,Information &amp; Human Centred Computer Project,S2/2012
11077,COMP8790,Software Engineering Project,S2/2012
11076,COMP8800,Computing Research Project,S2/2012
11075,COMP4005F,Computer Science IV Honours,S2/2012
11074,INFT4005F,"Information Technology Honours,Fulltime",S2/2012
11073,COMP8180,Systems and Software Safety,Aut/2012
11072,COMP8440,Free &amp; Open Source Software Development,Aut/2012
11070,INFT4005P,"Information Technology Honours,Parttime",S1/2012
11069,INFT4005F,"Information Technology Honours,Fulltime",S1/2012
11068,DART8004,Formal Structures for New Media 1,S1/2012
11067,COMP9000P,(Unknown),S1/2012
11066,COMP9000F,(Unknown),S1/2012
11062,COMP6700,Introductory Programming In Java,S1/2012
11060,COMP6311,Software Analysis and Design,S2/2012
11059,COMP4710,Topics in Software Engineering III,S1/2012
11056,ASGS1017,"New Media, the Web &amp; its tools",S1/2012
11055,COMP8320,Multicore Computing,S2/2010
11054,COMP3610,Principles of Programming Languages,S2/2010
11053,COMP4610,Computer Graphics,S2/2010
11052,COMP4330,Real-Time and Embedded Systems,S2/2010
11031,COMP8200,Master of Computing Honours Results,S2/2011
11030,COMP6710,Introduction to Software Systems,S2/2012
11029,COMP6464,High Performance Scientific Computation,S1/2012
11028,COMP3320,High Performance Scientific Computation,S1/2012
11027,COMP6331,Computer Networks,S1/2012
11026,COMP3310,Computer Networks,S1/2012
11025,COMP8190,Model-Driven Software Development,Spr/2012
11024,COMP4660,Bio-Inspired Computing,S1/2012
11023,COMP6490,Document Analysis,S2/2011
11022,COMP6365,System Architectural Understanding &amp; the Human Brain,Aut/2012
11021,COMP3650,System Architectural Understanding &amp; the Human Brain,Aut/2012
11020,PHIL2080,Logic,S1/2012
11019,COMP3530,System Engineering for Software Engineers,S1/2012
11018,COMP3710,Topics in Computer Science,Spr/2011
10991,COMP8800,Computing Research Project,S1/2012
10990,COMP8790,Software Engineering Project,S1/2012
10989,COMP8780,Information &amp;Human Centered Computing Project,S1/2012
10988,COMP8750,Computer &amp; Programming Language Systems Project,S1/2012
10987,COMP8740,Artificial Intelligence Project,S1/2012
10986,COMP8420,Bio-inspired Computing,S1/2012
10985,COMP8400,Algorithms for Data Mining,S1/2012
10984,COMP8200,Master of Computing Honours Results,S1/2012
10983,COMP8100,Requirements Elicitation and Analysis Techniques,S1/2012
10982,COMP7310,Green Information Technology Strategies,S1/2012
10981,COMP6467,Introduction to Statistical Machine Learning,S1/2012
10980,COMP6442,Software Construction,S1/2012
10979,COMP6363,Theory of Computation,S1/2012
10978,COMP6340,Networked Information Systems,S1/2012
10977,COMP6320,Artificial Intelligence,S1/2012
10975,COMP6300,Introduction to Computer Systems,S1/2012
10974,COMP4801,Software Engineering Honours Results,S1/2012
10973,COMP4800,Industrial Experience,S1/2012
10972,COMP4670,Introduction to Statistical Machine Learning,S1/2012
10971,COMP4540,Software Engineering Research Project,S1/2012
10970,COMP4500,Software Engineering Practice,S1/2012
10969,COMP4130,Managing Software Quality and Process,S1/2012
10968,COMP4006,Computer Science Honours,S1/2012
10967,COMP4005P,"Computing Science Honours,Parttime",S1/2012
10966,COMP4005F,Computer Science Honours,S1/2012
10965,COMP3760,Project Work in Information Systems,S1/2012
10964,COMP3750,Project Work in Comp Systems,S1/2012
10963,COMP3740,Project Work in Computing,S1/2012
10962,COMP3710,Topics in Computer Science,S1/2012
10961,COMP3700,Topics in Software Engineering,S1/2012
10960,COMP3630,Theory of Computation,S1/2012
10959,COMP3620,Artificial Intelligence,S1/2012
10958,COMP3500,Software Engineering Project (Part A),S1/2012
10957,COMP3420,Advanced Databases and Data Mining,S1/2012
10956,COMP3130,Computer Science Group Project,S1/2012
10955,COMP3120,Managing Software Development,S1/2012
10953,COMP3100,Software Engineering Group Project,S1/2012
10952,COMP2620,Logic,S1/2012
10951,COMP2500,Software Construction for Software Engineers,S1/2012
10950,COMP2410,Networked Information Systems,S1/2012
10949,COMP2300,Introduction to Computer Systems,S1/2012
10948,COMP2100,Software Construction,S1/2012
10947,COMP1710,Web Development and Design,S1/2012
10946,COMP1130,Introduction to Advanced Computing I,S1/2012
10945,COMP1100,Introduction to Programming and Algorithms,S1/2012
10944,COMPMISC,Miscellaneous Computing students,S2/2011
10940,LAWS3001,Unravelling Complexity,S2/2011
10937,COMP3740,Project Work in Computing,S1/2011
10902,PHIL2080,Logic,S1/2011
10900,VCPG6001,Unravelling Complexity,S2/2011
10899,VCUG3001,Unravelling Complexity,S2/2011
10898,COMP6719,Computing for Engineering Simulation,S2/2011
10897,COMP6311,Software Analysis and Design,S2/2011
10876,DART8004,Formal Structures for New Media 1,S1/2011
10875,ASGS1017,"New Media, the Web &amp; its tools",S1/2011
10849,COMP6730,Introductory Programming for Scientists,S2/2011
10848,COMP6710,Introduction to Software Systems,S2/2011
10847,COMP2610,Information Theory,S2/2011
10846,COMP2620,Logic,S1/2011
10844,COMP8200,Master of Computing Honours Results,S2/2010
10823,COMP6730,Introductory Programming for Scientists,S2/2010
10822,COMP6719,Computing for Engineering Simulation,S2/2010
10821,COMP6710,Introduction to Software Systems,S2/2010
10820,COMP4650,Document Analysis,S2/2011
10819,COMP3820,Software Engineering Internship,S2/2011
10818,COMP2130,Software Analysis &amp; Design,S2/2011
10817,COMP4300,Parallel Systems,S1/2011
10816,COMP6430,Parallel Systems,S1/2011
10815,COMP6365,System Architectural Understanding &amp; the Human Brain,S1/2015
10814,COMP8650,Advanced Topics in Statistical Machine Learning,S2/2011
10813,COMP8320,Multicore Computing,S2/2011
10812,COMP6461,Computer Graphics,S2/2011
10811,COMP6433,Real-time Embedded Systems,S2/2011
10810,COMP6361,Principles of Programming Languages,S2/2011
10809,COMP4610,Computer Graphics,S2/2011
10808,COMP4330,Real-Time and Embedded Systems,S2/2011
10807,COMP3610,Principles of Programming Languages,S2/2011
10806,COMP3650,System Architectural Understanding &amp; the Human Brain,S1/2015
10804,COMP7410,Data Mining &amp; Matching,Spr/2011
10803,INFT4005P,"Information Technology Honours,Parttime",S2/2011
10802,INFT4005F,"Information Technology Honours,Fulltime",S2/2011
10801,ENGN2219,Computing for Engineering Simulation,S2/2011
10800,COMPSEPC,Software Engineering Project Clients,S2/2011
10799,COMP9000P,(Unknown),S2/2011
10798,COMP9000F,(Unknown),S2/2011
10797,COMP8900P,(Unknown),S2/2011
10796,COMP8900F,(Unknown),S2/2011
10795,COMP8800,Computing Research Project,S2/2011
10794,COMP8790,Software Engineering Project,S2/2011
10793,COMP8780,Information &amp; Human Centred Computer Project,S2/2011
10792,COMP8770,eResearch Project,S2/2011
10791,COMP8760,Computer Science Project,S2/2011
10790,COMP8750,Computer Systems Project,S2/2011
10789,COMP8740,Artificial Intelligence Project,S2/2011
10788,COMP8730,Project Work in Software Engineering II,S2/2011
10787,COMP8710,Advanced Topics in Software Engineering C,S2/2011
10786,COMP8620,Advanced Topics in Artificial Intelligence,S2/2011
10785,COMP8420,Bio-inspired Computing,S1/2011
10784,COMP8173,Software Engineering Processes,S2/2011
10783,COMP8110,Managing Software Projects in a System Context,S2/2011
10782,COMP7420,Electronic Data Management,Sum/2011
10781,COMP7310,Green Information Technology Strategies,S1/2011
10780,COMP6720,Art Interaction and New Media,S2/2011
10779,COMP6466,Algorithms,S2/2011
10778,COMP6463,Overview of Logic &amp; Computation,S2/2011
10776,COMP6341,Information Technology in Electronic Commerce,S2/2011
10774,COMP6310,Concurrent &amp; Distributed Systems,S2/2011
10773,COMP6240,Relational Databases,S2/2011
10772,COMP4801,Software Engineering Honours Results,S2/2011
10771,COMP4800,Industrial Experience,S2/2011
10769,COMP4710,Topics in Software Engineering III ,S2/2011
10767,COMP4630,Overview of Logic &amp; Computation,S2/2011
10766,COMP4620,Advanced Topics in Artifical Intelligence,S2/2011
10765,COMP4600,Advanced Algorithms,S2/2011
10764,COMP4540,Software Engineering Research Project,S2/2011
10763,COMP4500,Software Engineering Practice,S2/2011
10762,COMP4006,Computer Science Honours,S2/2011
10761,COMP4005P,Computer Science IV Honours,S2/2011
10760,COMP4005F,Computer Science IV Honours,S2/2011
10758,COMP3760,Project Work in Information Systems,S2/2011
10757,COMP3750,Project Work in Comp Systems,S2/2011
10756,COMP3710,Topics in Computer Science,S2/2011
10755,COMP3700,Topics in Software Engineering,S2/2011
10754,COMP3600,Algorithms,S2/2011
10753,COMP3500,Software Engineering Project (Part B),S2/2011
10752,COMP3410,Information Technology in Electronic Commerce,S2/2011
10750,COMP3120,Managing Software Development,S1/2011
10749,COMP3100,Software Engineering Group Project,S2/2011
10748,COMP3006,Computer Science Research Project,S2/2011
10747,COMP1720,Art and Interaction in New Media,S2/2011
10746,COMP2600,Formal Methods in Software Engineering,S2/2011
10744,COMP2400,Relational Databases  ,S2/2011
10743,COMP2310,Concurrent and Distributed Systems,S2/2011
10741,COMP1730,Introductory Programming for Scientists,S2/2011
10740,COMP1510,Introduction to Software Engineering ,S2/2011
10739,COMP1140, Introduction to Advanced Computing II,S2/2011
10738,COMP1110,Introduction to Software Systems,S2/2011
10737,COMP8440,Free &amp; Open Source Software Development,Aut/2011
10736,COMP8180,Systems and Software Safety,Aut/2011
10735,INFT4005P,"Information Technology Honours,Parttime",S1/2011
10734,INFT4005F,"Information Technology Honours,Fulltime",S1/2011
10732,COMP9000P,(Unknown),S1/2011
10731,COMP9000F,(Unknown),S1/2011
10730,COMP8800,Computing Research Project,S1/2011
10729,COMP8790,Software Engineering Project,S1/2011
10728,COMP8780,Information &amp;Human Centered Computing Project,S1/2011
10727,COMP8770,eResearch Project,S1/2011
10725,COMP8750,Computer &amp; Programming Language Systems Project,S1/2011
10724,COMP8740,Artificial Intelligence Project,S1/2011
10723,COMP8730,Project Work in Software Engineering II,S1/2011
10722,COMP8710,Advanced Topics in Software Engineering C,S1/2011
10721,COMP8400,Algorithms for Data Mining,S1/2011
10720,COMP8200,Master of Computing Honours Results,S1/2011
10719,COMP8100,Requirements Elicitation and Analysis Techniques,S1/2011
10718,COMP6700,Introductory Programming In Java,S1/2011
10717,COMP6467,Introduction to Statistical Machine Learning,S1/2011
10715,COMP6442,Software Construction,S1/2011
10714,COMP6363,Theory of Computation,S1/2011
10713,COMP6340,Networked Information Systems,S1/2011
10711,COMP6320,Artificial Intelligence,S1/2011
10710,COMP6311,Software Analysis and Design,S1/2011
10709,COMP6300,Introduction to Computer Systems,S1/2011
10708,COMP4801,Software Engineering Honours Results,S1/2011
10707,COMP4800,Industrial Experience,S1/2011
10705,COMP4710,Topics in Software Engineering III,S1/2011
10702,COMP4670,Introduction to Statistical Machine Learning,S1/2011
10701,COMP4540,Software Engineering Research Project,S1/2011
10700,COMP4500,Software Engineering Practice,S1/2011
10699,COMP4130,Managing Software Quality and Process,S1/2011
10698,COMP4006,Computer Science Honours,S1/2011
10697,COMP4005P,"Computing Science Honours,Parttime",S1/2011
10696,COMP4005F,Computer Science Honours,S1/2011
10695,COMP3760,Project Work in Information Systems,S1/2011
10694,COMP3750,Project Work in Comp Systems,S1/2011
10693,COMP3710,Topics in Computer Science,S1/2011
10692,COMP3700,Topics in Software Engineering,S1/2011
10691,COMP3630,Theory of Computation,S1/2011
10690,COMP3620,Artificial Intelligence,S1/2011
10689,COMP3500,Software Engineering Project (Part A),S1/2011
10688,COMP3420,Advanced Databases and Data Mining,S1/2011
10685,COMP3130,Computer Science Group Project,S1/2011
10684,COMP3110,Software Analysis and Design,S1/2011
10683,COMP3100,Software Engineering Group Project,S1/2011
10681,COMP2500,Software Construction for Software Engineers,S1/2011
10680,COMP2410,Networked Information Systems,S1/2011
10679,COMP2300,Introduction to Computer Systems,S1/2011
10678,COMP2100,Software Construction,S1/2011
10677,COMP1710,Web Development and Design,S1/2011
10676,COMP1130,Introduction to Advanced Computing I,S1/2011
10675,COMP1100,Introduction to Programming and Algorithms,S1/2011
10624,COMP4006,Computer Science Honours,S2/2010
10623,COMP7420,Electronic Data Management,S2/2010
10622,COMP7410,Data Mining &amp; Matching,Spr/2010
10620,COMP9000P,(Unknown),S2/2010
10619,COMP9000P,(Unknown),S1/2010
10618,COMP9000F,(Unknown),S2/2010
10617,COMP9000F,(Unknown),S1/2010
10616,COMP6466,Algorithms,S2/2010
10614,COMP4730,Project Work in Software Engineering II,S1/2010
10598,COMP6464,High Performance Scientific Computation,S1/2010
10583,COMP8200,Master of Computing Honours Results,S1/2010
10568,COMP8190,Model-Driven Software Development,Spr/2010
10567,COMP8173,Software Engineering Processes,S2/2010
10566,COMP6330,Operating Systems Implementation,S2/2010
10565,COMP6330,Operating Systems Implementation,S2/2009
10564,COMP8900P,(Unknown),S2/2010
10563,COMP8900F,(Unknown),S2/2010
10562,COMP8800,Computing Research Project,S2/2010
10561,COMP8790,Software Engineering Project,S2/2010
10560,COMP8780,Information &amp; Human Centred Computer Project,S2/2010
10559,COMP8770,eResearch Project,S2/2010
10558,COMP8760,Computer Science Project,S2/2010
10557,COMP8750,Computer Systems Project,S2/2010
10556,COMP8740,Artificial Intelligence Project,S2/2010
10555,COMP8710,Advanced Topics in Software Engineering C,S2/2010
10554,COMP8620,Advanced Topics in Artificial Intelligence,S2/2010
10553,COMP8440,Free &amp; Open Source Software Development,Aut/2010
10552,COMP8420,Bio-inspired Computing,S2/2010
10551,COMP8180,Systems and Software Safety,Aut/2010
10550,COMP8110,Managing Software Projects in a System Context,S2/2010
10549,COMP6720,Automating tools for the New Media,S2/2010
10548,COMP6341,Information Technology in Electronic Commerce,S2/2010
10547,COMP6310,Concurrent &amp; Distributed Systems,S2/2010
10546,COMP6240,Relational Databases,S2/2010
10545,COMP4801,Software Engineering Honours Results,S2/2010
10544,COMP4800,Industrial Experience,S2/2010
10543,COMP4730,Project Work in Software Engineering II,S2/2010
10542,COMP4710,Topics in Software Engineering III ,S2/2010
10541,COMP4700,Topics in Software Engineering II ,S2/2010
10540,COMP4620,Advanced Topics in Artifical Intelligence,S2/2010
10539,COMP4540,Software Engineering Research Project,S2/2010
10538,INFT4005P,"Information Technology Honours,Parttime",S2/2010
10537,COMP4005P,Computer Science IV Honours,S2/2010
10536,INFT4005F,"Information Technology Honours,Fulltime",S2/2010
10535,COMP4005F,Computer Science IV Honours,S2/2010
10534,COMP3900,HCI Design and Evaluation,S2/2010
10533,COMP3760,Project Work in Information Systems,S2/2010
10532,COMP3750,Project Work in Comp Systems,S2/2010
10531,COMP3710,Topics in Computer Science,S2/2010
10530,COMP3700,Topics in Software Engineering,S2/2010
10529,COMP3600,Algorithms,S2/2010
10528,COMP3410,Information Technology in Electronic Commerce,S2/2010
10527,COMP3300,Operating Systems Implementation,S2/2010
10526,COMP3120,Managing Software Development,S2/2010
10525,COMP4500,Software Engineering Practice,S2/2010
10524,COMP3500,Software Engineering Project (Part B),S2/2010
10523,COMP3100,Software Engineering Group Project,S2/2010
10522,COMP3006,Computer Science Research Project,S2/2010
10521,COMP2720,Art and Interaction in New Media,S2/2010
10520,COMP2600,Formal Methods in Software Engineering,S2/2010
10519,COMP2400,Relational Databases  ,S2/2010
10518,COMP2310,Concurrent and Distributed Systems,S2/2010
10517,COMP2510,Software Design for Software Engineers,S2/2010
10516,COMP2110,Software Design,S2/2010
10515,COMP1510,Introduction to Software Engineering ,S2/2010
10514,COMP1140,Data Structures and Algorithms II,S2/2010
10513,COMP1110,Introduction to Software Systems,S2/2010
10504,COMP9000P,(Unknown),Spr/2009
10503,COMP9000F,(Unknown),Spr/2009
10502,COMP9000P,(Unknown),S2/2009
10501,COMP9000F,(Unknown),S2/2009
10500,COMP8900P,(Unknown),S2/2009
10499,COMP8900F,(Unknown),S2/2009
10498,COMP2100,Software Construction,S1/2010
10497,COMP4630,Overview of Logic &amp; Computation,S2/2010
10496,COMP4600,Advanced Algorithms,S2/2010
10137,ENGN2219,Computing for Engineering Simulation,S2/2010
10136,COMP8730,Project Work in Software Engineering II,S2/2010
10135,COMP8730,Project Work in Software Engineering II,S1/2010
10134,COMP7310,Green Information Technology Strategies,S2/2010
10133,COMP6442,Software Construction for eScience,S1/2010
10132,COMP6390,HCI Design and Evaluation,S2/2010
10131,COMP6331,Computer Networks,S1/2010
10130,COMP3320,High Performance Scientific Computation,S1/2010
10129,COMP3310,Computer Networks,S1/2010
10128,COMP1730,Introductory Programming for Scientists,S2/2010
10009,INFT4005P,"Information Technology Honours,Parttime",S1/2010
10008,INFT4005F,"Information Technology Honours,Fulltime",S1/2010
10007,DART8004,Formal Structures for New Media 1,S1/2010
10006,COMPSEPC,Software Engineering Project Clients,S2/2010
10005,COMP8800,Computing Research Project,S1/2010
10004,COMP8790,Software Engineering Project,S1/2010
10003,COMP8780,Information &amp;Human Centered Computing Project,S1/2010
10002,COMP8770,eResearch Project,S1/2010
10001,COMP8760,Computer Science Project,S1/2010
10000,COMP8750,Computer &amp; Programming Language Systems Project,S1/2010
9999,COMP8740,Artificial Intelligence Project,S1/2010
9997,COMP8710,Advanced Topics in Software Engineering C,S1/2010
9994,COMP8400,Algorithms for Data Mining,S1/2010
9992,COMP8100,Requirements Elicitation and Analysis Techniques,S1/2010
9991,COMP6700,Introductory Programming In Java,S1/2010
9990,COMP6467,Introduction to Statistical Machine Learning,S1/2010
9989,COMP6463,Overview of Logic &amp; Computation,S2/2010
9986,COMP6363,Theory of Computation,S1/2010
9985,COMP6340,Networked Information Systems,S1/2010
9984,COMP6320,Artificial Intelligence,S1/2010
9983,COMP6311,Software Analysis and Design,S1/2010
9982,COMP6300,Introduction to Computer Systems,S1/2010
9981,COMP4801,Software Engineering Honours Results,S1/2010
9980,COMP4800,Industrial Experience,S1/2010
9977,COMP4710,Topics in Software Engineering III,S1/2010
9976,COMP4700,Topics in Software Engineering II ,S1/2010
9974,COMP4670,Introduction to Statistical Machine Learning,S1/2010
9972,COMP4540,Software Engineering Research Project,S1/2010
9971,COMP4500,Software Engineering Practice,S1/2010
9969,COMP4130,Managing Software Quality and Process,S1/2010
9968,COMP4006,Computer Science Honours,S1/2010
9967,COMP4005P,"Computing Science Honours,Parttime",S1/2010
9966,COMP4005F,Computer Science Honours,S1/2010
9965,COMP3760,Project Work in Information Systems,S1/2010
9964,COMP3750,Project Work in Comp Systems,S1/2010
9963,COMP3710,Topics in Computer Science,S1/2010
9962,COMP3700,Topics in Software Engineering,S1/2010
9960,COMP3630,Theory of Computation,S1/2010
9959,COMP3620,Artificial Intelligence,S1/2010
9958,COMP3500,Software Engineering Project (Part A),S1/2010
9957,COMP3420,Advanced Databases and Data Mining,S1/2010
9956,COMP3130,Computer Science Group Project,S1/2010
9955,COMP3110,Software Analysis and Design,S1/2010
9954,COMP3100,Software Engineering Group Project,S1/2010
9953,COMP2750,Java Programming for New Media,S1/2010
9952,COMP2500,Software Construction for Software Engineers,S1/2010
9951,COMP2410,Networked Information Systems,S1/2010
9950,COMP2300,Introduction to Computer Systems,S1/2010
9948,COMP1710,Tools for New Media and the Web,S1/2010
9947,COMP1130,Data Structures and Algorithms I,S1/2010
9946,COMP1100,Introduction to Programming and Algorithms,S1/2010
9945,ASGS1017,"New Media, the Web &amp; its tools",S1/2010
9940,ENGN8102,Project Management,S2/2009
9939,COMPSEPC,Sofware Engineering Project Clients,S2/2009
9937,COMPSEPC,Sofware Engineering Project Clients,S1/2009
9936,COMP7310,Green ICT Strategies,S2/2009
9935,COMP3130,Computer Science Group Project,S2/2009
9934,COMP4006,Computer Science Honours,S2/2009
9933,ASGS1017,"New Media, the Web &amp; its tools",S1/2009
9932,DART8004,Formal Structures for New Media 1,S1/2009
9931,COMP8200,Master of Computing Honours Results,S2/2009
9930,COMP8200,Master of Computing Honours Results,S1/2009
9929,COMP8800,Computing Research Project,S1/2009
9928,COMP4006,Computer Science Honours,S1/2009
9927,INFT4005P,"Information Technology Honours,Parttime",S2/2009
9926,INFT4005P,"Information Technology Honours,Parttime",S1/2009
9925,INFT4005F,"Information Technology Honours,Fulltime",S2/2009
9924,INFT4005F,"Information Technology Honours,Fulltime",S1/2009
9923,COMP8420,Bio-inspired Computing,S2/2009
9922,COMP8320,Multicore Computing,S2/2009
9921,COMP6310,Concurrent &amp; Distributed Systems,S2/2009
9920,COMP8800,Computing Research Project,S2/2009
9919,COMP8790,Software Engineering Project,S2/2009
9918,COMP8780,Information &amp; Human Centred Computer Project,S2/2009
9917,COMP8770,eResearch Project,S2/2009
9916,COMP8760,Computer Science Project,S2/2009
9915,COMP8750,Computer Systems Project,S2/2009
9914,COMP8740,Artificial Intelligence Project,S2/2009
9913,COMP8730,Project Work in Software Engineering II,S2/2009
9912,COMP8720,Project Work in Software Engineering I,S2/2009
9911,COMP8710,Advanced Topics in Software Engineering C,S2/2009
9910,COMP8700,Topics in Software Engineering 1,S2/2009
9909,COMP8620,Advanced Topics in Artificial Intelligence,S2/2009
9908,COMP8602,Research Project,S2/2009
9907,COMP8601,Research Project,S2/2009
9906,COMP8150,Advanced Software Architecture,Spr/2009
9905,COMP8110,Managing Software Projects in a System Context,S2/2009
9904,COMP6466,Algorithms,S2/2009
9902,COMP6433,Real-time Embedded Systems,S2/2009
9901,COMP6361,Principles of Programming Languages,S2/2009
9900,COMP6341,Information Technology in Electronic Commerce,S2/2009
9899,COMP6240,Relational Databases,S2/2009
9898,COMP4801,Software Engineering Honours Results,S2/2009
9897,COMP4800,Industrial Experience,S2/2009
9896,COMP4730,Project Work in Software Engineering II,S2/2009
9895,COMP4720,Project Work in Software Engineering I,S2/2009
9894,COMP4710,Topics in Software Engineering III ,S2/2009
9893,COMP4700,Topics in Software Engineering II ,S2/2009
9891,COMP4610,Computer Graphics,S2/2009
9890,COMP4540,Software Engineering Research Project,S2/2009
9889,COMP4500,Software Engineering Practice,S2/2009
9888,COMP4330,Real-Time and Embedded Systems,S2/2009
9887,COMP4005P,Computer Science IV Honours,S2/2009
9886,COMP4005F,Computer Science IV Honours,S2/2009
9885,COMP3760,Project Work in Information Systems,S2/2009
9884,COMP3750,Project Work in Comp Systems,S2/2009
9883,COMP3710,Topics in Computer Science,S2/2009
9882,COMP3700,Topics in Software Engineering,S2/2009
9880,COMP3610,Principles of Programming Languages,S2/2009
9879,COMP3600,Algorithms,S2/2009
9878,COMP3500,Software Engineering Project (Part B),S2/2009
9877,COMP3410,Information Technology in Electronic Commerce,S2/2009
9876,COMP3120,Managing Software Development,S2/2009
9875,COMP3100,Software Engineering Group Project,S2/2009
9874,COMP3006,Computer Science Research Project,S2/2009
9873,COMP2720,Automating Tools for New Media,S2/2009
9872,COMP2600,Formal Methods in Software Engineering,S2/2009
9871,COMP2510,Software Design for Software Engineers,S2/2009
9870,COMP2400,Relational Databases  ,S2/2009
9869,COMP2310,Concurrent and Distributed Systems,S2/2009
9868,COMP2110,Software Design,S2/2009
9867,COMP1510,Introduction to Software Engineering ,S2/2009
9866,COMP1140,Data Structures and Algorithms II,S2/2009
9865,COMP1110,Introduction to Software Systems,S2/2009
9864,COMP2750,Java Programming for New Media,S1/2009
9863,COMP8790,Software Engineering Project,S1/2009
9862,COMP8780,Information &amp;Human Centered Computing Project,S1/2009
9861,COMP8770,eResearch Project,S1/2009
9860,COMP8760,Computer Science Project,S1/2009
9859,COMP8750,Computer &amp; Programming Language Systems Project,S1/2009
9858,COMP8740,Artificial Intelligence Project,S1/2009
9856,COMP8720,Project Work in Software Engineering I,S1/2009
9855,COMP8710,Advanced Topics in Software Engineering C,S1/2009
9854,COMP8700,Topics in Software Engineering 1,S1/2009
9853,COMP8440,Free &amp; Open Source Software Development,Aut/2009
9852,COMP8400,Algorithms for Data Mining,S1/2009
9851,COMP8180,Systems and Software Safety,Aut/2009
9850,COMP8100,Requirements Elicitation and Analysis Techniques,S1/2009
9849,COMP6700,Introductory Programming In Java,S1/2009
9848,COMP6467,Introduction to Statistical Machine Learning,S1/2009
9847,COMP6463,Overview of Logic &amp; Computation,S1/2009
9846,COMP6461,Computer Graphics,S2/2009
9845,COMP6442,Software Construction for eScience,Aut/2009
9843,COMP6430,Parallel Systems,S1/2009
9842,COMP6363,Theory of Computation,S1/2009
9841,COMP6340,Networked Information Systems,S1/2009
9840,COMP6320,Artificial Intelligence,S1/2009
9839,COMP6311,Software Analysis and Design,S1/2009
9838,COMP6300,Introduction to Computer Systems,S1/2009
9837,COMP4801,Software Engineering Honours Results,S1/2009
9836,COMP4800,Industrial Experience,S1/2009
9835,COMP4730,Project Work in Software Engineering II,S1/2009
9834,COMP4720,Project Work in Software Engineering I,S1/2009
9833,COMP4710,Topics in Software Engineering III,S1/2009
9832,COMP4700,Topics in Software Engineering II ,S1/2009
9831,COMP4670,Introduction to Statistical Machine Learning,S1/2009
9830,COMP4630,Overview of Logic &amp; Computation,S1/2009
9829,COMP4540,Software Engineering Research Project,S1/2009
9828,COMP4500,Software Engineering Practice,S1/2009
9827,COMP4300,Parallel Systems,S1/2009
9826,COMP4130,Managing Software Quality and Process,S1/2009
9824,COMP4005P,"Computing Science Honours,Parttime",S1/2009
9823,COMP4005F,Computer Science Honours,S1/2009
9822,COMP3760,Project Work in Information Systems,S1/2009
9821,COMP3750,Project Work in Comp Systems,S1/2009
9820,COMP3710,Topics in Computer Science,S1/2009
9819,COMP3700,Topics in Software Engineering,S1/2009
9818,COMP3630,Theory of Computation,S1/2009
9817,COMP3620,Artificial Intelligence,S1/2009
9816,COMP3500,Software Engineering Project (Part A),S1/2009
9815,COMP3420,Advanced Databases and Data Mining,S1/2009
9814,COMP3130,Computer Science Group Project,S1/2009
9813,COMP3110,Software Analysis and Design,S1/2009
9812,COMP2500,Software Construction for Software Engineers,S1/2009
9811,COMP3100,Software Engineering Group Project,S1/2009
9810,COMP2410,Networked Information Systems,S1/2009
9809,COMP2300,Introduction to Computer Systems,S1/2009
9808,COMP2100,Software Construction,S1/2009
9807,COMP1710,Tools for New Media and the Web,S1/2009
9806,COMP1130,Data Structures and Algorithms I,S1/2009
9805,COMP1100,Introduction to Programming and Algorithms,S1/2009
9804,COMP6365,System Architectural Understanding &amp; the Human Brain,S1/2009
9803,COMP3650,System Architectural Understanding &amp; the Human Brain,S1/2009
9766,COMP8630,Beyond Clasical Logic,S1/2009
9639,COMP6464,High Performance Scientific Computation,S1/2008
"""
    data = actual
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
