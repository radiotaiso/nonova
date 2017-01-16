#/bin/python

#PREREQUISITES TO RUN THIS THING
# -ConfigParser
# -nova-cli? or will it be hosted in tchai? if tchai true, we need to make it public
import os
import sys
#https://docs.python.org/2/library/configparser.html
from configparser import ConfigParser
from argparse import ArgumentParser




class NoNovaConfigParser(ConfigParser):
    def __init__(self):
        super(self).__init__()
        self.configp = configparser.ConfigParser()
        self.nonovaconfigfile="nonovaconfig.ini"
        # if (os.path.isfile(self.nonovaconfigfile)):
        #     print("%s file found" % self.nonovaconfigfile)
        #     self.configp.read(self.nonovaconfigfile)
        # else:
        #     print("Error: %s file not found" % self.nonovaconfigfile)
        #     self.nonova_create_config()
    def nonova_create_config(self):
            print ("Creating new text file...")
            print ("-------------------------")
            self.user = raw_input("What's your username? ")
            self.password = raw_input("What's your password? Pinky promise we won't share it")
            print ("thanks that's all, we'll let you know when is finished")
            self.configp.add_section("Credentials")
            self.configp.set("Credentials","user",user)
            self.configp.set("Credentials","pass",password)
            with open(self.nonovaconfigfile, "wb") as config_file:
                self.configp.write(config_file)


def cli_parser():
    parser = ArgumentParser(description = """Command line helper for filling nova""")
    parser.add_argument("-c" " --config", dest="config", help="Config file", type=config)
    parser.add_argument("-a" " --de-actividades", help="Print the activity arguments with ID", type=activity)
#    parser.add_argument("-P", "--de-proyectos",
    #help="Print your personal project arguments with ID, This requires CONF FILE ")
    parser.add_argument("--papu", dest="papu", default='saca el pack papu', action="store", type=str)
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    #return args

def config():
    # Verify conf file exists, else create_cofig
    confparse = NoNovaConfigParser()
    if not os.path.exists(nonovaconfigfile):
        confparse.nonova_create_config()
    else:
        confparse.read(nonovaconfigfile)
        user = confparse.get("Credentials","user")
        password = confparse.get("Credentials","pass")
        #print "Your credentials are "+user+" and "+password
        # Login to nova CLI using Credentials :D
        # Maybe a success message

def activity():
    print ("You will be required the activity ID")
    print ("------------------------------------")
    actividades = {1:"Coding",2:"Meeting w/Client",3:"Design",4:"Meeting",5:"Support",6:"Training",7:"Fix/Debug",8:"Project Hours",9:"Research",11:"Project Review",12:"Project Management",13:"Architect",14:"Testing / QA",15:"Estimation",16:"PTO",17:"Holiday",18:"Analysis",19:"UI Graphic Design",20:"Code Redesign",21:"iTexico MX Task",23:"Interviewing",24:"Recruting",25:"Documentation",26:"Environment Setup",27:"Technical Advising",28:"TL",29:"Vacation"}
    for key in actividades:
        print (key,"......",actividades[key])

def main():
    cli_parser()

if __name__ == "__main__":
    sys.exit(cli_parser())
