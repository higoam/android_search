
from model.log_segment import log_segment

class breakLog:

#    def __init__(self):
#        print()
        #print("Construct breakLog")
#        log_input = self.segmentImportantSections(log_input.strREAD_LOG)


# ------------------------------------------------------------------------|
# ------------------------------------------------------------------------|
# ------------------------------------------------------------------------|
    def segmentImportantSections(self, log_segmenting):

        vet_stringAux = log_segmenting.strREAD_LOG.splitlines(True)

        TAG_Collect_EVENT_LOG = 0
        TAG_Collect_SYSTEM_LOG = 0
        TAG_Collect_SYSTEM_PROPERTIES = 0
        TAG_Collect_PROCESSES_AND_THREADS = 0

        TAG_Collect_MEMORY_INFO = 0
        TAG_Collect_DUMPSYS_MEMINFO = 0
        TAG_Collect_PROCSTATS = 0

        TAG_Collect_CPU_INFO = 0


        STR_HEADER_LOG_AUX = ""

        STR_EVENT_LOG_AUX = ""
        STR_SYSTEM_LOG_AUX = ""
        STR_SYSTEM_PROPERTIES = ""
        STR_PROCESSES_AND_THREADS_AUX = ""

        STR_MEMORY_INFO = ""
        STR_DUMPSYS_MEMINFO = ""
        STR_DUMPSYS_PROCSTATS = ""

        STR_CPU_INFO_AUX = ""


        # Segment Header
        # Discovers the bugreport and header collection
        # ----------------------------------------------------------------|
        for line in vet_stringAux:
            STR_HEADER_LOG_AUX = STR_HEADER_LOG_AUX + line

            if line.find('Bugreport format version: 1.0') != -1:
                log_segmenting.strBUGREPORT = 1
            elif line.find('Bugreport format version: 2.0') != -1:
                log_segmenting.strBUGREPORT = 2

            if (line.find('------ MEMORY INFO') != -1):
                break


        # Segment Sections
        # ----------------------------------------------------------------|
        for line in vet_stringAux:

            # TAGs to enable copy text
            # ----------------------------------------------------------------|
            if (line.find('------ SYSTEM LOG') != -1):
                TAG_Collect_SYSTEM_LOG = 1
            elif line.find('was the duration of \'SYSTEM LOG\'') != -1 and (TAG_Collect_SYSTEM_LOG == 1):
                TAG_Collect_SYSTEM_LOG = 2

            if (line.find('------ EVENT LOG') != -1):
                TAG_Collect_EVENT_LOG = 1
            elif line.find('was the duration of \'EVENT LOG\'') != -1 and (TAG_Collect_EVENT_LOG == 1):
                TAG_Collect_EVENT_LOG = 2

            if (line.find('------ SYSTEM PROPERTIES') != -1):
                TAG_Collect_SYSTEM_PROPERTIES = 1
            elif line.find('was the duration of \'SYSTEM PROPERTIES\'') != -1 and (TAG_Collect_SYSTEM_PROPERTIES == 1):
                TAG_Collect_SYSTEM_PROPERTIES = 2




            if (line.find('------ MEMORY INFO (/proc/meminfo)') != -1):
                TAG_Collect_MEMORY_INFO = 1
            elif line.find('was the duration of \'MEMORY INFO\'') != -1 and (TAG_Collect_MEMORY_INFO == 1):
                TAG_Collect_MEMORY_INFO = 2

            if (line.find('Total  (   PSS   SwapPss ) kB') != -1) or (line.find('DUMP OF SERVICE HIGH meminfo:') != -1):
                TAG_Collect_DUMPSYS_MEMINFO = 1
            elif line.find('Tuning:') != -1 and (TAG_Collect_DUMPSYS_MEMINFO == 1):
                TAG_Collect_DUMPSYS_MEMINFO = 2

            if (line.find('LAST 3 HOURS:') != -1):
                TAG_Collect_PROCSTATS = 1
            elif line.find('Run time Stats:') != -1 and (TAG_Collect_PROCSTATS == 1):
                TAG_Collect_PROCSTATS = 2




            if (line.find('DUMP OF SERVICE CRITICAL cpuinfo') != -1):
                TAG_Collect_CPU_INFO = 1
            elif line.find('was the duration of dumpsys cpuinfo') != -1 and (TAG_Collect_CPU_INFO == 1):
                TAG_Collect_CPU_INFO = 2





            if (line.find('------ PROCESSES AND THREADS') != -1):
                TAG_Collect_PROCESSES_AND_THREADS = 1
            elif line.find('was the duration of \'PROCESSES AND THREADS') != -1 and (TAG_Collect_PROCESSES_AND_THREADS == 1):
                TAG_Collect_PROCESSES_AND_THREADS = 2





            # Confirmation to copy line to section
            # ----------------------------------------------------------------|
            if TAG_Collect_SYSTEM_LOG == 1:
               STR_SYSTEM_LOG_AUX = STR_SYSTEM_LOG_AUX + line
            if TAG_Collect_EVENT_LOG == 1:
               STR_EVENT_LOG_AUX = STR_EVENT_LOG_AUX + line
            if TAG_Collect_SYSTEM_PROPERTIES == 1:
               STR_SYSTEM_PROPERTIES = STR_SYSTEM_PROPERTIES + line

            if TAG_Collect_MEMORY_INFO == 1:
               STR_MEMORY_INFO = STR_MEMORY_INFO + line
            if TAG_Collect_DUMPSYS_MEMINFO == 1:
               STR_DUMPSYS_MEMINFO = STR_DUMPSYS_MEMINFO + line
            if TAG_Collect_PROCSTATS == 1:
               STR_DUMPSYS_PROCSTATS = STR_DUMPSYS_PROCSTATS + line

            if TAG_Collect_CPU_INFO == 1:
               STR_CPU_INFO_AUX = STR_CPU_INFO_AUX + line
            if TAG_Collect_PROCESSES_AND_THREADS == 1:
                STR_PROCESSES_AND_THREADS_AUX = STR_PROCESSES_AND_THREADS_AUX + line


        log_segmenting.strHEADER_LOG = STR_HEADER_LOG_AUX

        log_segmenting.strEVENT_LOG = STR_EVENT_LOG_AUX
        log_segmenting.strSYSTEM_LOG = STR_SYSTEM_LOG_AUX

        log_segmenting.strPPOCESSES_AND_THREADS = STR_PROCESSES_AND_THREADS_AUX

        log_segmenting.strSYSTEM_PROPERTIES = STR_SYSTEM_PROPERTIES

        log_segmenting.strMEMORY_INFO = STR_MEMORY_INFO
        log_segmenting.strDUMPSYS_MEMINFO = STR_DUMPSYS_MEMINFO
        log_segmenting.strDUMPSYS_PROCSTATS = STR_DUMPSYS_PROCSTATS


        log_segmenting.strCPU_INFO = STR_CPU_INFO_AUX

        return log_segmenting

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

#            print(line)

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



