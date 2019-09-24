#!/usr/bin/python
#coding: utf-8

import sys

from controller.breakLog import breakLog
from model.log_segment import log_segment
from controller.analyzingSluggish import analyzingSluggish

def main():

    broken_log = breakLog()
    analyzing_sluggish = analyzingSluggish()


    # Get Parameter
    strDump = sys.argv[1]

    # Open File Log
    file = open(strDump,"rb")
    logReadText = file.read()
    file.close()

    # Create Object of log segmented, input read log
    log_segmenting = log_segment(logReadText)

    # Discovers the bugreport and header collection
    # Segment every parts of the log
    log_segmenting = broken_log.segmentImportantSections(log_segmenting)

    if log_segmenting.strBUGREPORT == 1:
        analyzing_sluggish.memory(log_segmenting)


#        print("BUGREPORT VERSION 1")
#        log_segmenting = broken_log.segment_EVENT_LOG(log_segmenting)
#        log_segmenting = broken_log.segment_SYSTEM_LOG(log_segmenting)


    elif log_segmenting.strBUGREPORT == 2:
        analyzing_sluggish.memory(log_segmenting)
        analyzing_sluggish.cpu(log_segmenting)

#        print(log_segmenting.strPPOCESSES_AND_THREADS)

#        print("BUGREPORT VERSION 2")
#       log_segmenting = broken_log.segment_EVENT_LOG(log_segmenting)
#       log_segmenting = broken_log.segment_SYSTEM_LOG(log_segmenting)
#        print(log_segmenting.strSYSTEM_LOG)
#        print(log_segmenting.strDUMPSYS_PROCSTATS)
#        analyzing_sluggish.memory(log_segmenting)
#        analyzing_sluggish.cpu(log_segmenting)
#        analyzing_sluggish.temperature(log_segmenting)
#        analyzing_sluggish.inputSystem(log_segmenting)

#        analyzing_sluggish.SYSTEM_LOG(log_segmenting)
#        analyzing_sluggish.SYSTEM_LOG(log_segmenting)


    else:
        print("BUGREPORT VERSION NOT KNOWN")



#   log_segmenting = broken_log.segment_EVENT_LOG(log_segmenting)
#   log_segmenting = broken_log.segment_SYSTEM_LOG(log_segmenting)
#   log_segmenting = analyzing_slugging_log.analyze_EVENT_LOG(log_segmenting)


#    for item in log_segmenting.listEVENT_LOG:
#        print(item[9])



#    print(log_segmenting.strEVENT_LOG)
#    print(log_segmenting.strSYSTEM_LOG)
#    print(log_segmenting.strSYSTEM_PROPERTIES)
#    print(log_segmenting.strMEMORY_INFO)
#    print(log_segmenting.strCPU_INFO)



#    sluggingData = analyzeSlugging(logBroke)



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



