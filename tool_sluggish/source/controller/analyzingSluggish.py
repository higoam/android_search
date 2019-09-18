

import re
from logging import exception
from model.log_segment import log_segment

class analyzingSluggish:

#    def __init__(self):
#        print("")
        # Useful info for sluggin analysis
 #       self.counter_garbage_collector = ""
 #       self.lines_garbage_collector = ""
 #       self.counter_low_memory_killer = ""
 #       self.lines_low_memory_killer = ""

#        self.log_cat_V = ""
 #       self.log_cat_D = ""
  #      self.log_cat_I = ""
   #     self.log_cat_W = ""
    #    self.log_cat_E = ""
     #   self.log_cat_A = ""

        # Slugging Analysis Actions
#        self.countSluggingParameters(brokeLog.strSYSTEM_LOG,brokeLog.strEVENT_LOG)
#        self.explore_CPU(brokeLog.strCPU_INFO)
#        self.explore_EVENT_LOG(brokeLog.strEVENT_LOG)
#        self.explore_SYSTEM_LOG(brokeLog.strSYSTEM_LOG)

    def memory(self, segmented_log):

        print("\n   Analyze Memory")
        print("-----------------\n")

        # Check DUMPSYS_MEMINFO
        vet_stringAux = segmented_log.strDUMPSYS_MEMINFO.splitlines()
        processes = ""
        data_memory = ""
        cond_copy = True
        report_memory = ""

        for line in vet_stringAux:

            # Get Total_PSS_process
            if (line.find("K:")!=-1) and cond_copy:
                processes = processes + line + "\n"
            if (line.find("Total PSS by OOM adjustment") != -1):
                cond_copy = False
            if (line.find("Total RAM:")!=-1) or (line.find("Free RAM:")!=-1) or (line.find("Used RAM:")!=-1) or (line.find("Lost RAM:")!=-1):
                data_memory = data_memory + line + "\n"

        report_memory = report_memory + "# Memory data\n"
        report_memory = report_memory + data_memory
        report_memory = report_memory + "\n# Memory consumption per process\n"
        report_memory = report_memory + processes

        #print(report_memory)


        # Check PROCSTATS
        #vet_stringAux = segmented_log.strDUMPSYS_PROCSTATS.splitlines()

        #for line in vet_stringAux:
        #    print(line)


# -----------------------------------------------------------------------------------------------------------
#            print(line)

#            STR_AUX = line
#            STR_Total_PSS_process = STR_AUX[:STR_AUX.find('K')]

            # Get process
#            STR_AUX = STR_AUX[STR_AUX.find('K')+2:]
#            STR_process = STR_AUX[:STR_AUX.find('(')]

            # Get PID process
#            STR_AUX = STR_AUX[STR_AUX.find('pid')+3:]
#            STR_PID = STR_AUX[:STR_AUX.find(')')]

#            print(STR_Total_PSS_process)
#            print(STR_process)
#            print(STR_PID)

#            tuple = (STR_PID, STR_process, STR_Total_PSS_process)
#            list_Total_PSS_process.append(tuple)

#        for item in list_Total_PSS_process:
#            print(item[0] + " - " + item[1] + " - ")

#        print(processes)

        # Check MEMORY INFO
#        print("# MEMORY INFO")
#        vet_stringAux = segmented_log.strMEMORY_INFO.splitlines()
#        for line in vet_stringAux:
#            if (line.find("MemTotal")!=-1) or (line.find("MemFree")!=-1) or (line.find("MemAvailable")!=-1):
#                print(" " + line)

#        for item in list_Total_PSS_process:
#            print(item[0] + " " + item[1])
# -----------------------------------------------------------------------------------------------------------



    def cpu(self, segmented_log):
        print("\n   Analyze CPU")
        print("-----------------\n")

        print(segmented_log.strCPU_INFO)




    def temperature(self, segmented_log):
        print("Analyze Temperature")

    def package_installation(self, segmented_log):

        print("Analyze Package Installation")

    def wifi(self, segmented_log):
        print("Analyze Wifi")

    def inputSystem(self, segmented_log):
        print("Input System")
        stringAux = segmented_log.strSYSTEM_LOG.splitlines()

    def screen(self, segmented_log):
        print("Screen")


    def SYSTEM_LOG(self, segmented_log):

        stringAux = segmented_log.strSYSTEM_LOG.splitlines()


        for line in stringAux:

            # Input System
            if line.find('InputDispatcher: Waiting') != -1:
                print("")

            # Screen
            if line.find('screen_toggle') != -1:
                print("")






    def analyze_EVENT_LOG(self, log_segmenting):

        list_am_activity_launch_time = list()

        for item in log_segmenting.listEVENT_LOG:

#            if item[9] == "am_activity_launch_time":
#                print(item[9])
#                print(item[10])
#                list_am_activity_launch_time.append(item)

            if item[9] == "am_crash":
                print(item[8])
                print(item[9])
                print(item[10])


#            print(item[9])


#    def explore_CPU(self, CPU_LOG):
#        print(" Method: explore_CPU")
#        vet_CPU_LOG = CPU_LOG.splitlines()#

#        # 800%cpu  95%user   0%nice 102%sys 598%idle   0%iow   0%irq   5%sirq   0%host
#        pattern = "\d+%cpu"

#        for line in vet_CPU_LOG:
#            str_reset_info = re.search(pattern, line)
#            if str_reset_info is not None:
#                print(line)
#                break

        # try:
        #     for line in vet_CPU_LOG:
        #         str_reset_info = re.search(pattern, line)
        #         if str_reset_info is not None:
        #             print(line)
        #             break
        #
        # except:
        #     print("TRETA")


#    def countSluggingParameters(self, SYSTEM_LOG,EVENT_LOG):
#       vet_SYSTEM_LOG = SYSTEM_LOG.splitlines()
#        vet_EVENT_LOG = EVENT_LOG.splitlines()

#        print("SYSTEM LOG")

#        lmk = 0
#        strlmk = ""
##        gc = 0
 #       strgc = ""

 #       for line in vet_SYSTEM_LOG:

 #           if (line.find('lowmemorykiller') != -1):
 #               strlmk = strlmk + line + "\n"
 #               lmk = lmk + 1

 #           if (line.find('GC freed') != -1):
  #              strgc = strgc + line + "\n"
   #             gc = gc + 1


    #    print("EVENT LOG")
     #   i = 0
     #   for line in vet_EVENT_LOG:
     #       if (line.find('lowmemorykiller') != -1):
     #           i = i + 1


#        self.lines_garbage_collector = strgc
#        self.counter_garbage_collector = gc
#        self.lines_low_memory_killer = strlmk
#        self.counter_low_memory_killer = lmk


