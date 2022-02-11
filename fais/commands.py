#!/usr/bin/python3
#
# fais - Command Line Access to FAIS
#
# A command line tool for managing fais activity.
#
# Copyright Australian National University All rights reserved.
#
# GNU GPLv3 License
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version. See the file LICENSE.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# This file is part of fais.
#
# Author: Graham.Williams@anu.edu.au


from curses import echo
import re
import sys
import click

import numpy as np
import pandas as pd

from bs4 import BeautifulSoup
from plotnine import ggplot, aes, geom_bar

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

import fais.data as data
import fais.utils as utils

from fais.utils import pass_config, URL

# Do not limit dataframe output.

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


def sort_by_course_id(e):
    """For use in courses command to sort by strings beginning with numerics"""
    return int(re.sub(r'^(\d*).*', r'\1', e))


@click.command()
@pass_config
def courses(config):
    """All courses and unit codes, useful for obtaining a unit code."""

    utils.login()
    browser = config.browser

    elem = browser.find_element_by_name("in")
    select = Select(elem)
    select.select_by_value("allcourse")

    elem = browser.find_element_by_name("search")
    elem.send_keys(Keys.RETURN)

    # List all course.

    soup = BeautifulSoup(browser.page_source, features="lxml")
    table = soup.find_all("table")[2]

    # String extract the data we want. Some hrefs and some text.

    tr = table.find_all("tr")
    units = [str(k) for k in tr if 'Course.php?UnitID=' in str(k)]
    # Remove the prefix string.
    line_begin = r'^<tr><td><a href="Course.php\?UnitID='
    units = [re.sub(line_begin, r'', k) for k in units]
    # remove the '">' just before the course name
    units = [k.replace('">', ',', 1) for k in units]
    # Extract just the title from the rest.
    id_name_title = r'^(\d{4,5},\w*)</a></td><td>(<a.*?>)?([^<]*?)(</a>)?</td>.*?$'
    units = [re.sub(id_name_title, r'\1,\2\3', k) for k in units]
    # Remove any remaining markup/links.
    units = [re.sub(r"<.*?>", r"", k) for k in units]
    units = [re.sub(r"SoCS", r"", k) for k in units]

    units.sort(key=sort_by_course_id, reverse=True)

    for u in units:
        click.echo(u.strip())

    utils.logout()


@click.command()
@click.argument("course")
@pass_config
def enrolments(config, course):
    """Students enrolled in a course."""

    utils.login()
    browser = config.browser

    url = URL + f"Enrolments.php?UnitID={course}"
    browser.get(url)
    soup = BeautifulSoup(browser.page_source, features="lxml")

    if "Sorry - no such course found in database" in browser.page_source:
        utils.info_error(f"no such course `{course}'")
        sys.exit(1)

    title = soup.find_all("h2")[0].get_text()

    if "Sorry - This course has no students" in browser.page_source:
        if config.human:
            click.echo(f"{title}\n")
        else:
            print("Username,Name (s),Status,Mark,Grade,Degree,Sp")
        sys.exit(0)

    table = soup.find_all("table", class_="ClassList")[0]
    df = utils.html2table(table)
    df = df.rename(columns={"Username": "UID", "Name (s)": "Name"})

    if config.human:
        click.echo(f"{title}\n")
        click.echo(df)
    else:
        utils.html2csv(table)

    utils.logout()


########################################################################
# FINAL

@click.command()
@click.argument("course")
@pass_config
def final(config, course):
    """Students final grades for a course."""

    if config.fake:
        df = data.final(course)
        click.echo(df.to_csv(index=False).strip())
        sys.exit(0)

    utils.login()
    browser = config.browser

    url = URL + f"FinalMarks.php?UnitID={course}"
    browser.get(url)
    soup = BeautifulSoup(browser.page_source, features="lxml")

    if "Sorry - no students found for this course" in browser.page_source:
        if config.human:
            utils.info_error(f"no students found in course `{course}'")
        else:
            print("Student,Fore/Last Names,Degree," +
                  "FAIS Mark,FAIS Grade,Seq.,Sp")
        sys.exit(0)

    table = soup.find_all("table")[3]

    if config.human:
        title = soup.find_all("h2")[0].get_text()
        click.echo(f"{title}\n")
        click.echo(utils.html2table(table))
    else:
        utils.html2csv(table)

    utils.logout()


