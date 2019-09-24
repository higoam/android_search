
from model.Thread import Thread
from model.Process import Process
from controller.BreakLog import BreakLog

class AnalyzeThreadStack:

    def __init__(self, readLog):

        self.readLog = readLog
        self.traces = ""
        self.resumeLog = ""
        self.listProcess = list()

        self.breakingLog()
        self.analyzeAll()

# -----------------------------------------------------------------
# Referente a analise
# -----------------------------------------------------------------

    # -------------------------------------------------------------------------------
    # Chama a analise de cada processo
    def analyzeAll(self):

        for process in self.listProcess:
            self.analysisProcess(process)


    # -------------------------------------------------------------------------------
    # Analisa threads por processo
    def analysisProcess(self, processData):

        # Varre as threads ---------------------------------------------------->
        for thread in processData.listThreads:

            # Cria um resumo do log ---------------------------------------------------->
            if (thread.threadStatus == "Blocked") or \
                    (thread.threadStatus == "Waiting") or \
                    (thread.threadStatus == "TimedWaiting") or \
                    (thread.threadStatus == "Sleeping"):

                self.resumeLog = self.resumeLog + "\n"
                self.resumeLog = self.resumeLog + thread.firstLine + "\n"

            for line in thread.threadActivities.splitlines():
                if (line.find('  - ') != -1):
                    self.resumeLog = self.resumeLog + line + "\n"

#            for line in thread.listWaiting:
#                print(line)

#            for line in thread.listLocked:
#                print(line)


#            print(self.resumeLog)



    def analyzeActivities(self):

        for line in self.threadActivities.splitlines():
            stringAUX = line
            if (line.find('  - waiting on ') != -1):
#                print("waiting")
#                print(stringAUX[stringAUX.find('<') + 1: stringAUX.find('>') - 1])
                self.listWaiting.append(stringAUX[stringAUX.find('<') + 1: stringAUX.find('>') - 1])

            if (line.find('  - locked ') != -1):
#                print("locked")
#                print(stringAUX[stringAUX.find('<') + 1: stringAUX.find('>') - 1])
                self.listLocked.append(stringAUX[stringAUX.find('<') + 1: stringAUX.find('>') - 1])


# -----------------------------------------------------------------
# Referente a impressao
# -----------------------------------------------------------------

    def printThreads(self):

        for proc in self.listProcess:

            for thread in proc.listThreads:
                print(thread.threadName)


    def printResume(self):
        print(self.resumeLog)


#-----------------------------------------------------------------
# Referente a quebra do Log
#-----------------------------------------------------------------

    # -------------------------------------------------------------------------------
    # Quebra Log
    def breakingLog(self):

        # Verificar se eh um dumpstate
        if (self.readLog.find('dumpstate') != -1):
            self.traces = self.extractTraceFromDump().splitlines(True)
        else:
            self.traces = self.readLog.splitlines(True)

        self.createListProcess()


    # -------------------------------------------------------------------------------
    # Quebra Log DUMP - ARRUMAR
    def extractTraceFromDump(self, threadStackText):
        return threadStackText


    # -------------------------------------------------------------------------------
    # Cria Lista de Processos
    def createListProcess(self):

        proc = Process()
        processAUX = ""

        vet_log = self.traces

        for line in vet_log:
            processAUX = processAUX + line

            if (line.find('----- end') != -1):

                # Adicionar a Lista
                proc = self.createProcess(processAUX)
                self.listProcess.append(proc)
                # Zerar processAUX
                processAUX = ""

    # -------------------------------------------------------------------------------
    # Cria Processos
    def createProcess(self, processText):


        listThread = list()
        listThreadText = list()

        processNode = Process()

        firstThread = True
        creatingThread = False
        threadAUX = ""
        stringAUX = ""

        vet_proc = processText.splitlines()

        for item in vet_proc:

            # Cabecalho do Processo
            if (item.find('prio=') != -1) and firstThread:
                firstThread = False
                processNode.headProc = stringAUX
                stringAUX = ""

            # Threads do Processo
            if (item.find('prio=') != -1) and (not firstThread):

                listThreadText.append(stringAUX)

                threadNode = Thread(stringAUX)
                listThread.append(threadNode)

                stringAUX = ""

            stringAUX = stringAUX + item + "\n"

        # Add last thread of file
        listThreadText.append(stringAUX)
        threadNode = Thread(stringAUX)
        listThread.append(threadNode)

        processNode.listThreads = listThread

        return processNode


    # -------------------------------------------------------------------------------