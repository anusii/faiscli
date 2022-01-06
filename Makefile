########################################################################
#
# Makefile for fais command line interface
#
# Time-stamp: <Thursday 2022-01-06 15:50:50 +1100 Graham Williams>
#
# Copyright (c) Graham.Williams@togaware.com
#
# License: Creative Commons Attribution-ShareAlike 4.0 International.
#
########################################################################

# App version numbers
#   Major release
#   Minor update
#   Trivial update or bug fix

APP=fais
VER=0.1.0
DATE=$(shell date +%Y-%m-%d)

########################################################################
# Supported Makefile modules.

# Often the support Makefiles will be in the local support folder, or
# else installed in the local user's shares.

INC_BASE=./support

# Specific Makefiles will be loaded if they are found in
# INC_BASE. Sometimes the INC_BASE is shared by multiple local
# Makefiles and we want to skip specific makes. Simply define the
# appropriate INC to a non-existant location and it will be skipped.

INC_DOCKER=skip

include $(INC_BASE)/modules.mk

########################################################################
# HELP
#
# Help for targets defined in this Makefile.

define HELP
$(APP) cli:

  install	Developer install $(APP) locally (only needed once)

  enrolments	Example use of the enrolments command
  student       Example use of the student command

endef
export HELP

help::
	@echo "$$HELP"

########################################################################
# LOCAL TARGETS

enrolments: comp8410y20wi.tbl

comp3430s2y21.csv:
	$(APP) --csv enrolments 12886 > $@

comp8430s2y21.csv:
	$(APP) --csv enrolments 12887 > $@

comp8430s2y21.tbl:
	$(APP) enrolments 12887

comp8410y20wi.tbl:
	$(APP) enrolments 12635

student:
	@echo "Get a student UID and run '$(APP) student <uid>'"

# Install in dev mode (-e) so changes here are immediately deployed.

install:
	pip install -e .
