
from model.Thread import Thread
from model.Process import Process
from controller.Grafo import Grafo

class AnalyzeThreadStack:

    def __init__(self, readLog):

        self.readLog = readLog
        self.traces = ""
        self.resumeLog = ""
        self.listProcess = list()

        self.extractInformation()   # Obter dados do Log Traces

        self.grafo = Grafo()
        self.listTuple = list()

# -----------------------------------------------------------------
# -----------------------------------------------------------------
# ************** Referente a quebra dos Logs, *********************
# ************ organizacao e armazenamento dos dados **************
# -----------------------------------------------------------------
# -----------------------------------------------------------------


    # -------------------------------------------------------------------------------
    # Pagar dados e Organizar na Estrutura
    def extractInformation(self):

        strAUX = ""

        for line in self.readLog.splitlines():

            strAUX = strAUX + line + "\n"

            if (line.find('- end') != -1):

                newProcess = Process()
                newProcess.processText = strAUX
                firstThread = True
                strAUX2 = ""

                for line2 in newProcess.processText.splitlines():

                    if (line2.find('----- pid') != -1):
                        newProcess.pid = line2[line2.find('pid') + 4: line2.find('at') -1]

                    if (line2.find('Cmd line:') != -1):
                        newProcess.name = line2[line2.find('Cmd line:') + 10:]

                    if (line2[0:1] == "\""):
                        if firstThread:
                            firstThread = False
                            newProcess.headProc = strAUX2
                            strAUX2 = ""
                        else:
                            newThread = Thread(strAUX2)
                            newProcess.listThreads.append(newThread)
                            strAUX2 = ""
                    strAUX2 = strAUX2 + line2 + "\n"

                newThread = Thread(strAUX2)
                newProcess.listThreads.append(newThread)
                strAUX2 = ""

                self.listProcess.append(newProcess)
                strAUX = ""

#        for process in self.listProcess:
##            print "**** PROCESSO"
#            print process.name
#            print process.pid

    # -------------------------------------------------------------------------------
    # Cria Lista de Processos
    def segmentLogByProcess(self):

        newProcess = Process()
        processAUX = ""
        vet_log = self.readLog.splitlines()

        copyingProcess = False
        copyingThread = False
        copyingHead = False
        firstThread = True

        for line in vet_log.splitlines():

            if (line.find('prio=') != -1):
                if firstThread:
                    newProcess.headProc = processAUX
                    firstThread = False
                    processAUX = ""
                else:
                    newThread = Thread(processAUX)
                    newProcess.listThreads.append(newThread)
                    stringAUX = ""


            processAUX = processAUX + line + "\n"

                                    # Encontrou final da ultima threa (n), ira salvar ultima thread (n)


#            elif (line.find('prio=') != -1) and (not firstThread):  # Encontrou segunda (2) ou threads seguintes (i+1), ira salvar thread (i-1)
#                print("$$$$$$$$$$$$$ Imprimindo Thread")
#                print(newProcess.headProc)

#            if (line.find('----- end') != -1):                    # Encontrou final da ultima threa (n), ira salvar ultima thread (n)
#                newThread = Thread(processAUX)
#                newProcess.listThreads.append(newThread)
#                self.listProcess.append(newProcess)                 # Salva processo e atualiza variavel controle firstThread, ira comecar um novo processo
#                del newProcess.listThreads
#                stringAUX = ""
#                firstThread = True


    # -------------------------------------------------------------------------------
    # Organizar dados de processos e threads
    def organizeProcessThreadData(self):

        for process in self.listProcess:

            getHeadProcess = True
            stringAUX = ""

            for line in process.processText:

                if (line.find('prio=') != -1) and getHeadProcess:
                    getHeadProcess = False
                    process.headProc = stringAUX
                    stringAUX = ""

                if ((line.find('prio=') != -1) and not getHeadProcess):
                    newThread = Thread(stringAUX)
                    process.listThreads.append(newThread)
                    stringAUX = ""

                stringAUX = stringAUX + line + "\n"




