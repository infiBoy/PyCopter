# FileName : CopterThreadPool.py
# Date : 13.11.2013
# Developers : Maxim Arav

class CopterThreadPool():
    def __init__(self):
        self.threads = []
    def addThread(self, thread):
        self.threads.append(thread)
    def waitForThreadsToFinish(self):
        for th in self.threads:
            th.join()
    def closeAllThreads(self):
        for th in self.threads:
            th.terminate()
