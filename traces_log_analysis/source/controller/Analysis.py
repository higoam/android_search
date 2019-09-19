
from model.Thread import Thread
from model.process import process

class Analysis:

    def analysisProcess(self, processData):

        for thread in processData.listThreads:

#            print(thread.threadName)

            if thread.threadStatus == "\sgsrdgrdg":
                print("")