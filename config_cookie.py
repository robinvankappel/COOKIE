import string
import os

"""DEFINITION FOR COOKIE SOLVING"""
#DEFINITION OF WATCHERS
WATCHERS = 3 # Number of watchers used for cookie_maker and cookie_sender
WATCH_DIR = 'D:\\cookie\\cookies\\' #folder to watch
#LOCATION OF TREES
FLOP_DIR = 'E:\\60bb_dreamconfig\\'
PROCESSED_FLOPS_DIR = 'E:\\60bb_dreamconfig\\processed_flops\\' #location where trees are moved to after processing
MOVE_PROCESSED_FLOPS = True  # move the flops which have been handled to PROCESSED_FLOPS_DIR
#LOCATION OF PIO
PIO_DIR = 'C:\\PioSOLVER-edge\\'
PIO_NAME = 'PioSOLVER-edge19.exe'


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
