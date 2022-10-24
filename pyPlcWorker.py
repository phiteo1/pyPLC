# Worker for the pyPLC
#
# Tested on Windows10 with python 3.9
#

#------------------------------------------------------------
import pyPlcHomeplug

class pyPlcWorker():
    def __init__(self, callbackAddToTrace=None, callbackShowStatus=None):
        print("initializing pyPlcWorker") 
        self.nMainFunctionCalls=0
        self.strUserAction = ""
        self.callbackAddToTrace = callbackAddToTrace
        self.callbackShowStatus = callbackShowStatus
        self.hp = pyPlcHomeplug.pyPlcHomeplug(self.callbackAddToTrace, self.callbackShowStatus)
 
    def addToTrace(self, s):
        self.callbackAddToTrace(s)
        
    def showStatus(self, s, selection = ""):
        self.callbackShowStatus(s, selection)        
        
    def mainfunction(self):
        self.nMainFunctionCalls+=1
        #self.showStatus("pyPlcWorker loop " + str(self.nMainFunctionCalls))
        self.hp.mainfunction() # call the lower-level worker
        
    def handleUserAction(self, strAction):
        self.strUserAction = strAction
        if (strAction == "P"):
            self.hp.enterPevMode()
        if (strAction == "E"):
            self.hp.enterEvseMode()
        if (strAction == "L"):
            self.hp.enterListenMode()  
        # self.addToTrace("UserAction " + strAction)
        self.hp.sendTestFrame(strAction)

