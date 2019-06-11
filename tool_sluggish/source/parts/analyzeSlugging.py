
from breakLog import breakLog

class analyzeSlugging:

    def __init__(self, brokeLog):

        # Useful info for sluggin analysis
        self.counter_garbage_collector
        self.lines_garbage_collector
        self.counter_low_memory_killer
        self.lines_low_memory_killer

        # Slugging Analysis Actions
        self.countSluggingParameters(brokeLog.strSYSTEM_LOG,brokeLog.strEVENT_LOG)




    def explore_CPU(self, CPU_LOG):
        vet_CPU_LOG = CPU_LOG.splitlines()




    def countSluggingParameters(self, SYSTEM_LOG,EVENT_LOG):
        vet_SYSTEM_LOG = SYSTEM_LOG.splitlines()
        vet_EVENT_LOG = EVENT_LOG.splitlines()

        print("SYSTEM LOG")

        lmk = 0
        strlmk = ""
        gc = 0
        strgc = ""

        for line in vet_SYSTEM_LOG:

            if (line.find('lowmemorykiller') != -1):
                strlmk = strlmk + line + "\n"
                lmk = lmk + 1

            if (line.find('GC freed') != -1):
                strgc = strgc + line + "\n"
                gc = gc + 1


        print("EVENT LOG")
        i = 0
        for line in vet_EVENT_LOG:
            if (line.find('lowmemorykiller') != -1):
                i = i + 1


        self.lines_garbage_collector = strgc
        self.counter_garbage_collector = gc
        self.lines_low_memory_killer = strlmk
        self.counter_low_memory_killer = lmk