@click.command()
@click.argument("course")
@click.option("--mark", is_flag=True, default=False)
@click.option("--grade", is_flag=True, default=False)
@pass_config
def function(config, course, mark, grade):
    """Functions for --marks (int) and --grades (str)."""

    utils.login()
    browser = config.browser

    url = URL + f"FinalMarks.php?Functions={course}"
    browser.get(url)

    soup = BeautifulSoup(browser.page_source, features="lxml")
    textareas = soup.find_all("textarea")

    both = not mark and not grade

    if mark or both:
        title = soup.find_all("h2")[0].get_text()
        title = title.replace("Mark/Grade", "Mark")
        nstar = len(title) + 4
        click.echo(f"/{'*' * nstar}/")
        click.echo(f"/* {title} */")
        click.echo(f"/{'*' * nstar}/\n")
        click.echo(textareas[0].string)

    if grade or both:
        title = soup.find_all("h2")[0].get_text()
        title = title.replace("Mark/Grade", "Grade")
        nstar = len(title) + 4
        click.echo(f"/{'*' * nstar}/")
        click.echo(f"/* {title} */")
        click.echo(f"/{'*' * nstar}/\n")
        click.echo(textareas[1].string)

    utils.logout()


@click.command()
@click.argument("course")
@pass_config
def stats(config, course):
    """Stats for final grades for a course."""

    utils.login()
    browser = config.browser

    url = URL + f"FinalMarks.php?UnitID={course}"
    browser.get(url)

    soup = BeautifulSoup(browser.page_source, features="lxml")

    title = soup.find_all("h2")[0].get_text()
    click.echo(f"{title}\n")

    table = soup.find_all("table")[3]
    df = utils.html2table(table)

    df["FAIS Mark"][df["FAIS Mark"] == ""] = "0"
    df['FAIS Mark'] = df['FAIS Mark'].astype(int)

    de = df[["FAIS Mark"]].describe().round().astype(int)
    click.echo("Mark Statistics")
    click.echo(de.transpose())

    gr = df['FAIS Grade']
    gr = gr.value_counts().sort_index().to_frame()
    gr = gr.reindex(["HD", "D", "CR", "P", "PX", "N", "NCN", "WD"])
    gp = gr.divide(gr.sum()).multiply(100).round(0).astype(int)

    click.echo("\nDistribution of Grade Counts")
    click.echo(gr.transpose())

    click.echo("\nDistribution of Grade Percentages")
    click.echo(gp.transpose())

    # Plot the Grades distribution.
    
    grades = pd.Categorical(df["FAIS Grade"],
                            categories=["HD", "D", "CR", "P",
                                        "PX", "N", "NCN", "WD"])
    df = df.assign(grades=grades)
    print(ggplot(df) + aes(x="grades") + geom_bar())

    utils.logout()


########################################################################
# STUDENT

