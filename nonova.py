#/bin/python

#PREREQUISITES TO RUN THIS THING
# -Python27
# -ConfigParser
# -ArgParse
# -nova-cli? or will it be hosted in tchai? if tchai true, we need to make it public
import os
import sys
import platform
## https://docs.python.org/2/library/configparser.html
from configparser import ConfigParser
from argparse import ArgumentParser

class NoNovaConfigParser(ConfigParser):
    def __init__(self, conf_file):
        self.configp = ConfigParser()
        self.nonovaconfigfile = conf_file
    def nonova_create_config(self):
            print ("Creating new text file...")
            print ("-------------------------")
            self.user = raw_input("What's your username?: ")
            self.password = raw_input("What's your password? Pinky promise we won't share it: ")
            print ("Thanks that's all, we'll let you know when is finished")
            self.configp.add_section("Credentials")
            self.configp.set("Credentials","user",self.user)
            self.configp.set("Credentials","pass",self.password)
            self.osPlatform = ""
            self.osPlatform = platform.system()
            self.configp.set("Credentials","OS",self.osPlatform)

            with open(self.nonovaconfigfile, "wb") as config_file:
                self.configp.write(config_file)
            print "Config file created!"
            print "Remember use the -p option to fetch your projects! You only need to do this once!"
    def nonova_confirm_config(self):
            self.configp.read(self.nonovaconfigfile)
            print "File Found!"
            self.userConfirm = self.configp.get("Credentials","user")
            self.passConfirm = self.configp.get("Credentials","pass")
            self.osPlatformC = self.configp.get("Credentials","os")
            print "Your credentials are {} and {} and currently running on {}".format(self.userConfirm, self.passConfirm,self.osPlatformC)
    def nonova_get_projects(self):
            self.configp.read(self.nonovaconfigfile)
            self.userConfirm = self.configp.get("Credentials","user")
            self.passConfirm = self.configp.get("Credentials","pass")
            self.osPlatform = self.configp.get("Credentials","os")
            self.pathToCli = ""
            self.nnString = "{} /u {} /p {} projects".format(self.pathToCli,self.userConfirm,self.passConfirm)
            if osPlatform == "Windows":
                 self.pathToCli="/bin/win/nova-cli.exe"
                 print self.nnString
            elif osPlatform == "Darwin":
                 pathToCli="/bin/osx/nova-cli"
            elif osPlatform == "Linux" or "Linux2":
                 pathToCli="/bin/linux"


# --------- ends NoNovaConfigParser class -----------------
# --------- Arg Parser arguments --------------------------
def cli_parser():
    parser = ArgumentParser(description = """Command line helper for filling nova""")
    parser.add_argument("-c" " --config", dest="config", help="You must run this only the first time", type=str)
    parser.add_argument("-p" " --project", dest="getp", help="Update your project list", type=str)
    parser.add_argument("-A" ,dest="activity", help="Print the activity arguments with ID",action="store_true")
    # parser.add_argument("-P", "--de-proyectos",
    # help="Print your personal project arguments with ID, This requires CONF FILE ")
    # parser.add_argument("--papu", dest="papu", help="summon papu" default="saca el pack papu", action="store", type=str)
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    return args
# ---- Arg Parser Options! ------------------------------------------
def config(args):
    # Verify conf file exists, else create_cofig
    if not os.path.exists(confparse.nonovaconfigfile):
        confparse.nonova_create_config()
    else:
        print confparse.nonovaconfigfile
        confparse.nonova_confirm_config()

def update_projects(args):
    print "si entra al update_projects"
    print confparse.nonovaconfigfile
    # if not os.path.exists(confparse.nonovaconfigfile)::
    #     print "config.ini was not found, you must create one first."
    #     confparse.nonova_create_config()
    # else:
    #     confparse.nonova_get_projects()


def activity():
    print "You will be required the activity ID"
    print "------------------------------------"
    actividades = {
            1:"Coding",2:"Meeting w/Client",3:"Design",4:"Meeting",
            5:"Support",6:"Training",7:"Fix/Debug",8:"Project Hours",
            9:"Research",11:"Project Review",12:"Project Management",
            13:"Architect",14:"Testing / QA",15:"Estimation",16:"PTO",
            17:"Holiday",18:"Analysis",19:"UI Graphic Design",
            20:"Code Redesign",21:"iTexico MX Task",23:"Interviewing",
            24:"Recruting",25:"Documentation",26:"Environment Setup",
            27:"Technical Advising",28:"TL",29:"Vacation"}
    for key in actividades:
        print "{} ...... {}".format(key, actividades[key])
# ----- END Arg Parser Options ------------------------------------
def main():
    global confparse
    args = cli_parser()
    confparse = NoNovaConfigParser(args)
    if args.activity:
        activity()
    if args.config:
        config(args)
    if args.getp:
        update_projects(args)


if __name__ == "__main__":
    sys.exit(main())
