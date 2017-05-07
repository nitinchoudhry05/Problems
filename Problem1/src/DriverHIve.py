'''
Created on 05-May-2017

@author: nitinchoudhry
'''

import sys
sys.path.append("../")
from Resources.Cleaner import *
from Hive.HiveExecutor import *

class Driver(object):
    
    def __init__(self):
        
        #try:
            self.Hive=HiveExecutor()
            self.Cleaner=Cleaner("HiveLogs")
            self.Run()
            
        #except Exception,e:
            #print "Exception Encountered while initiating the Driver"
            #print str(e)
    
    def Run(self):
        print "Please Check Output Folder to Check Running Hive Commands "
        self.Hive.Run()
                
    
    
    
        
            
        


if __name__ == '__main__':
    
    #try:
        driver=Driver()
        #Driver.Run()        
    #except Exception ,e:
        #print "Exception Encountered While Running The Driver" 
        #print e
               

        
        
        
