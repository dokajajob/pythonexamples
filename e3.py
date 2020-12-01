import sys
sys.stdout = open("run.txt", "w")
import datetime

help(datetime)
 
sys.stdout.close()

