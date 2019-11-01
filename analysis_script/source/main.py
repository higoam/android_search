#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from controller.BreakLog2 import BreakLog2
from model.LogSections import LogSections
from controller.Analyzing import Analyzing

def main():

    # Ler arquivo                                                                                   
    # ------------------------------------------------------------------------|
    logReadText = read_log()

    # Segment every parts of the log
    # ------------------------------------------------------------------------|
    brokenLog = BreakLog2(logReadText)


    # Analyze Parts
    # ------------------------------------------------------------------------|
#    analyzingDump = Analyzing()
#    analyzingDump.createReport()

#    print(brokenLog.logSections.strCPU_INFO)

    # Verifica BugReport e faz análise
    # ------------------------------------------------------------------------|
#    if log_segmenting.strBUGREPORT == 1:
#        print("\nNo support for Bugreport version 1")
#    elif log_segmenting.strBUGREPORT == 2:
#        analyzing_sluggish.createReport(log_segmenting)
#    else:
#        print("BUGREPORT VERSION NOT KNOWN")

#    analyzingObj = Analyzing()


def read_log():

    # Get Parameter
    strDump = sys.argv[1]

    # Open File Log
    file = open(strDump,"rb")
    logReadText = file.read()
    file.close()

    logReadText = logReadText.decode('utf-8',errors='ignore')

    return str(logReadText)

# ------------------------------------------------------------------------|
main()


