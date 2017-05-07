'''
Created on 05-May-2017

@author: nitinchoudhry
'''

import sys
sys.path.append("../")
from Resources import Cleaner
from Hive import HiveExecutor

class Driver(object):
    
    def __init__(self):
        
        try:
            self.Hive=HiveExecutor()
            self.Cleaner=Cleaner("HiveLogs")
            self.Run()
            
        except Exception,e:
            print "Exception Encountered while initiating the Driver"
            print str(e)
    
    def Run(self):
        print "Please Check Output Folder to Check Running Hive Commands "
        self.Hive.Run()
        Lines=self.ConfigFile.readlines()
                
    
    
    
        
            
        


if __name__ == '__main__':
    
    try:
        Driver=Driver()
        #Driver.Run()        
    except Exception ,e:
        print "Exception Encountered While Running The Driver" 
        print e
               

        
        
        