@click.command()
@click.argument("uid", callback=utils.validate_uid)
@click.option("-s", "--session", default="")
@pass_config
def student(config, uid, session):
    """Student details."""

    # For stdin if uid not supplied
    #
    # if sys.stdin.isatty():
    #     try:
    #         for uid in sys.stdin:
    #             ...
    #     except KeyboardInterrupt:
    #         pass
    # else:
    #     for line in sys.stdin.readlines():
    #         ...

    if config.fake:
        df = data.student(uid)
        ds = data.students()
        entry = ds[ds['Student ID'] == uid]
        if not len(entry):
            if config.human:
                utils.info_error(f"no such student `{uid}'")
                sys.exit(1)
            else:
                print("UID,Name,Sex,Unitid,Course,Description," +
                      "Sem/Year,Status,Grade,Final,Comment")
                sys.exit(0)
        name = entry['Fore/Last name(s)'][0]
        title = f"Details for student: {uid} - {name}"
        sex = "F"
        degree = "MADAN"

        # Add unitid for each course as required for FAIS+

        course = data.courses()
        df = pd.merge(df, course, on=['Course', 'Sem/Year'])
        # Why not add Description to the merge so the following not required?
        df.rename(columns={'Description_x': 'Description'}, inplace=True)
        del df['Description_y']
    else:
        utils.login()
        browser = config.browser

        # Search for given student's UID.

        elem = browser.find_element_by_name("in")
        select = Select(elem)
        select.select_by_value("anystudent")

        elem = browser.find_element_by_name("search")
        elem.send_keys(uid)
        elem.send_keys(Keys.RETURN)

        # Check if no students found.

        if "Sorry - no students match" in browser.page_source:
            if config.human:
                utils.info_error(f"no such student `{uid}'")
                sys.exit(1)
            else:
                print("UID,Name,Sex,Unitid,Course,Description," +
                      "Sem/Year,Status,Grade,Final,Comment")
                sys.exit(0)

        # Click the first identified student's UID.
        # TODO list all students returned from the fais match.

        path = "/html/body/table/tbody/tr/td[2]/form/table/tbody/tr[2]/td[1]/a"
        elem = browser.find_elements_by_xpath(path)[0]
        elem.click()

        # List students details.

        soup = BeautifulSoup(browser.page_source, features="lxml")
        tables = soup.find_all("table")
        if len(tables) < 5:
            utils.info_warning(f"student not found '{uid}'")
            sys.exit(0)
        table = tables[4]
        df = pd.read_html(str(table))[0]

        # Extract student information.

        title = soup.find_all("h2")[0].get_text()
        name = title.split(" - ")[1]
        sex = Select(browser.find_element_by_name("Sex"))
        sex = sex.first_selected_option.get_attribute("value")
        path = "/html/body/table/tbody/tr/td[2]/form/p[1]/b[2]"
        degree = browser.find_elements_by_xpath(path)[0]
        degree = degree.text

        # 20211217 gjw Fake added unitid. TODO Investigate if can
        # obtain obtain unitid through scrpaing to add it in - i.e.,
        # COURSES might need to be loaded by default on startup?
        #
        # 20220114 Utilise data.courses. If in there, update Unitid,
        # otherwise just use 00000.

        df['Unitid'] = 0
        courses = data.courses()
        for i, r in df.iterrows():
            unit = courses[(courses["Course"] == r["Course"]) &
                           (courses["Sem/Year"] == r["Sem/Year"])]
            if (len(unit)):
                df.at[i, "Unitid"] = unit.iloc[0]["Unitid"]

    # Filter for the session of interest.

    if session != "":
        df = df[df['Sem/Year'].str.contains(session)]

    # Remove unwanted columns.

    del df["Enrol."]
    del df["Sp"]

    # Generate the required output.
    if config.human:
        click.echo(f"{title} - {sex} - {degree}\n")
        click.echo(df.replace(np.nan, ''))
    else:
        df["UID"] = uid
        df["Name"] = name
        df["Degree"] = degree
        df["Sex"] = sex

        df = df.iloc[:, [8, 9, 10, 11, 7, 0, 1, 2, 3, 4, 5, 6]]

        # Add start_date column

        df['start_date'] = df.apply(lambda row: start_date(row), axis=1)

        # Sort by start date and then by Final so in FAIS+ the chart
        # is sorted the way we want it. Arguable whether this should
        # be done here or in Flutter, but okay for now.

        df = df.sort_values(["start_date", "Final"], ascending=(True, False))

        click.echo(df.to_csv(index=False).strip())

    if not config.fake:
        utils.logout()


########################################################################
# STUDENTS

