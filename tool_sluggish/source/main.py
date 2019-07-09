#!/usr/bin/python
#coding: utf-8

import sys
from parts.analyzeSlugging import analyzeSlugging
from parts.breakLog import breakLog

def main():

    # Get Parameter
    strDump = sys.argv[1]

    # Open File Log
    file = open(strDump,"rb")
    logDump = file.read()
    file.close()

    # Segment parts of the log
    logBroke = breakLog(logDump)

#    print(logBroke.strSYSTEM_PROPERTIES)

    sluggingData = analyzeSlugging(logBroke)



#    print("\n")
#    print("Garbage Collector:")
#    print(sluggingData.counter_garbage_collector)
#    print(sluggingData.lines_garbage_collector)

#    print("\n")
#    print("Low Memory Killer:")
#    print(sluggingData.counter_low_memory_killer)
#    print(sluggingData.lines_low_memory_killer)


#    print(logBroke.strSYSTEM_PROPERTIES)





main()


#print("Teste")

#file = open("/home/higof/Documents/DUMPS/dumpState_J410GUBU1ASE5_201905241059.log","rb")
#log = file.read()
#file.close()


#print(log)



