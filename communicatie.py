import subprocess
import time
from jlink import *

#cjlink = ['/opt/JLink_Linux_V664_arm/JLinkExe', '-Device', 'NRF52832_XXAA', '-speed', '4000', '-if', 'SWD', '-autoconnect', '1']
#flash_command = cjlink + ['i']
#session = subprocess.Popen(cjlink, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#stdout = session.communicate()

#for line in iter(stdout):
#    if line.decode('utf-8') == '':
#        break
#    print(line.decode('utf-8'))
#    print('hoi')

#if session.returncode != 0:
#    print("FAILED!")

#print(session.returncode)

#run_commands(self,'connect',60)

ob = Programmer()
commands = JLink(ob)
x = commands.run_commands(['connect','','s','','i','exit'], 0)
print (x)