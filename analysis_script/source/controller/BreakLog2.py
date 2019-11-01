#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from model.LogSections import LogSections

class BreakLog2:

# ------------------------------------------------------------------------|
# ----------------------------  Constructor ------------------------------|
# ------------------------------------------------------------------------|
    def __init__(self, dump):

        self.dumpstate = dump
        self.logSections = LogSections()

        self.segmentImportantSections()

# ------------------------------------------------------------------------|
# ---------------------  Segment Important Sections ----------------------|
# ------------------------------------------------------------------------|
    def segmentImportantSections(self):

        # ------------------------------------------------------------------------|
        # Copy Control Variables
        # ------------------------------------------------------------------------|
        copy_condition_SYSTEM_LOG = 0
        copy_condition_EVENT_LOG = 0
        copy_condition_TRACES = 0

        # Segment Sections
        # ----------------------------------------------------------------|
        for line in self.dumpstate.splitlines():
            
            # TAGs to enable copy text
            # ----------------------------------------------------------------|
            if (line.find('------ EVENT LOG') != -1):
                copy_condition_EVENT_LOG = 1
            elif line.find('was the duration of \'EVENT LOG\'') != -1 and (copy_condition_EVENT_LOG == 1):
                copy_condition_EVENT_LOG = 2

#            if (line.find('------ SYSTEM LOG') != -1):
#                copy_condition_SYSTEM_LOG = 1
#            elif line.find('was the duration of \'SYSTEM LOG\'') != -1 and (copy_condition_SYSTEM_LOG == 1):
#                copy_condition_SYSTEM_LOG = 2

            if (line.find('------ VM TRACES JUST NOW') != -1):
                copy_condition_TRACES = 1
            elif line.find('was the duration of \'VM TRACES JUST NOW\'') != -1 and (copy_condition_TRACES == 1):
                copy_condition_TRACES = 2

            # Confirmation to copy line to section
            # ----------------------------------------------------------------|
            if copy_condition_EVENT_LOG == 1:
               self.logSections.strEVENT_LOG = self.logSections.strEVENT_LOG + line + "\n"

#            if copy_condition_SYSTEM_LOG == 1:
#               self.logSections.strSYSTEM_LOG = self.logSections.strSYSTEM_LOG + line + "\n"

            if copy_condition_TRACES == 1:
               self.logSections.strTRACES = self.logSections.strTRACES + line + "\n"


        print(self.logSections.strEVENT_LOG)

# ------------------------------------------------------------------------|
# ------------------------------------------------------------------------|
# ------------------------------------------------------------------------|
    def print_HEADER_LOG(self):

        print(self.logSections.strHEADER_LOG)


# ------------------------------------------------------------------------|
# ------------------------------------------------------------------------|
# ------------------------------------------------------------------------|
    def segment_EVENT_LOG(self, log_segmenting):

        print("")
        print(" Method: explore_EVENT_LOG")

        vet_EVENT_LOG = log_segmenting.strEVENT_LOG.splitlines()

        list_event_types = list()
        list_all_events = list()

        # Coleta Eventos
        for line in vet_EVENT_LOG:

            print(line)
            # Get month
            STR_AUX = line
            STR_month = STR_AUX[:2]

            # Get day
            STR_AUX = STR_AUX[3:]
            STR_day = STR_AUX[:2]

            # Get hour
            STR_AUX = STR_AUX[3:]
            STR_hour = STR_AUX[:2]

            # Get minute
            STR_AUX = STR_AUX[3:]
            STR_minute = STR_AUX[:2]

            # Get second
            STR_AUX = STR_AUX[3:]
            STR_second = STR_AUX[:6]

            # Get PID
            STR_AUX = STR_AUX[7:]
            STR_PID = STR_AUX[:5]

            # Get TID
            STR_AUX = STR_AUX[6:]
            STR_TID = STR_AUX[:5]

            # Get package
            STR_AUX = STR_AUX[6:]
            STR_package = STR_AUX[:5]

            # Get priority
            STR_AUX = STR_AUX[6:]
            STR_priority = STR_AUX[:1]

            # Get tag
            STR_AUX = STR_AUX[2 :]
            STR_tag = STR_AUX[:STR_AUX.find(':')]

            # Get message
            STR_AUX = STR_AUX[STR_AUX.find(':')+1:]
            STR_message = STR_AUX

            #             0         1        2          3           4          5        6          7             8          9         10
            tuple = (STR_month, STR_day, STR_hour, STR_minute, STR_second, STR_PID, STR_TID, STR_package, STR_priority, STR_tag, STR_message)
            list_all_events.append(tuple)

            if tuple[9] not in list_event_types:
                list_event_types.append(tuple[9])

        # Ordena Tipos de Eventos encontrados
        list_event_types.sort()

