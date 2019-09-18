import sys

from controller.breakLog import breakLog
from model.Thread import Thread
from model.process import process

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def main():

    #Auxiliar
    breakingLog = breakLog()

    listProcess = list()



    # Ler Log
    logReadText = read_log()

    # Quebra Log
    listProcess = breakingLog.createList(logReadText)

    print(len(listProcess))

    for item in listProcess:
        print(item.headProc)



    # Analisa e Imprime Log


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
