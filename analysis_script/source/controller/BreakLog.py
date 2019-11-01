#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from model.LogSections import LogSections

class BreakLog:

# ------------------------------------------------------------------------|
# ----------------------------  Constructor ------------------------------|
# ------------------------------------------------------------------------|
    def __init__(self, dump):

        self.dumpstate = dump.splitlines()
        self.logSections = LogSections()

        self.segmentImportantSections()

# ------------------------------------------------------------------------|
# ---------------------  Segment Important Sections ----------------------|
# ------------------------------------------------------------------------|
    def segmentImportantSections(self):

        logSectionsAUX = LogSections()

        # ------------------------------------------------------------------------|
        # Copy Control Variables
        # ------------------------------------------------------------------------|
        copy_condition_EVENT_LOG = 0
        copy_condition_SYSTEM_LOG = 0
        copy_condition_SYSTEM_PROPERTIES = 0

        copy_condition_PROCESSES_AND_THREADS = 0

        copy_condition_MEMORY_INFO = 0
        copy_condition_DUMPSYS_MEMINFO = 0

        copy_condition_CPU_INFO = 0
        copy_condition_CPU_INFO_2 = 0

        copy_condition_TRACES = 0

        # ------------------------------------------------------------------------|
        # Variables with copies - Accumulator
        # ------------------------------------------------------------------------|
        STR_HEADER_LOG_AUX = ""

        STR_EVENT_LOG_AUX = ""
        STR_SYSTEM_LOG_AUX = ""


        STR_SYSTEM_PROPERTIES = ""
        STR_PROCESSES_AND_THREADS_AUX = ""

        STR_MEMORY_INFO = ""
        STR_DUMPSYS_MEMINFO = ""
        STR_DUMPSYS_PROCSTATS = ""

        STR_CPU_INFO_AUX = ""
        STR_CPU_INFO_2 = ""

        STR_TRACES = ""


# DESCARTE ---------------------------------------------------------------|
#        copy_condition_PROCSTATS = 0
# ------------------------------------------------------------------------|


        # Segment Header
        # Discovers the bugreport and header collection
        # ----------------------------------------------------------------|
        #for line in dumpAUX.splitlines():

            # Implementar Verificacao do BugReport


            #STR_HEADER_LOG_AUX = STR_HEADER_LOG_AUX + line

            #if line.find('Bugreport format version: 1.0') != -1:
            #    log_segmenting.strBUGREPORT = 1
            #elif line.find('Bugreport format version: 2.0') != -1:
            #    log_segmenting.strBUGREPORT = 2

            #if (line.find('------ MEMORY INFO') != -1):
            #    break
        print("\nFalta Implementar Verificacao do BugReport\n")


#        return 0
#        for line in self.dumpstate:
#            print(line)


        # Segment Sections
        # ----------------------------------------------------------------|
        for line in self.dumpstate:

#            print(line)

            # TAGs to enable copy text
            # ----------------------------------------------------------------|
            if (line.find('------ SYSTEM LOG') != -1):
                copy_condition_SYSTEM_LOG = 1
            elif line.find('was the duration of \'SYSTEM LOG\'') != -1 and (copy_condition_SYSTEM_LOG == 1):
                copy_condition_SYSTEM_LOG = 2

            if (line.find('------ EVENT LOG') != -1):
                copy_condition_EVENT_LOG = 1
            elif line.find('was the duration of \'EVENT LOG\'') != -1 and (copy_condition_EVENT_LOG == 1):
                copy_condition_EVENT_LOG = 2


#            if (line.find('------ SYSTEM PROPERTIES') != -1):
#                copy_condition_SYSTEM_PROPERTIES = 1
#            elif line.find('was the duration of \'SYSTEM PROPERTIES\'') != -1 and (copy_condition_SYSTEM_PROPERTIES == 1):
#                copy_condition_SYSTEM_PROPERTIES = 2


#            if (line.find('------ MEMORY INFO (/proc/meminfo)') != -1):
#                copy_condition_MEMORY_INFO = 1
#            elif line.find('was the duration of \'MEMORY INFO\'') != -1 and (copy_condition_MEMORY_INFO == 1):
#                copy_condition_MEMORY_INFO = 2


