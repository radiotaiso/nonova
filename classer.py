from configparser import ConfigParser


class NoNovaConfigParser(ConfigParser):
    def __init__(self, args):
        ConfigParser.__init__(self)
        print("slf")
        self.args = args
        self.config_file = args.config
        self.osPlatform = ""
        self.user = ""
        self.password = ""
        self._check_config()

    def _check_config(self):
        print(self.args.config)
        if self.read(self.args.config):
            print("Yes")
        else:
            self._create_config()

    def _create_config(self):
        print ("Creating new text file...")
        print ("-------------------------")
        self.user = raw_input("What's your username?: ")
        self.password = raw_input("What's your password? Pinky promise we won't share it: ")
        print ("Thanks that's all, we'll let you know when is finished")
        self.add_section("Credentials")
        self.set("Credentials","user",self.user)
        self.set("Credentials","pass",self.password)
        self.set("Credentials","OS",self.osPlatform)
        with open(self.args.config, "wb") as config_file:
            try:
                self.write(config_file)
            finally:
                print "Config file created!"
                print "Remember use the -p option to fetch your projects! You only need to do this once!"

    def confirm_config(self):
            self.read(self.args.config)
            print "File Found!"
            self.userConfirm = self.get("Credentials","user")
            self.passConfirm = self.get("Credentials","pass")
            self.osPlatformC = self.get("Credentials","os")
            print "Your credentials are {} and {} and currently running on {}".format(self.userConfirm, self.passConfirm,self.osPlatformC)

    def get_projects(self,pathToCli): # Gets projects from configured credentials
            self.read(self.args.config)
            self.userConfirm = self.get("Credentials","user")
            self.passConfirm = self.get("Credentials","pass")
            self.fn = os.path.join(os.path.dirname(__file__),pathToCli) + " projects"
            print self.fn
            #raw_input
            if self.osPlatform == "Darwin":
                call(self.fn, shell=True)
            else:
                print self.fn
                p = subprocess.check_output(self.fn).splitlines()
                for i in p:
                    tab = {}
                    print i.split("\t")

# --------- ends NoNovaConfigParser class -----------------


class NovaCliConn(self):
    def __init__(self):
        self.nova_path = 
