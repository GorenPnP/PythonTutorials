# how to use imports? Nobody will ever know :(
# except somebody tell it you:
import os

# just imports os with no extra name, members can accesed via os.<method name>
print(os.getlogin())

import os as system
# now we import os as system means, we access every member from os via system instead of os
print(system.getlogin())

# now we import the function getLogin directly and can use them without a prefix
from os import getlogin
print(getlogin())

# we import from os the member getlogin, wich is in our case a function, BUT HEY everything is an object in python
# we have import getlogin now and changed the name
from os import getlogin as loginname
print(loginname())
from os import _exit as exit
exit(1)
# just as an example