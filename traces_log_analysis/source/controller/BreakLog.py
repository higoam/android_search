
from model.Thread import Thread
from model.Process import Process

class BreakLog:

    def __init__(self):
        self.list = list()

    def createListProcess(self, logRead):

        print("TESTE3")

        processAUX = ""
        listProcessText = list()
        listProcess = list()

        vet_log = logRead.splitlines(True)


        for line in vet_log:
            processAUX = processAUX + line

            if (line.find('----- end') != -1):

                # Adicionar a Lista
                listProcessText.append(processAUX)
                listProcess.append(self.createProc(processAUX))
                # Zerar processAUX
                processAUX = ""

#        self.createProc(listProcessText[2])

        return listProcess


    def createProc(self, processText):

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

        #self.createThread(listThreadText[1])








