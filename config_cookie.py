import string
import os
COOKIE_DIR = 'D:\\cookie\\'

"""INPUT PARAMETERS FOR COOKIE SOLVING"""
#DEFINITION OF WATCHERS
WATCHERS = 10 # Number of watchers used for cookie_maker and cookie_sender
#LOCATION OF TREES
FLOP_DIR = 'E:\\dreamconfigs\\'
PROCESSED_FLOPS_DIR = 'E:\\dreamconfigs\\processed_flops\\' #location where trees are moved to after processing
MOVE_PROCESSED_FLOPS = True  # move the flops which have been handled to PROCESSED_FLOPS_DIR
#LOCATION OF PIO
PIO_DIR = 'C:\\PioSOLVER-pro\\'
PIO_NAME = 'PioSOLVER-pro19.exe'
#LOG FILE
LOG_NAME = 'dev_machine.log'

"""DERIVED PARAMETERS"""
WATCH_DIR = os.path.join(COOKIE_DIR,'cookies\\') #folder to watch
LOG_FILE = os.path.join(COOKIE_DIR,'Dropbox','CM_logs',LOG_NAME) #folder to watch

#Class which defines all info about which folders are being used and watched
class Watchers():
    """
        Make object with key value (e.g. r:0:b66) and key actions (e.g.bet66, raise172, call, check, fold)
        """
    def __init__(self,watchers,watch_dir):
        self.number = watchers
        self.dir = watch_dir
        subfolders = [string.ascii_uppercase[i] for i in xrange(self.number)]
        self.paths = list()
        for subfolder in subfolders:
            if not os.path.exists(self.dir + subfolder):
                os.makedirs(self.dir + subfolder)
            self.paths.append(self.dir + subfolder)
