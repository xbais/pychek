########################
#                      #
#       pyProdigy      #
#                      #
########################

# Author : Aakash Singh Bais

import sys
import tqdm
from colorama import init
init()
from colorama import Fore, Back, Style
from time import time
import os
import psutil # cpu, gpu and ram stats

from pyfiglet import Figlet
header_fig = Figlet(font='graffiti')

# Global Constants
PID = os.getpid()
print(Fore.RED + "PID = " + str(PID) + Style.RESET_ALL) 

# Global variables
checkpt_count = 0
last_time = time() # will track the time of the last checkpt
checkpt_dict = {} # Will track all checkpoint stats including time

def reset_chkpt():
    "Resets the global variable checkpoint_count to 0"

    global checkpt_count

    checkpt_count = 0
    return checkpt_count

def check(*arguments):
    """Prints the checkpoint, keeping a track of the checkpoint count. First argument is status.
       The status codes are:
            pass. Okay
            warn. Warning
            error. Error
    """
    global checkpt_count, last_time, checkpt_dict
    end = "\n"
    #if arguments[0] == "pass":
    #    end = "\r"

    if arguments[0] == "header":
        statement = Fore.YELLOW + "".join([str(header_fig.renderText(_)) for _ in arguments[1:]]) + Style.RESET_ALL
        print(statement, end=end)
        return statement
    elif arguments[0] == "info":
        statement = Fore.BLUE + "INFO :\t" + Style.RESET_ALL + "".join([str(_) for _ in arguments[1:]])
        print(statement, end=end)
        return statement
    elif arguments[0] == "finish":
        statement = ">>>\t" + Back.GREEN + Fore.BLACK + " Program execution finished. " + Style.RESET_ALL + "\t<<<"
        print(statement, end=end)
        return statement

    # Time stats
    new_time = time()
    time_taken = new_time - last_time
    last_time = new_time

    statement = ""
    checkpt_count += 1
    status = arguments[0].lower()
    status_values = ["pass", "warn", "error"]
    colour_values = [Fore.GREEN, Fore.YELLOW, Fore.RED]

    assert status in status_values

    fore_colour = colour_values[status_values.index(status)]

    for argument in arguments[1:]:
        statement += str(argument)

    print("[ Check-" + str(checkpt_count) + " ]\t" + fore_colour + status.upper() + Style.RESET_ALL + " : " + statement + "\t\t" + Fore.BLUE + "(t = " + str(round(time_taken,3)) + " s)" + Style.RESET_ALL, end=end)
    return statement

# TODO : RAM, CPU, GPU monitoring checks and warnings

if __name__ == "__main__":
    print("#"*5 + " Everything is okay. " + "#"*5)
    print("Please use this Python script as a module, by importing it in other scripts.")
