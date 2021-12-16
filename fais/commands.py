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


import os
import re
import sys
import click

import numpy as np
import pandas as pd

from bs4 import BeautifulSoup
from time import gmtime, strftime
from plotnine import ggplot, aes, geom_bar

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.expected_conditions import presence_of_element_located

import fais.data as data
import fais.utils as utils

from fais.utils import pass_config


def sort_by_course_id(e):
    """For use in courses command to sort by strings beginning with numerics"""
    return int(re.sub(r'^(\d*).*', r'\1', e))


@click.command()
@pass_config
def courses(config):
    """All courses and unit codes, useful for obtaining a unit code."""

    utils.login_fais()
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

    utils.login_fais()
    browser = config.browser

    url = f"https://cs.anu.edu.au/fais/staff/Enrolments.php?UnitID={course}"
    browser.get(url)

    if "Sorry - no such course found in database" in browser.page_source:
        utils.info_error(f"no such course `{course}'")
        sys.exit(1)

    soup = BeautifulSoup(browser.page_source, features="lxml")
    table = soup.find_all("table", class_="ClassList")[0]

    df = utils.html2table(table)
    df = df.rename(columns={"Username": "UID", "Name (s)": "Name"})
    
    if config.human:
        title = soup.find_all("h2")[0].get_text()
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

    else:

        utils.login_fais()
        browser = config.browser

        url = f"https://cs.anu.edu.au/fais/staff/FinalMarks.php?UnitID={course}"
        browser.get(url)

        soup = BeautifulSoup(browser.page_source, features="lxml")
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

    utils.login_fais()
    browser = config.browser

    url = f"https://cs.anu.edu.au/fais/staff/FinalMarks.php?Functions={course}"
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

    utils.login_fais()
    browser = config.browser

    url = f"https://cs.anu.edu.au/fais/staff/FinalMarks.php?UnitID={course}"
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
        name = "Harriet Potter"
        title = f"Details for student: {uid} - Harriet Potter"
        sex = "F"
        degree = "MADAN"

        # Add unitid for each course as required for FAIS+

        course = data.courses()
        df = pd.merge(df, course, on=['Course', 'Sem/Year'])
        # Why not add Description to the merge so the following not required?
        df.rename(columns={'Description_x': 'Description'}, inplace=True)
        del df['Description_y']
    else:
        utils.login_fais()
        browser = config.browser

        # Search for given student's UID.

        elem = browser.find_element_by_name("in")
        select = Select(elem)
        select.select_by_value("anystudent")

        elem = browser.find_element_by_name("search")
        elem.send_keys(uid)
        elem.send_keys(Keys.RETURN)

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
        # obtain obtain unitid throug scrpaing to add it in - i.e.,
        # COURSES might need to be loaded by default on startup?

        df['Unitid'] = 12886

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
        df["Sex"] = sex

        df = df.iloc[:, [8, 9, 10, 7, 0, 1, 2, 3, 5, 6]]
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
        utils.login_fais()
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


########################################################################
# WATTLE MARKS

@click.command()
@click.argument("unit")
@click.argument("assessment")
@pass_config
def wmarks(config, unit, assessment):
    """Wattle assessement for import into FAIS.

The aim is to extract the uid,mark from Wattle into a CSV file.
A fais command will then load that up into an assessment variable.

If no assessment is supplied, print the list of all assessments available.

Example:

    $ fais wmarks 34101 "Quiz 1"
"""

    utils.login_wattle()
    browser = config.browser
    wait = config.wait

    # EXTRACT MARKS
    #
    # Exports to COMP3430_Sem2_2021 Grades-20211129_2115-comma-separated.csv
    # Exports to COMP3430_Sem2_2021 Grades-20211129_2121-comma-separated.csv

    url = "https://wattlecourses.anu.edu.au/grade/export/txt/index.php?id="
    browser.get(url + unit)
    now = strftime("%Y%m%d_%H%M", gmtime())
    elem = browser.find_element_by_name("submitbutton")
    elem.click()

    # Be sure to wait a little by going home and check when we get there.

    browser.get("https://wattlecourses.anu.edu.au/my/")
    wait.until(presence_of_element_located((By.ID, "page-my-index")))

    # Hopefully the file is now saved and present. For Chrome headless
    # the file is saved into the current working directory but in
    # Downloads when not in headless mode. TOD Need to find the optins
    # to specify where to save the file by default without asking.

    COURSE = "COMP3430_Sem2_2021"  # TODO FIX THIS
    fname = f"{COURSE} Grades-{now}-comma_separated.csv"
    home = os.path.expanduser(f"~")
    downloads = f"{home}/Downloads/{fname}"
    if os.path.exists(fname):
        fpath = os.path.expanduser(fname)
    elif os.path.exists(downloads):
        fpath = os.path.expanduser(f"~/Downloads/{fname}")
    else:
        utils.info_error("could not find saved CSV file")
        sys.exit(1)

    df = pd.read_csv(fpath)
    os.remove(fpath)

    ndf = list(df)
    cols = [x for x in ndf if assessment in x]
    cols.insert(0, 'Uni ID')
    cols.insert(2, 'First name')
    cols.insert(3, 'Surname')
    click.echo(df[cols].to_csv(index=False).strip())

    utils.logout()
