# rotate-cisco-enable-secret
This repository consists of a module. The module consists of 3 x scripts main, utils & paramikoModule.

main.py
This script calls the other two python scripts. It consists of the logic and provides a human readable interface to the user

utils.py
This script has got functions for the banner, menu options, get credentials of the user & get the new secret to be configured

paramikoModule.py
This script can be used as a great paramiko template for other python programmes as well.
It provides functions to connect to a cisco IOS device, get shell, send commands, close sessions and show the output

USAGE
In order to use this programme, just download the 3 x python scripts and store them in the same folder.
Run the main.py script and follow the terminal instructions.