# -----------------------------------------------------------------
# -----------------------------------------------------------------
# ********* Referente a analise dos dados obtidos *****************
# -----------------------------------------------------------------
# -----------------------------------------------------------------

    # -------------------------------------------------------------------------------
    # Criar um resumo do LOG
    def createThreadSummary(self):

        backupLine = ""

        for process in self.listProcess:

            self.resumeLog = self.resumeLog + "######################################" + "\n"
            self.resumeLog = self.resumeLog + "# Process: " + process.name + "\n"
            self.resumeLog = self.resumeLog + "# pid: " + process.pid + "\n"
            self.resumeLog = self.resumeLog + "######################################" + "\n\n"

            for thread in process.listThreads:

                for line in thread.threadActivities.splitlines():
                    if (line.find('  - ') != -1):
                        backupLine  = backupLine + line + "\n"

                if backupLine != "":
                    self.resumeLog = self.resumeLog + thread.firstLine + "\n"
                    self.resumeLog = self.resumeLog + backupLine + "\n"
                    backupLine = ""

    # -------------------------------------------------------------------------------
    # Identificar Threads esperando por recursos e threads que possuem o recurso
    def analyzeResources(self):

        for process in self.listProcess:

            listOfTupleResourceLocked = list()
            listTemp = list()

            searchResource = False
#            print("\n\n**************************************")
#            print("      Analisando Processo")
#            print("**************************************")

            for thread in process.listThreads:

                # Identifica, e Lista com recursos (waiting - waiting unknown - locked - sleeping - Untreated Line)
                for line in thread.threadActivities.splitlines():

                    if line.find('- waiting') != -1:
                        if line.find('unknown') != -1:
                            thread.listWaitingUnknownObject.append(line)
                        else:
                            thread.listWaitingTotal.append(line[line.find('<') + 1: line.find('>')])
                    elif line.find('- locked') != -1:
                        thread.listLockedTotal.append(line[line.find('<') + 1: line.find('>') ])
                        tupleLocked = (thread.sysTid,line[line.find('<') + 1: line.find('>') ])
                        listOfTupleResourceLocked.append(tupleLocked)
                    elif line.find(' - sleeping') != -1:
                        thread.listSleepingTotal.append(line[line.find('<') + 1: line.find('>')])
                    elif line.find(' - ') != -1 :
                        print("Untreated Line")


                # Identifica threads com recursos Waiting
                for elem in thread.listWaitingTotal:
                    if not thread.listLockedTotal.count(elem):
                        my_tuple = (thread.sysTid,elem)
                        listTemp.append(my_tuple)
#                        print "  ",my_tuple[0], my_tuple[1],"\n"

                # Identifica threads com recursos Waiting
                for elem in thread.listSleepingTotal:
                    if not thread.listLockedTotal.count(elem):
                        my_tuple = (thread.sysTid,elem)
                        listTemp.append(my_tuple)
#                       print "  ",my_tuple[0], my_tuple[1],"\n"

            if(listTemp):

                # Recursos em Espera
                for resourceWaiting in listTemp:

                    resourceNotFind = True

                    # Procurando nos Recursos Bloqueados
                    for resourceLock in listOfTupleResourceLocked:

                        if resourceWaiting[1] == resourceLock[1]:
                            tupleDefinitive = (resourceWaiting[0], resourceWaiting[1],resourceLock[0])
                            process.listTupleResource.append(tupleDefinitive)
                            resourceNotFind = False

                    if resourceNotFind:
                        tupleDefinitive = (resourceWaiting[0], resourceWaiting[1], "unknown")
                        process.listTupleResource.append(tupleDefinitive)
                        resourceNotFind = True



# -----------------------------------------------------------------
# -----------------------------------------------------------------
# ******************** Referente a impressao **********************
# -----------------------------------------------------------------
# -----------------------------------------------------------------

    def printThreads(self):

        for proc in self.listProcess:

            for thread in proc.listThreads:
                print(thread.threadName)



    def printThreadSummary(self):
        print(self.resumeLog)



    def pritThreadsProblem(self):

        print("\n\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
        print("*** Threads em Espera - Resumo")
        print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")

        for process in self.listProcess:

            if(process.listTupleResource):

                print "\n   Process:", process.name, " - ", process.pid
                print "   __________________________________________________________"
                print "     Wating Thread", "|        Resource     " , "|   Locked Thread   "
                print "   __________________________________________________________"

                for item in process.listTupleResource:
                    print "         ",item[0], "    |     " , item[1], "    |    ", item[2]

        print("\n\n\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
        print("*** Threads em Espera")
        print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")

        for process in self.listProcess:

            if(process.listTupleResource):

                print "\n   Process:", process.name, " - ", process.pid

                for item in process.listTupleResource:

                    # Busca e Imprime a Thread em Espera
                    for thread in process.listThreads:
                        if item[0] == thread.sysTid:
                            print thread.threadText

                    # Verifica se tem registros da thread que segura o recurso
                    if item[2] == "unknown":
                        "Thread Desconhecida"
                    else:
                        for thread in process.listThreads:
                            if item[2] == thread.sysTid:
                                print thread.threadText