#        for item in list_event_types:
#            print(item)


        log_segmenting.listEVENT_LOG = list_all_events

        return log_segmenting







# ------------------------------------------------------------------------|
# ------------------------------------------------------------------------|
# ------------------------------------------------------------------------|
    def segment_SYSTEM_LOG(self, log_segmenting):

        print("")
        print(" Method: explore_SYSTEM_LOG")

        vet_SYSTEM_LOG = log_segmenting.strSYSTEM_LOG.splitlines()

        list_event_types = list()
        list_all_events = list()

        # Coleta Eventos
        for line in vet_SYSTEM_LOG:

            # Get month
            STR_AUX = line
            STR_month = STR_AUX[:2]

            # Get day
            STR_AUX = STR_AUX[3:]
            STR_day = STR_AUX[:2]

            # Get hour
            STR_AUX = STR_AUX[3:]
            STR_hour = STR_AUX[:2]

            # Get minute
            STR_AUX = STR_AUX[3:]
            STR_minute = STR_AUX[:2]

            # Get second
            STR_AUX = STR_AUX[3:]
            STR_second = STR_AUX[:6]

            # Get PID
            STR_AUX = STR_AUX[7:]
            STR_PID = STR_AUX[:5]

            # Get TID
            STR_AUX = STR_AUX[6:]
            STR_TID = STR_AUX[:5]

            # Get package
            STR_AUX = STR_AUX[6:]
            STR_package = STR_AUX[:5]

            # Get priority
            STR_AUX = STR_AUX[6:]
            STR_priority = STR_AUX[:1]

            # Get tag
            STR_AUX = STR_AUX[2 :]
            STR_tag = STR_AUX[:STR_AUX.find(':')]

            # Get message
            STR_AUX = STR_AUX[STR_AUX.find(':')+1:]
            STR_message = STR_AUX

            #             0         1        2          3           4          5        6          7             8          9         10
            tuple = (STR_month, STR_day, STR_hour, STR_minute, STR_second, STR_PID, STR_TID, STR_package, STR_priority, STR_tag, STR_message)
            list_all_events.append(tuple)

            if tuple[9] not in list_event_types:
                list_event_types.append(tuple[9])



        # Ordena Tipos de Eventos encontrados
        list_event_types.sort()


        log_segmenting.listSYSTEM_LOG = list_all_events

        return log_segmenting


#    def getLogSections(self):
#        return self.logSections



# ------------------------------------------------------------------------|
# ------------------------------------------------------------------------|
# ------------------------------------------------------------------------|
#    def updateEventTypes(self):
#        print(" Method: updateEventTypes")
#
#        list_file = list()
#        list_log = list()
#        new_list = list()

        # Read file Type Events
#        file_types_events = open("../data/types_of_known_events.txt", "r")
#        types_events = file_types_events.read()
#        file_types_events.close()
#        vet_types_events = types_events.splitlines()

#        for line in vet_types_events:
#            new_list.append(line)


        # Read Log Type Events
#        vet_stringAux = self.strEVENT_LOG.splitlines()
#        for line in vet_stringAux:
#            line_AUX = line[39:]
#            line_AUX = line_AUX[:line_AUX.find(':')]

#            if line_AUX not in new_list:
#                new_list.append(line_AUX)

#        print("FILE")
#        for x in list_file:
#            print(x)

#        print("LOG")
#        for x in list_log:
#            print(x)

#        for iten in list_log:


#        new_list.extend(list_file)
#        new_list.extend(list_log)

#        print("NEW LIST")
#        for x in new_list:
#            print(x)

        # Get Events of Logs Now



        # Add two lists



        # Write new file Type Events



