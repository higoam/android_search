

class Thread:

    def __init__(self, threadText):

        self.threadText = threadText

        #Line 0
        self.firstLine = ""         #
        self.threadName = ""        #
        self.prio = ""              #
        self.tid = ""               #
        self.threadStatus = ""      #

        #Line 1
        self.group = ""             #
        self.sCount = ""            #
        self.dsCount = ""           #
        self.obj = ""               #
        self.self = ""              #

        #Line 2
        self.sysTid = ""            #
        self.nice = ""              #
        self.cgrp = ""              #
        self.sched = ""             #

        #Line 3
        self.state = ""             #
        self.schedstat = ""         #
        self.utm = ""               #
        self.stm =""                #
        self.core = ""              #
        self.hz = ""                #

        #Line 4                     #
        self.stack = ""             #
        self.stacksize = ""         #

        #Line 5
        self.mutexex = ""           #

        #Others Line
        self.threadActivities = ""              #
        self.listWaitingTotal = list()          #
        self.listLockedTotal = list()           #
        self.listSleepingTotal = list()         #
        self.listWaitingUnknownObject = list()  #
        self.listDependente = list()

        self.gettingThreadInformation()



    # -------------------------------------------------------------------------------
    # Coletar dados do Cabecalho da Thread e popular atributos
    def gettingThreadInformation(self):

        getThreadActivities = False

        stringAUX = ""
        for line in self.threadText.splitlines():

            # Thread Activities -- --------------------------------------->
            if (getThreadActivities == True):
                self.threadActivities = self.threadActivities + line + "\n"



            # Line 0 ---------------------------------------------------->
            if (line.find('prio=') != -1):
                stringAUX = line

                self.firstLine = line
                # Get Thread Name
                self.threadName = stringAUX[1:stringAUX.find('\"',1)]

                if (stringAUX.find('(not attached)') != -1):

                    self.tid = "!"
                    self.threadStatus = "!"
                else:

                    # Get Prio
                    self.prio = stringAUX[ stringAUX.find('prio=')+5: stringAUX.find('tid=')]

                    # Get Prio
                    strAUX = stringAUX[ stringAUX.find('tid=')+4:]
                    self.tid = strAUX[:strAUX.find(" ")]

                    # Get Status Thread
                    self.threadStatus = strAUX[strAUX.find(" ")+1:]

            # Line 1 ---------------------------------------------------->
            if (line.find('group=') != -1):
                stringAUX = line

            # Line 2 ---------------------------------------------------->
            if (line.find('sysTid=') != -1):
                stringAUX = line

                if (line.find('nice=') != -1):
                    self.sysTid = stringAUX[line.find('sysTid=') +7: line.find('nice=')-1]
                else:
                    self.sysTid = stringAUX[line.find('sysTid=') +7:]

            #Line 3
            if (line.find('state=') != -1):
                stringAUX = line

            # Line 4
            if (line.find('stack=') != -1):
                stringAUX = line

            # Line 5
            if (line.find('mutexes=') != -1):

                stringAUX = line

                getThreadActivities = True
                stringAUX = ""




