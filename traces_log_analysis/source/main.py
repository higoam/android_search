import sys

from controller.AnalyzeThreadStack import AnalyzeThreadStack
from model.Thread import Thread
from model.Process import Process


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def main():

    logReadText = read_log()



    threadStackData = AnalyzeThreadStack(logReadText)

#    threadStackData.createThreadSummary()
#    threadStackData.printThreadSummary()
#    threadStackData.analyzeResources()
#    threadStackData.pritThreadsProblem()


    print("FIM")
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def read_log():

    # Get Parameter
    strDump = sys.argv[1]

    # Open File Log
    file = open(strDump,"r")
    logReadText = file.read()
    file.close()

    return logReadText

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
main()
