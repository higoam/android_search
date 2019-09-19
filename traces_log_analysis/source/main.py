import sys

from controller.breakLog import breakLog
from controller.Analysis import Analysis
from model.Thread import Thread
from model.process import process


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def main():

    #Auxiliar
    breakingLog = breakLog()
    analyzing = Analysis()

    listProcess = list()



    # Ler Log
    logReadText = read_log()

    # Quebra Log
    processListData = breakingLog.createList(logReadText)

#    for item in processListData:
#        for item2 in item.listThreads:
#            print(item2.threadText)


    # Analisa e Imprime Log
    analyzing.analysisProcess(processListData[1])

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def read_log():

    # Get Parameter
    strDump = sys.argv[1]

    # Open File Log
    file = open(strDump,"rb")
    logReadText = file.read()
    file.close()



    print("Leu Arquivo")
    return str(logReadText)




# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
main()
