

class Thread:

    def __init__(self, threadText):

        self.threadText = threadText

        #Line 0
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
        self.threadActivities = ""  #

        self.gettingThreadInformation()

    def gettingThreadInformation(self):

        stringAUX = ""
        for line in self.threadText.splitlines():

            if (line.find('prio=') != -1):
                stringAUX = line
                self.threadName = stringAUX[1:stringAUX.find('\"',1)]
                if (stringAUX.find('(not attached)') != -1):
                    print("Falta Tratar esse caso, pegar o prio")
                    print(stringAUX)
                else:

#                    print(stringAUX.find('prio='))
#                    print(stringAUX.find('tid='))
                    self.prio = stringAUX[ stringAUX.find('prio=')+5: stringAUX.find('tid=')]
                    self.tid = ""  #
                    self.threadStatus = ""  #

            if (line.find('group=') != -1):
                stringAUX = line

            if (line.find('sysTid=') != -1):
                stringAUX = line

            if (line.find('state=') != -1):
                stringAUX = line


        print(self.threadName)
        print(self.prio)










