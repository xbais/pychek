
########################
#                      #
#        PYCHEK        #
#                      #
########################

# Author : Aakash Singh Bais

import sys
from tqdm import tqdm
from colorama import init
init()
from colorama import Fore, Back, Style
from time import time
import os
import psutil # cpu, gpu and ram stats
import logging, inspect
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
from pyfiglet import Figlet
header_fig = Figlet(font='graffiti')

# Global Constants
PID = os.getpid()
print(Fore.RED + "PID = " + str(PID) + Style.RESET_ALL, end="\n") 

# Global variables
#checkpt_count = 0
last_time = time() # will track the time of the last checkpt
checkpt_dict = {} # Will track all checkpoint stats including time
seen_files = [] # List of files that have been seen by the get_call_count function
total_checkpoints = 0
current_checkpoint = 0
#pbar = tqdm(total=0) # TQDM progress bar object
#pbar.set_description("Checkpt Progress")

#print = tqdm.write

def print_(string:str) -> None:
    frame, fileName, line_number, function_name, lines, index = inspect.stack()[2]
    pre = Fore.LIGHTMAGENTA_EX #Fore.BLACK + Back.WHITE
    post = Style.RESET_ALL
    logging.info(f"[{pre}{fileName}{post} : {pre}ln {line_number}{post} : {pre}{function_name}{post}{Style.RESET_ALL}] \n{string}\n")
    return
"""
def set_tqdm(total:int):
    global pbar
    
    #if pbar == None:
    #    pbar = tqdm(total=total)
    #else:
    pbar.total = total
    pbar.refresh()
"""
def reset_chkpt():
    "Resets the global variable checkpoint_count to 0"

    global checkpt_count

    checkpt_count = 0
    return checkpt_count

def get_call_count(file_location:str): # From Python file
    global seen_files
    # Add file to the list of seen files
    if file_location not in seen_files:
        print("[ SCAN ] " + file_location)
        seen_files.append(file_location)

        # If file not already seen, count function calls in the file
        with open(file_location, "r") as _:
            data = _.readlines()
        
        count = 0
        
        for line in data: # TODO : Optimisation needed
            line = line.strip()
            if "check(" in line and line.split("check(")[0] == "" and not ("check(\"header\"" in line or "check('header'" in line):
                count += 1
        print("[ SCAN result ] +" + str(count) + " checkpoints")
        return count
    else:
        return -1

def check(*arguments):
    """Prints the checkpoint, keeping a track of the checkpoint count. First argument is status.
       The status codes are:
            pass. Okay
            warn. Warning
            error. Error
    """
    global last_time, checkpt_dict, seen_files, total_checkpoints, current_checkpoint
    end = ""

    # Getting the Python file location of the calling function (to get the total count of the calls)
    namespace = sys._getframe(1).f_globals  # caller's globals
    if '__file__' not in namespace.keys():
        print("ERROR : You are probably trying to run PyChek from a Python Interactive session. This is currently not supported, try using in a Python script instead.")
        exit()

    caller_path = namespace['__file__'] # Location of the calling python file
    
    call_count = get_call_count(caller_path)
    
    if call_count != -1:
        total_checkpoints += call_count
        #set_tqdm(total_checkpoints)
        pass
    #if arguments[0] == "pass":
    #    end = "\r"
    
    if arguments[0] == "header":
        statement = Fore.YELLOW + "".join([str(header_fig.renderText(_)) for _ in arguments[1:]]) + Style.RESET_ALL
        print("\n" + statement+end)
        return statement
    elif arguments[0] == "info":
        current_checkpoint += 1
        statement = f"[ Chk {str(current_checkpoint)}/{str(total_checkpoints)} ]\t" + " ℹ️ " + Back.CYAN + Fore.BLACK + " INFO " + Style.RESET_ALL + " :\t" + Fore.CYAN + "".join([str(_) for _ in arguments[1:]]) + Style.RESET_ALL
        print_(statement + end)
        return statement
    elif arguments[0] == "finish":
        statement = ">>>\t" + Back.GREEN + Fore.BLACK + " Program execution finished. " + Style.RESET_ALL + "\t<<<"
        print_(statement + end)
        return statement

    # Time stats
    new_time = time()
    time_taken = new_time - last_time
    last_time = new_time

    statement = ""
    current_checkpoint += 1
    status = arguments[0].lower()
    status_values = ["pass", "warn", "error"]
    status_symbols = ["✅", "⚠️", "❌"]
    bullet_colour_values = [Back.GREEN + Fore.BLACK, Back.YELLOW + Fore.BLACK, Back.RED + Fore.WHITE]
    text_colour_values = [Fore.GREEN, Fore.YELLOW, Fore.RED]

    assert status in status_values

    bullet_colour = bullet_colour_values[status_values.index(status)]
    text_colour = text_colour_values[status_values.index(status)]
    status_symbol = status_symbols[status_values.index(status)]

    for argument in arguments[1:]:
        statement += str(argument)

    print_(f"[ Chk {str(current_checkpoint)}/{str(total_checkpoints)} ]\t" + f" {status_symbol} " + bullet_colour + " " + status.upper() + " " + Style.RESET_ALL + " :\t" + text_colour + statement + Style.RESET_ALL + "\t\t" + Fore.BLUE + "(t = " + str(round(time_taken,3)) + " s)" + Style.RESET_ALL + end)
    #pbar.update(1)
    return statement

# TODO : RAM, CPU, GPU monitoring checks and warnings

if __name__ == "__main__":
    print("#"*5 + " Everything is okay. " + "#"*5)
    print("Please use this Python script as a module, by importing it in other scripts.")
