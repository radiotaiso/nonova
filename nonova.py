#!/bin/python
# -*- coding: utf-8 -*-
#PREREQUISITES TO RUN THIS THING
# -Python27
# -ConfigParser
# -ArgParse
# -nova-cli? or will it be hosted in tchai? if tchai true, we need to make it public

import sys
import logging
from argparse import ArgumentParser
from classer import NoNovaConfigParser
from classer import NovaCliConn
import activity
import re
from nonova_exceptions import InvalidCategoryException, InvalidProjectException

activities = []

id_name_regex = re.compile("(\d+)\s+([^\n]+)\n")

# --------- Arg Parser arguments --------------------------


def cli_parser():
    parser = ArgumentParser(description = """Command line helper for filling nova""")
    parser.add_argument("-c" " --config", dest="config", help="You must run this only the first time", type=str, default="config.ini")
    parser.add_argument("-C" " --category", dest="category", help="Show categories available", action="store_true")
    parser.add_argument("-p" " --project", dest="getp", help="Show your project list", action="store_true")
    parser.add_argument("-a" " --activity", dest="new_activity", help="Insert new set of activities", action="store_true")
    parser.add_argument("-r" " --read", dest="read", help="Read from file and upload activities found", action="store_true")
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    return args

def new_activity():
    logging.info("Starting to add activities n' stuff")

    # activities.append(a)
    stop_input = "y"
    invalid_data = 'true'
    b = activity.Activity()
    while stop_input.lower().strip()[0] == 'y':
        a = activity.Activity()
        # while invalid_data == 'true':
        #     invalid_data = 'false'
        #     if not a.project:
        #         invalid_data = 'true'
        a.project = raw_input("Project number?[{}]: ".format(b.project)) or b.project
        #     if not a.category:
        #         invalid_data = 'true'
        if not validate_project(a.project):
            raise InvalidProjectException("%s is not a valid project, please enter one of the following\n: %s" % (
                a.project, backend.execute("projects")
            ))
        a.category = raw_input("Category number?[{}]: ".format(b.category)) or b.category
        #     if not a.hours:
        #         invalid_data = 'true'
        if not validate_category(a.category):
            raise InvalidCategoryException("%s is not a valid category, please enter one of the following\n: %s" % (
                a.category, backend.execute("categories")
            ))
        a.hours = raw_input("Number of hours?[{}]: ".format(b.hours)) or b.hours
        #     if not a.comment:
        #         invalid_data = 'true'
        a.comment = raw_input("Comment?[{}]: ".format(b.comment)) or b.comment
        b = a
        print backend.execute(a.toString())

        # Adding to file
        store = raw_input("Want to save activity to file? [y/N]")
        if store == "y".lower().strip()[0]:
            save_activity(a)

        # Loop
        stop_input = raw_input("Want to add another? [Y/n]: ") or "y"
        logging.info("add another? %s", stop_input)


def get_projects(): # Only changes the word to send
    projects_response = backend.execute("projects")
    logging.info("Yo, I just checked my projects!")
    return id_name_regex.findall(projects_response)


def get_categories(): # Should we be saving this in the .ini file? To avoid requiring it from nova each time and quicker printing.
    categories_response = backend.execute("categories")
    logging.info("Mah categories dawg! here they are")
    return id_name_regex.findall(categories_response)


def save_activity(act):
    """

    :type act: Activity objetc
    """
    for i in act.attribute_list:
        novaconf.set("Activities", "{} {}".format(act.id, i), getattr(act, i))
    with open(novaconf.args.config, "wb") as config_file:
        try:
            novaconf.write(config_file)
        finally:
            logging.info("Activity {} added to config".format(act.id))


def read_from_file():
    file_activities = {}
    activity_values = []
    passes = 1
    novaconf.read(novaconf.args.config)
    for (each_key, each_val) in novaconf.items("Activities"):
        keys = {}
        k, v = each_key.split(" ")
        keys[v] = each_val
        activity_values.append(keys)
        file_activities[k] = activity_values
        if passes == 4:
            activity_values = []
        passes += 1
    return file_activities


def add_from_file():
    file_act = read_from_file()
    if file_act.keys() > 0:
        logging.info("Pack de actividades encontrado papu")
        for i in file_act.keys():
            a = activity.Activity()
            dic = file_act[i]
            for v in dic:
                for k in v:
                    setattr(a, k, v[k])
            print backend.execute(a.toString())


def validate_project(project_id):
    """

    :param project_id: integer, the project_id to validate
    :return: boolean Wether the received project_id is a valid one or not.
    """

    backend = NovaCliConn(novaconf)
    projects = get_projects()
    if isinstance(project_id, str):
        try:
            project_id = int(project_id.strip())
        except ValueError, e:
            return False
    return any([project[0] for project in projects if int(project[0].strip()) == project_id])
    pass

def validate_category(category_id):
    """

    :param activity_id: integer, the activity_id to validate
    :return: boolean Wether the receivedactivity_id is a valid one or not.
    """
    backend = NovaCliConn(novaconf)
    categories = get_categories()
    if isinstance(category_id, str):
        category_id = int(category_id.strip())
    return any([category[0] for category in categories if int(category[0].strip()) == category_id])
    pass

def main():
    global novaconf
    global backend
    logging.basicConfig(filename='nonovawtf.log' ,format='%(asctime)s - %(levelname)s:%(message)s',datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    #Parse teh world (one command line at a time)
    logging.info("WOOOOT I\'M ALIVE MTF!")
    args = cli_parser()
    # Read config file, if not, create one.
    novaconf = NoNovaConfigParser(args)
    # Ensure connection to nova-cli backend
    backend = NovaCliConn(novaconf)
    # Choose your destiny

    if args.new_activity:
        new_activity()
    elif args.getp:
        print backend.execute("projects")
    elif args.category:
        print backend.execute("categories")
    elif args.read:
        add_from_file()

if __name__ == "__main__":
    sys.exit(main())
