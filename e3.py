import os
import sys
sys.stdout = open("run.txt", "w")
import datetime

cmd = 'cat run.txt |grep days'
help(datetime)

os.system(cmd)
 
sys.stdout.close()

