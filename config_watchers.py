import string
# Number of watchers used for cookie_maker and cookie_sender
WATCHERS = 3
WATCH_DIR = 'D:\\db-filler\\generated_scripts\\OUTPUT_results\\' #folder to watch
#todo: change WATCH_DIR to 'D:\\cookie\\OUTPUT_results\\' #folder to watch

class Watchers():
    """
        Make object with key value (e.g. r:0:b66) and key actions (e.g.bet66, raise172, call, check, fold)
        """
    def __init__(self):
        self.number = WATCHERS
        self.dir = WATCH_DIR
        subfolders = [string.ascii_lowercase[i] for i in self.number]
        for subfolder in subfolders:
            self.paths = self.dir + subfolder