@click.command()
@click.argument("pattern", default="")
@pass_config
def students(config, pattern):
    """All current students.

A pattern can be specified as a filter on the UID and Name.
"""

    if config.fake:
        df = data.students()
    else:
        utils.login()
        browser = config.browser

        elem = browser.find_element_by_name("in")
        select = Select(elem)
        select.select_by_value("curstudent")

        elem = browser.find_element_by_name("search")
        elem.send_keys(Keys.RETURN)

        # List all students.

        soup = BeautifulSoup(browser.page_source, features="lxml")
        table = soup.find_all("table")[2]
        df = pd.read_html(str(table))[0]

    df = df.rename(columns={'Student ID': "UID", "Fore/Last name(s)": 'Name'})
    del df["Initial(s)"]

    # Filter by uid or name

    if pattern != "":
        d1 = df[df['UID'].str.contains(pattern)]
        d2 = df[df['Name'].str.contains(pattern)]
        df = pd.concat([d1, d2])

    # Extract Name into Fore and Last

    fore = [k.split()[:-1] for k in df['Name']]
    df['Fore'] = [" ".join(k) for k in fore]
    df['Last'] = [k.split()[-1] for k in df['Name']]

    del df['Name']

    # Missing data for now:

    df['Sex'] = "NA"

    # Order for output.

    df = df.iloc[:, [0, 2, 3, 4, 1]]

    if config.human:
        click.echo(df)
    else:
        click.echo(df.to_csv(index=False).strip())

    if not config.fake:
        utils.logout()

def start_date(row):
    sem = row["Sem/Year"].split("/")[0]
    year = row["Sem/Year"].split("/")[1]
    if sem == "Sum":
        return year+"-"+"0"
    elif sem == "S1":
        return year+"-"+"1"
    elif sem == "Aut":
        return year+"-"+"2"
    elif sem == "Win":
        return year+"-"+"3"
    elif sem == "S2":
        return year+"-"+"4"
    elif sem == "Spr":
        return year+"-"+"5"
    else:
        return ""


########################################################################
# PROGRAMS

@click.command()
@click.argument("pattern", default="")
@pass_config
def programs(config, pattern):
    """
    All current programs. 
    A pattern can be specified as a filter for the programs name. Can also use grep.
    Using database : 'data/prog_enrolments_admityear-ANU.csv' from FAIS project.
    """

    # list all the programs. No need of -f flag.

    df = data.programs()       

    # Filter by program name.
    # NOTE: Filters are case-sensitive.

    if pattern != "":
        d1 = df[df['program'].str.contains(pattern)]
        d2 = df[df['year'].astype(str).str.contains(pattern)]
        d3 = df[df['admit_year'].astype(str).str.contains(pattern)]
        d4 = df[df['nenrolled'].astype(str).str.contains(pattern)]
        d5 = df[df['program_id'].astype(str).str.contains(pattern)]
        d6 = df[df['program_desc'].astype(str).str.contains(pattern)]

        # Union of the resultants

        df = pd.concat([d1, d2, d3, d4, d5, d6]).drop_duplicates()     
        df.index = range(0, len(df))


    # Check the -h flag for pretty printing (human consumable).

    if config.human:
        click.echo("---------------------------------------------")
        click.echo("Note: \"Programs' Patterns Are Case-Sensitive\"")
        click.echo("---------------------------------------------")
        click.echo(df)
    else:
        click.echo(df.to_csv(index=False).strip())


########################################################################
# PROGRAM

@click.command()
@click.argument("programid")
@pass_config
def program(config, programid):
    """Provide with a program_id as argument and use `fais program <id>`."""

    # list all programs 

    df = data.programs()

    return_df = df[df['program_id'].astype(str).str.contains(programid)]
    return_df.index = range(0, len(return_df))

    if config.human:
        click.echo("-----------------------------------------------------")
        click.echo("Note: \"Listing programs...\"")
        click.echo("-----------------------------------------------------")
        click.echo(return_df)
    else:
        click.echo(return_df.to_csv(index=False).strip())
