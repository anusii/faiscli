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
from selenium.webdriver.common.keys import Keys

import pandas as pd

APP = "fais"
URL = "https://cs.anu.edu.au/fais/staff/"


class Config(object):

    def __init__(self):
        self.debug = None
        self.human = None
        self.browser = None
        self.fake = None
        self.wait = None
        self.private = os.path.expanduser("~/.config/fais/config.json")

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
        username = os.environ.get("FAIS_USERNAME")
        source = "environment variable FAIS_USERNAME"
    elif os.path.exists(config.private):
        with open(config.private, 'r') as file:
            username = yaml.safe_load(file)["username"]
            source = config.private
    else:
        try:
            username = input("Username: ")
            source = "prompt"
        except Exception:
            info_error("a username is required to continue.")
            sys.exit(1)

    if username == "":
        info_error(f"empty username according to {source}.")
        sys.exit(1)

    if config.debug:
        info_success(f"username obtained from {source}.")

    return username


@pass_config
def get_password(config):
    if os.environ.get("FAIS_PASSWORD"):
        password = os.environ.get("FAIS_PASSWORD")
        source = "environment variable FAIS_PASSWORD"
    elif os.path.exists(config.private):
        with open(config.private, 'r') as file:
            password = yaml.safe_load(file)["password"]
            source = config.private
    else:
        try:
            password = getpass.getpass()
            source = "prompt"
        except Exception:
            info_error("a password is required to continue")
            sys.exit(1)

    if password == "":
        info_error(f"empty password according to {source}.")
        sys.exit(1)

    if config.debug:
        info_success(f"password obtained from {source}.")

    return password


def html2csv(table):
    rows = table.find_all("tr")
    writer = csv.writer(sys.stdout)
    for row in rows:
        csv_row = []
        for cell in row.find_all(["td", "th"]):
            csv_row.append(cell.get_text())
        writer.writerow(csv_row)


@pass_config
def login(config):

    username = get_username()
    password = get_password()

    # Driver/Session

    options = webdriver.ChromeOptions()

    if not config.debug:
        options.headless = True

    browser = webdriver.Chrome(options=options)
    config.browser = browser

    # Login

    browser.get(URL + "StaffDetails.php")
    assert "FAIS Login" in browser.title

    elem = browser.find_element_by_name("Username")
    elem.clear()
    elem.send_keys(username)

    elem = browser.find_element_by_name("Password")
    elem.clear()
    elem.send_keys(password)

    elem.send_keys(Keys.RETURN)

    if "FAIS Details" not in browser.title:
        info_error(f"failed to login as user '{username}'")
        sys.exit(1)

    return(browser)


@pass_config
def logout(config):
    config.browser.close()


# VALIDATION


def validate_uid(ctx, param, value):
    """Check the University ID and optionally strip email address."""
    if re.match(r'^[uU]\d{7}$', value):
        return value
    elif re.match(r'^[uU]\d{7}@anu.edu.au$', value):
        return value.replace("@anu.edu.au", "")
    raise click.BadParameter(f"'{value}'. Should be like 'u1234567'.")


# MESSAGES

def info_message(uid_or_group, message, colour=None, err=False):
    """Write to stdout with format `KEY: ___`"""
    click.secho("{}".format(uid_or_group), nl=False, fg=colour, err=err)
    click.echo(": {}".format(message))


def info_success(message):
    """Write success to stdout with format `KEY: ___` in green colour"""
    info_message(APP, message, "green")


def info_warning(message):
    """Write warning to stdout with format `KEY: ___` in orange colour"""
    info_message(APP, message, "yellow")


def info_error(message):
    """Write error to stdout with format `KEY: ___` in red colour"""
    info_message(APP, message, "red", err=True)
