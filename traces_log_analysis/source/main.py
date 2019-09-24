import sys

from controller.AnalyzeThreadStack import AnalyzeThreadStack
from model.Thread import Thread
from model.Process import Process


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def main():

    logReadText = read_log()
    threadStackData = AnalyzeThreadStack(logReadText)

#   threadStackData.printThreads()
    threadStackData.printResume()

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
