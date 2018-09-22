# MAINLY THOUGHT TO BE EXCECUTED, I.E. LITTLE COMMENTING
import os, re

def recursive_print(directory, regex, tabs=""):
    """prints directory tree recursively, highlights files matching regex"""

    print(tabs[:-1] + "-\x1b[92m" + directory.strip() + "\033[0m")
    tabs += "| "

    dicts = []
    found_files = []
    for f in os.listdir(directory):
        if os.path.isdir(f):
            dicts.append(f)
        else:
            if regex.match(f):
                found_files.append(f)
                print(tabs + "\x1b[31m" + f + '\033[0m')
            else:
                print(tabs + f)

    for d in dicts:
        found_files += recursive_print(d, regex, tabs)
    
    return set(found_files)
    

if __name__ == "__main__":

    while True:

        print("\nDora sieht alles. Aber anders als sie haben wir nicht ewig lange Zeit nach mickrigen Details wie Dateien zu suchen. Die sie nie suchen würde. Aber selbst ihr dürften Regex gefallen.")
        print("Syntax is da: https://docs.python.org/3.3/library/re.html")

        regex = ""
        while not regex:

            regex = input(">> ")
            try:
                if not regex:
                    print("Das ist ja leer.")
                    continue
                regex = re.compile(".*" + regex + ".*")
            except:
                regex = ""


        # Getting the current work directory (cwd)
        thisdir = os.getcwd()
        founds = recursive_print(thisdir, regex)

