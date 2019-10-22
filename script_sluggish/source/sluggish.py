#!/usr/bin/python
#coding: utf-8

import sys

from controller.breakLog import breakLog
from model.log_segment import log_segment
from controller.analyzingSluggish import analyzingSluggish

def main():

    broken_log = breakLog()
    analyzing_sluggish = analyzingSluggish()


    # Ler arquivo
    # ------------------------------------------------------------------------|
    strDump = sys.argv[1]
    file = open(strDump,"rb")
    logReadText = file.read()
    file.close()


    # Segment every parts of the log
    # ------------------------------------------------------------------------|
    log_segmenting = log_segment(logReadText)
    log_segmenting = broken_log.segmentImportantSections(log_segmenting)


    # Verifica BugReport e faz análise
    # ------------------------------------------------------------------------|
    if log_segmenting.strBUGREPORT == 1:
        print("\nNo support for Bugreport version 1")
    elif log_segmenting.strBUGREPORT == 2:
        analyzing_sluggish.createReport(log_segmenting)
    else:
        print("BUGREPORT VERSION NOT KNOWN")







# ------------------------------------------------------------------------|
main()


