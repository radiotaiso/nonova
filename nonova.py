#!/bin/python

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
    parser.add_argument("-C" " --category", dest="category", help="Show categories of activities", action="store_true")
    parser.add_argument("-p" " --project", dest="getp", help="Update your project list", action="store_true")
    parser.add_argument("-a" " --activity", dest="new_activity", help="Insert new activity", action="store_true")
    parser.add_argument("-A", dest="from file", help="Reads activity from file", action="store_true")
    # parser.add_argument("-P", "--de-proyectos",
    # help="Print your personal project arguments with ID, This requires CONF FILE ")
    # parser.add_argument("--papu", dest="papu", help="summon papu" default="saca el pack papu", action="store", type=str)
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    return args

def new_activity():
    global a
    another = "y"
    a = Activity()
    while raw_input("Add another [y/n]?:").lower().strip()[0] == "y":
        project = raw_input("Project number?[{}]: ".format(a.project)) or a.project
        # projectP = project
        category = raw_input("Category number?[{}]: ".format(a.category)) or a.category
        # categoryP = category
        hours = raw_input("Number of hours?[{}]: ".format(a.hours)) or a.hours
        # hoursP = hours
        #ticket = raw_input("Ticket?: ")
        comment = raw_input("Comment?[{}]: ".format(a.comment)) or a.comment
        # comment = commentP
        a = Activity(Project=project, Category=category, Hours=hours, Comment=comment)
        backend.execute(a.toString())

def get_projects():
    backend.execute("projects")

def get_categories():
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
