#!/bin/python
# -*- coding: utf-8 -*-

#PREREQUISITES TO RUN THIS THING
# -Python27
# -ConfigParser
# -ArgParse
# -nova-cli? or will it be hosted in tchai? if tchai true, we need to make it public
import os
import sys
import platform
import subprocess
from subprocess import call
from configparser import ConfigParser
from argparse import ArgumentParser
from classer import NoNovaConfigParser
from classer import NovaCliConn
from classer import Activity

# --------- Arg Parser arguments --------------------------
def cli_parser():
    parser = ArgumentParser(description = """Command line helper for filling nova""")
    parser.add_argument("-c" " --config", dest="config", help="You must run this only the first time", type=str, default="config.ini")
    parser.add_argument("-C" " --category", dest="category", help="Show categories available", action="store_true")
    parser.add_argument("-p" " --project", dest="getp", help="Show your project list", action="store_true")
    parser.add_argument("-a" " --activity", dest="new_activity", help="Insert new set of activities", action="store_true")
    parser.add_argument("-A", dest="from file", help="Reads activity from file --UNAVAILABLE", action="store_true")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    return args

def new_activity():
    a = Activity()
    stopInput = "y"
    while stopInput == "y".lower().strip()[0]:
        a.project = raw_input("Project number?[{}]: ".format(a.project))
        a.category = raw_input("Category number?[{}]: ".format(a.category))
        a.hours = raw_input("Number of hours?[{}]: ".format(a.hours))
        a.comment = raw_input("Comment?[{}]: ".format(a.comment))
        backend.execute(a.toString())
        # backend.test_exec(a.toString())
        stopInput = raw_input("Want to add another? [y/N]: ")

def get_projects(): # Only changes the word to send
    backend.execute("projects")

def get_categories(): # Should we be saving this in the .ini file? To avoid requiring it from nova each time and quicker printing.
    backend.execute("categories")

def main():
    global novaconf
    global backend
    #Parse teh world (one command line at a time)
    args = cli_parser()
    # Read config file, if not, create one.
    novaconf = NoNovaConfigParser(args)
    # Ensure connection to nova-cli backend
    backend = NovaCliConn(novaconf)
    # Choose your destiny

    if args.new_activity:
        new_activity()
    elif args.getp:
        get_projects()
    elif args.category:
        get_categories()

if __name__ == "__main__":
    sys.exit(main())
