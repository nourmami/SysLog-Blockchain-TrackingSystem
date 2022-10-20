import os
import time
lines=5
with open("filename.txt") as file:

        for line in file:
            pass
        last_line = line
while(1):
    with open("filename.txt") as file:

        for line in file:
            pass
        if (last_line != line):
            splited = last_line.split(', ')
            msg = splited[2]+ splited[4]+splited[5]
            msg = msg.replace(' ', '_')

            msg = msg.replace('(', '_')

            msg = msg.replace(')', '_')
            shell='LOG'+str(lines)+' '+msg.strip()+' '+str(splited[0])+' '+str(splited[3])+' '+str(splited[1])
            #print (shell)
            os.system('./shell.sh '+shell)
            lines+=1
            time.sleep(3)
            last_line=line
            
        
