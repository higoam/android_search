#!/usr/bin/python3
#coding: utf-8

import sys

from controller.BreakLog import BreakLog
from model.LogSections import LogSections
from controller.Analyzing import Analyzing

def main():

#    analyzingObj = Analyzing()

    # Ler arquivo                                                                                   
    # ------------------------------------------------------------------------|
    pathDump = sys.argv[1]
    file = open(pathDump,'r+b')
    dumpstate = file.read()
    file.close()



    dumpstateStr = str(dumpstate)


    # Segment every parts of the log
    # ------------------------------------------------------------------------|
    brokenLog = BreakLog(dumpstateStr)

    # Verifica BugReport e faz análise
    # ------------------------------------------------------------------------|
#    if log_segmenting.strBUGREPORT == 1:
#        print("\nNo support for Bugreport version 1")
#    elif log_segmenting.strBUGREPORT == 2:
#        analyzing_sluggish.createReport(log_segmenting)
#    else:
#        print("BUGREPORT VERSION NOT KNOWN")




# ------------------------------------------------------------------------|
main()


