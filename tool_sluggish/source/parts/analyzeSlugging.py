

import re
from logging import exception

from breakLog import breakLog

class analyzeSlugging:

    def __init__(self, brokeLog):

        # Useful info for sluggin analysis
        self.counter_garbage_collector = ""
        self.lines_garbage_collector = ""
        self.counter_low_memory_killer = ""
        self.lines_low_memory_killer = ""

        self.log_cat_V = ""
        self.log_cat_D = ""
        self.log_cat_I = ""
        self.log_cat_W = ""
        self.log_cat_E = ""
        self.log_cat_A = ""

        # Slugging Analysis Actions
#        self.countSluggingParameters(brokeLog.strSYSTEM_LOG,brokeLog.strEVENT_LOG)
#        self.explore_CPU(brokeLog.strCPU_INFO)
        self.explore_EVENT_LOG(brokeLog.strEVENT_LOG)
#        self.explore_SYSTEM_LOG(brokeLog.strSYSTEM_LOG)

    def explore_CPU(self, CPU_LOG):
        print(" Method: explore_CPU")
        vet_CPU_LOG = CPU_LOG.splitlines()

        # 800%cpu  95%user   0%nice 102%sys 598%idle   0%iow   0%irq   5%sirq   0%host
        pattern = "\d+%cpu"

        for line in vet_CPU_LOG:
            str_reset_info = re.search(pattern, line)
            if str_reset_info is not None:
                print(line)
                break

        # try:
        #     for line in vet_CPU_LOG:
        #         str_reset_info = re.search(pattern, line)
        #         if str_reset_info is not None:
        #             print(line)
        #             break
        #
        # except:
        #     print("TRETA")

    def explore_SYSTEM_LOG(self, SYSTEM_LOG):
        print(" Method: explore_SYSTEM_LOG")
        vet_SYSTEM_LOG = SYSTEM_LOG.splitlines()

        list_event_types = list()
        i = 0

        for line in vet_SYSTEM_LOG:
            line_AUX = line[37:]
            line_AUX = line_AUX[:line_AUX.find(':')]

            if line_AUX not in list_event_types:
                list_event_types.append(line_AUX)

            i = i + 1

        list_event_types.sort()

        for x in list_event_types:
            print(x)

        print(i)



        # Separar por Tipos de Eventos = V,D,I,W,E,A
#        for line in vet_SYSTEM_LOG:
#            print(line)
#            line_AUX = line[37:38]
#            line_AUX = line_AUX[:line_AUX.find(':')]
#            print(line_AUX)
#            if line_AUX == "V":
#                self.log_cat_V = self.log_cat_V + line + "\n";
#            elif line_AUX =="D":
#                self.log_cat_D = self.log_cat_D + line + "\n";
#            elif line_AUX == "I":
#                self.log_cat_I = self.log_cat_I + line + "\n";
#            elif line_AUX == "W":
#                self.log_cat_W = self.log_cat_W + line + "\n";
#            elif line_AUX == "E":
#                self.log_cat_E = self.log_cat_E + line + "\n";
#            elif line_AUX == "A":
#                self.log_cat_A = self.log_cat_A + line + "\n";

#        print("I")
#        print(self.log_cat_I)
#        print("V")
#        print(self.log_cat_V)
#        print("D")
#        print(self.log_cat_D)

            # Orena Lista
#            list_event_types.sort()

            # Imprime Lista
#            for x in list_event_types:
#                print(x)


    def explore_EVENT_LOG(self, EVENT_LOG):
        print(" Method: explore_EVENT_LOG")
        vet_EVENT_LOG = EVENT_LOG.splitlines()

        list_event_types = list()
        line_AUX =  ""
        idexP = 0
        i = 0

        # Coleta Eventos
        for line in vet_EVENT_LOG:
            print(line)
            line_AUX = line[39:]
            line_AUX = line_AUX[:line_AUX.find(':')]

            if line_AUX not in list_event_types:
                list_event_types.append(line_AUX)

#            if line_AUX == "cpu":
#                print(line)
#            print(line_AUX)

            i = i + 1

        # Ordena Lista
        list_event_types.sort()

        # Imprime Lista
#        for x in list_event_types:
#            print(x)

        print(i)

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


