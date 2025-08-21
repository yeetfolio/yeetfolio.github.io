import ctypes, sys # Check admin rights and exit the program(sys.exit).
from time import sleep # Delay prompts/text outputs so users can actually read them.
import subprocess # Run the process required to KILL(Murder(Unlive)) Windows.
######################################################
# BULLSHIT FOR WINDOWS VERSION 1.0 -- MANGOLOVER1899 #
######################################################
# * This program is designed to crash your computer. #
#   It is designed for Windows-based PCs, and won't  #
#   run on Mac's and Linux's.                        #
######################################################
######################################################
# COPYRIGHT NOTICE                                   #
######################################################
# Copyright (C) 2025 mangolover1899(itsyeetsup).     #
# Free to distribute for commercial, personal,       #
# public and private use. Created by Jacob           #
# Hache.                                             #
######################################################
def is_admin(): # Check for admin priviliges
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin(): # Code to run with admin privs
    print("yo") # Get the users attention.
    sleep(3)
    print("[1;37;41mYO PAY ATTENTION[0m") # Sudo get the users attention.
    sleep(5)
    print("I'm gonna [31mBSOD[0m your computer now bro") # Get the damn user's attention and warn them.
    sleep(4.5)
    print("I'm not joking bro") # Make sure the user is warned.
    sleep(1.8)
    print("I'm doing it...") # Extra warning for liability reasons.
    sleep(3)
    print("5...") # 5-Second countdown from 5 going down by one every second, about the length of a 5-second countdown
    sleep(1)      # which counts down from 5 to 1 every second, equal to the length of a 5-second countdown timer that
                  # counts down from within 5 seconds of time. Very simple concept.
    print("[1;33m4[0m...")
    sleep(1)
    print("[33m3[0m...")
    sleep(1)
    print("[1;31m2[0m...")
    sleep(1)
    print("[31m1[0m...")
    sleep(1)
    print("[47;31mRIP BRO :([0m") # Heat death(THE FINAL WARNING).
    sleep(3)
    try:      
       subprocess.run("taskkill /F /IM svchost.exe") # Computer go brrr.
                     # ^^^^^^^^ Taskkill process kills a very important process.
                     #          This causes windows to absolutely shit its pants
                     #          and die its own subsequent heat death in the form
                     #          of a BSOD. We want this, this is intentional.
    except:
        sleep(5)
        print("I guess that didn't work... Bruh.") # It's not my fault its yours, it works just fine on my end,         
        sys.exit(1)                                # so skill issue.
else: # what to do without admin superiority:
    print("You need [45;34;1m A D M I N I S T R A T O R   P E R M I S S I O N S [0m to run this program.")
  # ^^^^^ Let them know they need to be priveledged.
    sleep(2.5)
    print("[43;31m A T T E N T I O N(very important): [0m") # Warn them BEFORE they start crashing their PC.
    def confirmation(prompt="[33mType [1;31mYES[22;33m to confirm:[0;1;34m ", key="YES"): # Set up a prompt to
        try:                                                                                      # make sure they WANT
            userconfirm = input(prompt)                                                           # to murder their PC.
            if userconfirm == key: # Return True if user confirms:
                return True
            elif userconfirm.upper() == key:
                return True
            else:                  # Return False otherwise:
                return False
        except KeyboardInterrupt: # Detect ^C/KeyboardInterrupt's: 
            print("") # Empty line to move text out of prompt.
            sleep(1)
            return False
    print("This program will [31mCRASH[0m your computer. To continue, please confirm the prompt below:")
  # ^^^^^^ Bring up previous prompt:
    if not confirmation(): # What to do if prompt is unconfirmed:
        print("[0mAlright, turning back...") 
        sys.exit(0) # Sadly admit defeat and leave.
    # ...and if the prompt IS confirmed:
    print("[0mAsking for admin permissions now...") # Tell user you're asking for admin now.
    sleep(3.5)
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1) # Ask for admin.
