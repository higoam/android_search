

class Process:

    def __init__(self):

        self.processText = ""

        self.headProc = ""
        self.pid = ""               #
        self.name = ""              #
        self.date = ""              #
        self.otherdata = ""         #

        self.listThreads = list()                       #
        self.listThreadsWithUnknownObject = list()      #
        self.listThreadsWaitingResource = list()        #
        self.listTupleResource = list()

    def gettingProcessInformation(self):

        getThreadActivities = False

        stringAUX = ""