#            if (line.find('Total  (   PSS   SwapPss ) kB') != -1) or (line.find('DUMP OF SERVICE HIGH meminfo:') != -1):
#                copy_condition_DUMPSYS_MEMINFO = 1
#            elif line.find('Tuning:') != -1 and (copy_condition_DUMPSYS_MEMINFO == 1):
#                copy_condition_DUMPSYS_MEMINFO = 2


            #if (line.find('LAST 3 HOURS:') != -1):
            #    copy_condition_PROCSTATS = 1
            #elif line.find('Run time Stats:') != -1 and (copy_condition_PROCSTATS == 1):
            #    copy_condition_PROCSTATS = 2


#            if (line.find('DUMP OF SERVICE CRITICAL cpuinfo') != -1):
#                copy_condition_CPU_INFO = 1
#            elif line.find('was the duration of dumpsys cpuinfo') != -1 and (copy_condition_CPU_INFO == 1):
#                copy_condition_CPU_INFO = 2


#            if (line.find('------ CPU INFO') != -1):
#                copy_condition_CPU_INFO_2 = 1
#            elif line.find('was the duration of \'CPU INFO\'') != -1 and (copy_condition_CPU_INFO_2 == 1):
#                copy_condition_CPU_INFO_2 = 2


 #           if (line.find('------ PROCESSES AND THREADS') != -1):
#                copy_condition_PROCESSES_AND_THREADS = 1
#            elif line.find('was the duration of \'PROCESSES AND THREADS') != -1 and (copy_condition_PROCESSES_AND_THREADS == 1):
#                copy_condition_PROCESSES_AND_THREADS = 2


#            if (line.find('------ VM TRACES JUST NOW') != -1):
#                copy_condition_TRACES = 1
#            elif line.find('was the duration of \'VM TRACES JUST NOW\'') != -1 and (copy_condition_TRACES == 1):
#                copy_condition_TRACES = 2



            # Confirmation to copy line to section
            # ----------------------------------------------------------------|
            if copy_condition_SYSTEM_LOG == 1:
               STR_SYSTEM_LOG_AUX = STR_SYSTEM_LOG_AUX + line  + "\n"
            if copy_condition_EVENT_LOG == 1:
               STR_EVENT_LOG_AUX = STR_EVENT_LOG_AUX + line + "\n"
#            if copy_condition_SYSTEM_PROPERTIES == 1:
#               STR_SYSTEM_PROPERTIES = STR_SYSTEM_PROPERTIES + line + "\n"

#            if copy_condition_MEMORY_INFO == 1:
#               STR_MEMORY_INFO = STR_MEMORY_INFO + line + "\n"
#            if copy_condition_DUMPSYS_MEMINFO == 1:
#               STR_DUMPSYS_MEMINFO = STR_DUMPSYS_MEMINFO + line + "\n"
            #if copy_condition_PROCSTATS == 1:
            #   STR_DUMPSYS_PROCSTATS = STR_DUMPSYS_PROCSTATS + line

#            if copy_condition_CPU_INFO == 1:
#               STR_CPU_INFO_AUX = STR_CPU_INFO_AUX + line + "\n"
#            if copy_condition_CPU_INFO_2 == 1:
#               STR_CPU_INFO_2 = STR_CPU_INFO_2 + line + "\n"

#            if copy_condition_TRACES == 1:
#               STR_TRACES = STR_TRACES + line + "\n"

#            if copy_condition_PROCESSES_AND_THREADS == 1:
#                STR_PROCESSES_AND_THREADS_AUX = STR_PROCESSES_AND_THREADS_AUX + line + "\n"




#        logSectionsAUX.strHEADER_LOG = STR_HEADER_LOG_AUX

     #  # logSectionsAUX.strEVENT_LOG = STR_EVENT_LOG_AUX
     #   logSectionsAUX.strSYSTEM_LOG = STR_SYSTEM_LOG_AUX


#        for line in STR_EVENT_LOG_AUX.splitlines():
#            print(line)


#        logSectionsAUX.strPPOCESSES_AND_THREADS = STR_PROCESSES_AND_THREADS_AUX

#        logSectionsAUX.strSYSTEM_PROPERTIES = STR_SYSTEM_PROPERTIES

#        logSectionsAUX.strMEMORY_INFO = STR_MEMORY_INFO
#        logSectionsAUX.strDUMPSYS_MEMINFO = STR_DUMPSYS_MEMINFO
#        logSectionsAUX.strDUMPSYS_PROCSTATS = STR_DUMPSYS_PROCSTATS



#        logSectionsAUX.strCPU_INFO = STR_CPU_INFO_AUX
#        logSectionsAUX.strCPU_INFO_2 = STR_CPU_INFO_2

#        logSectionsAUX.strTRACES = STR_TRACES

        self.logSections = logSectionsAUX





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



