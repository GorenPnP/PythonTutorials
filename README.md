# PythonTutorials
## Download contents of this repo as zip
If you do not want to setup git, you can download contents as zip. But you would have to download a slightly changed package again and again on each change.

## Setup git on Windows
Download git for windows [here](https://git-scm.com/download/win) and click through the installing wizard.
You may leave all settings at their default, except you want to have an Icon on your Desktop or do not need a fancy gui\:

![screenshot_general_settings](doc/images/1_general_settings.PNG)

You can also change the default editor git uses, if you are not familiar with vi\:

![screenshot_default_editor](doc/images/2_default_editor.PNG)

One last thing you **should** change is one setting concerning newlines, since they are different in Windows and Linux systems\:

![screenshot_newline_settings](doc/images/3_newline_config.PNG)

When the installation is completed, start git-cmd and move in a directory where you want to clone the files of thos repository into. (to **c**hange **d**irectories, use `cd <dirname>`. To change into the parent directory, use `cd ..`. Go back to your home dir with just `cd`). Then type/paste `git clone https://github.com/GorenPnP/PythonTutorials.git` and you should have a new directory containing everything in this repo.

## Thoughts on the folder-structure
You will find a possible solution for every excercise in aufgaben/ in loesungen/. Also, the naming of files in both directories is nearly identical, so you may find specific ones easily.

The files in tutorial_code/ are meant to be read, since they contain typical constructs and are heavily commented, just as most solutions in loesungen/ are. There, you will also find a cheatsheet containing basic language features of python3.

We hope this helps you learn a pretty noice language \:D
