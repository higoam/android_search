

class breakLog:

    def __init__(self, logText):
        self.logText = logText
        self.logate = "HIGO"

        # Strings to store sections
        self.strHEADER_LOG = ""

        self.strEVENT_LOG = ""
        self.strSYSTEM_LOG = ""
        self.strSYSTEM_PROPERTIES = ""

        self.strCPU_INFO = ""

        self.strMEMORY_INFO = ""
        self.strDUMPSYS_MEMINFO = ""


        self.strDUMPSYS_BATTERY = ""
        self.strDUMPSYS_WIFI = ""

        self.strDUMPSYS_ACTIVITY = ""
        self.strDUMPSYS_PACKAGE = ""
        self.strDUMPSYS_WINDOW = ""
        self.strDUMPSYS_POWER = ""
        self.strDUMPSYS_NETSTATS = ""
        self.strDUMPSYS_AUDIO = ""
        self.strDUMPSYS_ALARM = ""


        self.segmentImportantSections(logText)
#        self.updateEventTypes()



# ------------------------------------------------------------------------|
# ------------------------------------------------------------------------|
# ------------------------------------------------------------------------|
    def segmentImportantSections(self, stringAux):
        vet_stringAux = stringAux.splitlines(True)

        TAG_Collect_EVENT_LOG = 0
        TAG_Collect_SYSTEM_LOG = 0
        TAG_Collect_SYSTEM_PROPERTIES = 0

        TAG_Collect_MEMORY_INFO = 0
        TAG_Collect_DUMPSYS_MEMINFO = 0

        TAG_Collect_CPU_INFO = 0

        STR_HEADER_LOG_AUX = ""

        STR_EVENT_LOG_AUX = ""
        STR_SYSTEM_LOG_AUX = ""
        STR_SYSTEM_PROPERTIES = ""

        STR_MEMORY_INFO = ""
        STR_DUMPSYS_MEMINFO = ""

        STR_CPU_INFO_AUX = ""

        # Discovers the bugreport and header collection
        # ----------------------------------------------------------------|
        for line in vet_stringAux:
            STR_HEADER_LOG_AUX = STR_HEADER_LOG_AUX + line

            if line.find('Bugreport format version: 1.0') != -1:
                VERSION_BUGREPORT = 1
            elif line.find('Bugreport format version: 2.0') != -1:
                VERSION_BUGREPORT = 2

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

            if (line.find('Total PSS by process:') != -1):
                TAG_Collect_DUMPSYS_MEMINFO = 1
            elif line.find('Tuning:') != -1 and (TAG_Collect_DUMPSYS_MEMINFO == 1):
                TAG_Collect_DUMPSYS_MEMINFO = 2

            if (line.find('------ CPU') != -1):
                TAG_Collect_CPU_INFO = 1
            elif line.find('was the duration of \'CPU') != -1 and (TAG_Collect_CPU_INFO == 1):
                TAG_Collect_CPU_INFO = 2



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
            if TAG_Collect_CPU_INFO == 1:
               STR_CPU_INFO_AUX = STR_CPU_INFO_AUX + line


        self.strEVENT_LOG = STR_EVENT_LOG_AUX
        self.strSYSTEM_LOG = STR_SYSTEM_LOG_AUX
        self.strSYSTEM_PROPERTIES = STR_SYSTEM_PROPERTIES
        self.strDUMPSYS_MEMINFO = STR_DUMPSYS_MEMINFO
        self.strMEMORY_INFO = STR_MEMORY_INFO
        self.strCPU_INFO = STR_CPU_INFO_AUX




# ------------------------------------------------------------------------|
# ------------------------------------------------------------------------|
# ------------------------------------------------------------------------|
    def updateEventTypes(self):
        print(" Method: updateEventTypes")

        list_file = list()
        list_log = list()
        new_list = list()

        # Read file Type Events
        file_types_events = open("../data/types_of_known_events.txt", "r")
        types_events = file_types_events.read()
        file_types_events.close()
        vet_types_events = types_events.splitlines()

        for line in vet_types_events:
            new_list.append(line)


        # Read Log Type Events
        vet_stringAux = self.strEVENT_LOG.splitlines()
        for line in vet_stringAux:
            line_AUX = line[39:]
            line_AUX = line_AUX[:line_AUX.find(':')]

            if line_AUX not in new_list:
                new_list.append(line_AUX)

#        print("FILE")
#        for x in list_file:
#            print(x)

#        print("LOG")
#        for x in list_log:
#            print(x)

#        for iten in list_log:


        new_list.extend(list_file)
        new_list.extend(list_log)

        print("NEW LIST")
        for x in new_list:
            print(x)

        # Get Events of Logs Now



        # Add two lists



        # Write new file Type Events



