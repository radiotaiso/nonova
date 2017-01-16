#/bin/python

#PREREQUISITES TO RUN THIS THING
# -ConfigParser
# -nova-cli? or will it be hosted in tchai? if tchai true, we need to make it public
import os
#https://docs.python.org/2/library/configparser.html
import configparser
from optparse import argumentParser
from argparse import ArgumentParser

#Requerir el archivo de config, si no existe, prompt user/pass y crear uno
nonovaconfigfile="nonovaconfig.ini" # Esto no creo que deba estar aqui pero sirve de momento


class NoNovaOptsParser(ArgumentParser):
    def __init__(self):
        usage = "usage %prog [arguments]"
        self.add_argument("-c" "--la-conf", dest="config",
                  help="Set config file with user:pass")
        self.add_argument("-A", "--de-actividades",
                  help="Print the activity arguments with ID")
        self.add_argument("-P", "--de-proyectos",
                  help="Print your personal project arguments with ID, This requires CONF FILE ")
        self.add_argument("-papu",
                  help="saca el pack papu")

class NoNovaConfigParser(ConfigParser):
    def __init__(self):
        super(self).__init__()
        configp = configparser.ConfigParser()
        if (os.path.isfile(nonovaconfigfile)):
            print("%s file found" %nonovaconfigfile)
            configp.read(nonovaconfigfile)
        else:
            print("Error: %s file not found" %nonovaconfigfile)
    #    NoNovaConfigParserCreate()
    #def NoNovaConfigParserCreate:
            print ("Creating new text file...")
            print ("-------------------------")
            user = raw_input("What's your username? ")
            password = raw_input("What's your password? Pinky promise we won't share it")
            print ("thanks that's all, we'll let you know when is finished")
            configp.add_section("Credentials")
            configp.set("Credentials","user",user)
            configp.set("Credentials","pass",password)
                        "Your username is %(user) and your password is secret, you can always update it in "+nonovaconfigfile+" where this project is located."

        with open(nonovaconfigfile, "wb") as config_file:
            configp.write(config_file)

def tablitaActividades():
    print "You will be required the activity ID"
    print "------------------------------------"
    actividades = {1:"Coding",2:"Meeting w/Client",3:"Design",4:"Meeting",5:"Support",6:"Training",7:"Fix/Debug",8:"Project Hours",9:"Research",11:"Project Review",12:"Project Management",13:"Architect",14:"Testing / QA",15:"Estimation",16:"PTO",17:"Holiday",18:"Analysis",19:"UI Graphic Design",20:"Code Redesign",21:"iTexico MX Task",23:"Interviewing",24:"Recruting",25:"Documentation",26:"Environment Setup",27:"Technical Advising",28:"TL",29:"Vacation"}
    for key in actividades:
        print key,"......",actividades[key]

def tablitaProyectos:
    #Login with default
    #Request Projects
    #Save it in the same config file as the user/pass? and request it everytime "llenamelo.py" runs
def config():

def test():

def main()




if __name__ == "__main__" :






 llenamelo --config

 user
 pass
 Default Project:
 Default Activity:
Duracion [obligatorio]:

FLOW DEMBOW PARA LLENAR ACTIVIDADES:

user [default]:
project [default]:
activity [default]:
time?
Another? Y/n
Change something on next activity? Y/n
(add N number of activities)

Cambiar algo? y/N
if respuesta == y:
1
Proyecto / Actividad / Tiempo / Texto
2
Proyecto / Actividad / Tiempo / Texto
N
Proyecto / Actividad / Tiempo / Texto

    Which one? 1,2,3? 1

    prompt>
        login? y/N
        project?
        Activity
        Duracion?

Cambiar algo? y/N
if respuesta ==N:
Submitting o k ase

!!!error handling
Success, id1 id2 id3
O fail por que te la pelas










#REFERENCIAS AL NOVA CLI DE GOLANG

# nova-cli  /u ucoria@itexico.net /p itexico1 add /P 33 /t 8 /c 14 Training with Antonio

# /P Projects------------------------------------------
# ID      Name
# 6       iTexico MX Delivery
# 1056    Envoy Phase 2
# 1069    Almer Test Team
# 1078    Clarifire - Development
# 1081    Entitlement
# 1093    Tandyner - Test Team
# 1092    Ryder POD Mobile
# 1091    Pisa FarmacoVigilancia - Test Team
# 1079    Development phase
# 33      Carbon Black Enterprise Response

# /c Categories---------------------------------------
# ID      Name
# 1       Coding
# 2       Meeting w/Client
# 3       Design
# 4       Meeting
# 5       Support
# 6       Training
# 7       Fix/Debug
# 8       Project Hours
# 9       Research
# 11      Project Review
# 12      Project Management
# 13      Architect
# 14      Testing / QA
# 15      Estimation
# 16      PTO
# 17      Holiday
# 18      Analysis
# 19      UI Graphic Design
# 20      Code Redesign
# 21      iTexico MX Task
# 23      Interviewing
# 24      Recruting
# 25      Documentation
# 26      Environment Setup
# 27      Technical Advising
# 28      TL
# 29      Vacation
