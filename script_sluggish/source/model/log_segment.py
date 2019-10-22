

class log_segment:

    def __init__(self, read_log):

        # Strings to store sections
        self.strREAD_LOG = read_log
        self.strBUGREPORT = ""

        self.strHEADER_LOG = ""

        self.strPPOCESSES_AND_THREADS = ""
        self.strEVENT_LOG = ""
        self.strSYSTEM_LOG = ""
        self.strSYSTEM_PROPERTIES = ""

        self.strMEMORY_INFO = ""
        self.strDUMPSYS_MEMINFO = ""
        self.strDUMPSYS_PROCSTATS = ""

        self.strCPU_INFO = ""
        self.strCPU_INFO_2 = ""

        self.listEVENT_LOG = ""

