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
#
# Some code borrowed from utils in lucy.

import os
import re
import sys
import csv
import yaml
import click
import getpass

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common.exceptions import TimeoutException

import pandas as pd

APP = "fais"


class Config(object):

    def __init__(self):
        self.debug = None
        self.human = None
        self.browser = None
        self.fake = None
        self.wait = None
        self.private = os.path.expanduser("~/.config/fais/private.json")


pass_config = click.make_pass_decorator(Config, ensure=True)


def html2table(table):
    """https://www.thepythoncode.com/article/
convert-html-tables-into-csv-files-in-python"""

    headers = []
    for th in table.find("tr").find_all("th"):
        headers.append(th.text.strip())

    rows = []
    for tr in table.find_all("tr")[1:]:
        cells = []
        # grab all td tags in this table row
        tds = tr.find_all("td")
        if len(tds) == 0:
            # if no td tags, search for th tags
            # can be found especially in wikipedia tables below the table
            ths = tr.find_all("th")
            for th in ths:
                cells.append(th.text.strip())
        else:
            # use regular td tags
            for td in tds:
                cells.append(td.text.strip())
        rows.append(cells)

    results = pd.DataFrame(rows, columns=headers)

    return(results)


@pass_config
def get_username(config):
    if os.environ.get("FAIS_USERNAME"):
        return os.environ.get("FAIS_USERNAME")
    elif os.path.exists(config.private):
        with open(config.private, 'r') as file:
            return yaml.safe_load(file)["username"]
    else:
        try:
            username = input("Username: ")
            assert username != ""
            return username
        except Exception:
            info_error("a username is required to continue")
            sys.exit(1)


@pass_config
def get_password(config):
    if os.environ.get("FAIS_PASSWORD"):
        return os.environ.get("FAIS_PASSWORD")
    elif os.path.exists(config.private):
        with open(config.private, 'r') as file:
            return yaml.safe_load(file)["password"]
    else:
        try:
            password = getpass.getpass()
            assert password != ""
            return password
        except Exception:
            info_error("a password is required to continue")
            sys.exit(1)


def html2csv(table):
    rows = table.find_all("tr")
    writer = csv.writer(sys.stdout)
    for row in rows:
        csv_row = []
        for cell in row.find_all(["td", "th"]):
            csv_row.append(cell.get_text())
        writer.writerow(csv_row)


@pass_config
def login_fais(config):

    # Driver/Session

    options = webdriver.ChromeOptions()

    if not config.debug:
        options.headless = True

    browser = webdriver.Chrome(options=options)
    config.browser = browser

    # Login

    browser.get("https://cs.anu.edu.au/fais/staff/StaffDetails.php")
    assert "FAIS Login" in browser.title

    elem = browser.find_element_by_name("Username")
    elem.clear()
    elem.send_keys(get_username())

    elem = browser.find_element_by_name("Password")
    elem.clear()
    elem.send_keys(get_password())

    elem.send_keys(Keys.RETURN)

    assert "FAIS Details" in browser.title, "fais: failed to login"

    return(browser)


@pass_config
def login_wattle(config):

    # Driver/Session

    options = webdriver.ChromeOptions()
    if not config.debug:
        options.headless = True
    browser = webdriver.Chrome(options=options)
    config.browser = browser
    wait = WebDriverWait(browser, 10)
    config.wait = wait

    # Login

    browser.get("https://wattlecourses.anu.edu.au/")

    try:
        wait.until(presence_of_element_located((By.NAME, "j_username")))
    except TimeoutException:
        info_error("timed out waiting for Wattle login page")
        logout()
        sys.exit(1)

    assert "Australian National University Login Service" in browser.title

    elem = browser.find_element_by_name("j_username")
    elem.clear()
    elem.send_keys(get_username())

    elem = browser.find_element_by_name("j_password")
    elem.clear()
    elem.send_keys(get_password())

    elem.send_keys(Keys.RETURN)

    try:
        wait.until(presence_of_element_located((By.ID, "page-my-index")))
    except TimeoutException:
        info_error("timed out waiting after login")
#        logout()
        sys.exit(1)

    assert "Dashboard" in browser.title, "fais: failed to login to Wattle"

    return(browser)


@pass_config
def logout(config):
    config.browser.close()


# VALIDATION


def validate_uid(ctx, param, value):
    if re.match(r'^[uU]\d{7}$', value):
        return value
    raise click.BadParameter(f"'{value}'. Should be like 'u1234567'.")


# MESSAGES

def info_message(uid_or_group, message, colour=None, err=False):
    """Write to stdout with format `KEY: ___`"""
    click.secho("{}".format(uid_or_group), nl=False, fg=colour, err=err)
    click.echo(": {}".format(message))


def info_success(uid_or_group, message):
    """Write success to stdout with format `KEY: ___` in green colour"""
    info_message(uid_or_group, message, "green")


def info_warning(message):
    """Write warning to stdout with format `KEY: ___` in orange colour"""
    info_message(APP, message, "yellow")


def info_error(message):
    """Write error to stdout with format `KEY: ___` in red colour"""
    info_message(APP, message, "red", err=True)
