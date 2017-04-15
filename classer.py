import os
import sys
import logging
import subprocess
import getpass
from configparser import ConfigParser


class NoNovaConfigParser(ConfigParser):
    def __init__(self, args):
        ConfigParser.__init__(self)
        self.args = args
        self.config_file = args.config
        self.osPlatform = sys.platform
        self.user = ""
        self.password = ""
        self._check_config()
        logging.info("Checking if there is any config file!")

    def _check_config(self):
        # print(self.args.config)
        if self.read(self.args.config):
            # self.read(self.args.config)
            # print "File Found!"
            self.userConfirm = self.get("Credentials","user")
            self.passConfirm = self.get("Credentials","pass")
            self.osPlatformC = self.get("Credentials","os")
            # print "Your credentials are {} and {} and currently running on {}".format(self.userConfirm, self.passConfirm,self.osPlatformC)
            logging.info("Nice! there's the config file!")
            logging.info("Your credentials are {} and {} and currently running on {}".format(self.userConfirm, self.passConfirm,self.osPlatformC))
        else:
            logging.info("Oh shoot! couldn't find any! let'sa go maek one!")
            self._create_config()

    def _create_config(self):
        print ("Creating new text file...")
        print ("-------------------------")

        while not self.user:
            self.user = raw_input("What's your username?: ")
            if not self.user:
                print('ups! Any user added, please try again')
        while not self.password:
            self.password = getpass.getpass("What's your password? Pinky promise we won't share it: ")
            if not self.password:
                print('mmm, you not add any password! Please try again')


        print ("Thanks that's all, we'll let you know when is finished")
        self.add_section("Credentials")
        self.add_section("Activities")
        self.set("Credentials","user",self.user)
        self.set("Credentials","pass",self.password)
        self.set("Credentials","OS",self.osPlatform)
        with open(self.args.config, "wb") as config_file:
            try:
                self.write(config_file)
            finally:
                print("Remember use the -p option to fetch your projects! You only need to do this once!")
                logging.info("Config file created!!")
# --------- ends NoNovaConfigParser class -----------------


class NovaCliConn():
    def __init__(self, conffile):
        self.confile = conffile
        self.path = self.check_os()
        self.user = conffile.get("Credentials", "user")
        self.pwd = conffile.get("Credentials", "pass")

    def execute(self, command):
        # Construct command
        self.payload = os.getcwd().replace('\\','/')+ "{} {} -u {} -p {}".format(self.path, command, self.user, self.pwd)
        logging.info("Executing order 66")
        logging.info(self.payload)
        # Execute by subprocess
        try:
            output = subprocess.check_output(self.payload, shell=True)
        except subprocess.CalledProcessError as e:
            print("No error belongs nowhere: {}".format(e))
        finally:
            pass

    def check_os(self):
        if sys.platform == ("win32" or "Windows" or "win64"):
            return "\\bin\\win\\nova-cli.exe"
        elif sys.platform == "darwin":
            return "/bin/osx/nova-cli"
        elif sys.platform == "Linux" or "Linux2":
            return "Sorry dude, but trix es solo para chavos."

    def test_exec(self, command): #Just prints, no real input to nova-cli
        self.payload = "{} {} -u {} -p {}".format(self.path, command, self.user, self.pwd)
        print (self.payload)
        logging.info("Why are you here? you're not supposed to come to test_exec")
