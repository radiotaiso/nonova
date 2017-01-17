#/bin/python

#PREREQUISITES TO RUN THIS THING
# -Python27
# -ConfigParser
# -ArgParse
# -nova-cli? or will it be hosted in tchai? if tchai true, we need to make it public
import os
import sys
## https://docs.python.org/2/library/configparser.html
from configparser import ConfigParser
from argparse import ArgumentParser

class NoNovaConfigParser(ConfigParser):
    def __init__(self, conf_file):
        self.configp = ConfigParser()
        self.nonovaconfigfile = conf_file
        # if (os.path.isfile(self.nonovaconfigfile)):
        #     print("%s file found" % self.nonovaconfigfile)
        #     self.configp.read(self.nonovaconfigfile)
        # else:
        #     print("Error: %s file not found" % self.nonovaconfigfile)
        #     self.nonova_create_config()
    def nonova_create_config(self):
            print ("Creating new text file...")
            print ("-------------------------")
            self.user = raw_input("What's your username?: ")
            self.password = raw_input("What's your password? Pinky promise we won't share it: ")
            print ("Thanks that's all, we'll let you know when is finished")
            self.configp.add_section("Credentials")
            self.configp.set("Credentials","user",self.user)
            self.configp.set("Credentials","pass",self.password)
            with open(self.nonovaconfigfile, "wb") as config_file:
                self.configp.write(config_file)
            print "Config file created!"
            print "Remember use the -p option to fetch your projects! You only need to do this once!"
    def nonova_confirm_config(self):
            print "Entra a nonova_confirm_config"
            print "one step in the right direction"
            self.configp.read(self.nonovaconfigfile)
            userConfirm = self.configp.get("Credentials","user")
            passConfirm = self.configp.get("Credentials","pass")
            print "Success!"
            print "Your credentials are {} and {}".format(userConfirm, passConfirm)
def cli_parser():
    parser = ArgumentParser(description = """Command line helper for filling nova""")
    parser.add_argument("-c" " --config", dest="config", help="Config file", type=str)
    parser.add_argument("-A" ,dest="activity", help="Print the activity arguments with ID",action="store_true")
#    parser.add_argument("-P", "--de-proyectos",
    # help="Print your personal project arguments with ID, This requires CONF FILE ")
    # parser.add_argument("--papu", dest="papu", help="summon papu" default="saca el pack papu", action="store", type=str)
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    return args

def config(args):
    # Verify conf file exists, else create_cofig
    confparse = NoNovaConfigParser(args.config)
    if not os.path.exists(confparse.nonovaconfigfile):
        confparse.nonova_create_config()
    else:
        # Everything here moves to a func to be the same as the if
        confparse.nonova_confirm_config()
        # user = confparse.get("Credentials","user")
        # password = confparse.get("Credentials","pass")
        # print "Success!"
        # print "Your credentials are {} and {}".format(user, password)
        # Login to nova CLI using Credentials :D
        # Maybe a success message

def activity():
    print "You will be required the activity ID"
    print "------------------------------------"
    actividades = {1:"Coding",2:"Meeting w/Client",3:"Design",4:"Meeting",5:"Support",6:"Training",7:"Fix/Debug",8:"Project Hours",9:"Research",11:"Project Review",12:"Project Management",13:"Architect",14:"Testing / QA",15:"Estimation",16:"PTO",17:"Holiday",18:"Analysis",19:"UI Graphic Design",20:"Code Redesign",21:"iTexico MX Task",23:"Interviewing",24:"Recruting",25:"Documentation",26:"Environment Setup",27:"Technical Advising",28:"TL",29:"Vacation"}
    for key in actividades:
        print "{} ...... {}".format(key, actividades[key])

def main():
    args = cli_parser()
    if args.activity:
        activity()
    if args.config:
        config(args)

if __name__ == "__main__":
    sys.exit(main())
