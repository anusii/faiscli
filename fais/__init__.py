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
# Details of the GNU General Public License v3 is available from
# https://www.gnu.org/licenses/gpl-3.0.en.html.
#
# This file is part of fais.
#
# Author: Graham.Williams@anu.edu.au


import sys
import click

import fais.commands as cmd
import fais.utils as utils

from fais.utils import pass_config

# Help message should report app as fais.

sys.argv[0] = utils.APP


# ----------------------------------------------------------------------
# Set up command line parser and dispatch commands.
# ----------------------------------------------------------------------

@click.group()
@click.option("-h", "--human", is_flag=True, default=False,
              help="Pretty print for human consumption.")
@click.option("-d", "--debug", is_flag=True, default=False,
              help="Display the browser.")

@pass_config
def cli(config, human, debug):
    """Access FAIS functionality from the command line."""
    config.human = human
    config.debug = debug

#    if False:  # command in ['wget']:
#        utils.login_wattle()
#    else:
#        utils.login_fais()


cli.add_command(cmd.courses)
cli.add_command(cmd.enrolments)
cli.add_command(cmd.final)
cli.add_command(cmd.function)
cli.add_command(cmd.stats)
cli.add_command(cmd.student)
cli.add_command(cmd.students)
cli.add_command(cmd.wmarks)

if __name__ == '__main__':
    try:
        cli()
    except KeyboardInterrupt:
        pass
