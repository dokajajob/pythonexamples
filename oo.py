import os

cmd = 'cat run.txt |grep days'

out = os.system(cmd)

print(out)
