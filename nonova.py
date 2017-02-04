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

def main():
    args = cli_parser()
    novaconf = NoNovaConfigParser(args)
    if args.new_activity:
        print("New activity")
    elif args.getp:
        print("Get projects")
    elif args.category:
        print("Get categories")
    elif args.config:
        print("Config file")



if __name__ == "__main__":
    sys.exit(main())
