#/bin/python

#PREREQUISITES TO RUN THIS THING
# -ConfigParser
# -nova-cli? or will it be hosted in tchai? if tchai true, we need to make it public
import os
#https://docs.python.org/2/library/configparser.html
import configparser
from argparse import ArgumentParser



class NoNovaConfigParser(ConfigParser):
    def __init__(self):
        super(self).__init__()
        self.configp = configparser.ConfigParser()
        nonovaconfigfile="nonovaconfig.ini"
        if (os.path.isfile(nonovaconfigfile)):
            print("%s file found" %nonovaconfigfile)
            self.configp.read(nonovaconfigfile)
        else:
            print("Error: %s file not found" %nonovaconfigfile)
            self.NoNovaCreateConfig()
    def NoNovaCreateConfig(self):
            print ("Creating new text file...")
            print ("-------------------------")
            user = raw_input("What's your username? ")
            password = raw_input("What's your password? Pinky promise we won't share it")
            print ("thanks that's all, we'll let you know when is finished")
            self.configp.add_section("Credentials")
            self.configp.set("Credentials","user",user)
            self.configp.set("Credentials","pass",password)

        with open(nonovaconfigfile, "wb") as config_file:
            self.configp.write(config_file)

def cli_parser():
    parser = ArgumentParser(description = """Command line helper for filling nova""")
    parser.add_argument("-c" " --config", dest="config", help="Config file")
    parser.add_argument("-A" " --de-actividades",
    help="Print the activity arguments with ID")
#    parser.add_argument("-P", "--de-proyectos",
    #help="Print your personal project arguments with ID, This requires CONF FILE ")
    parser.add_argument("--papu", dest="papu", default='saca el pack papu', action="store", type=str)
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    #return args

if __name__ == "__main__":
    sys.exit(cli_parser())
