'''
Created on 06-May-2017

@author: nitinchoudhry
'''
import sys
sys.path.append("../")
from Resources import Cleaner
from Spark import  SparkExecutor

class Driver(object):
    
    def __init__(self):
        
        try:
            self.Spark=SparkExecutor()
            self.Cleaner=Cleaner("SparkLogs")
            self.Run()
        except Exception,e:
            print "Exception Encountered while initiating the Driver"
            print str(e)
    
    def Run(self):
        print "Please Check Output Folder to Check Running Spark Commands "
        self.Spark.Run()
        


if __name__ == '__main__':
    
    try:
        Driver=Driver()
        Driver.Run()        
    except Exception ,e:
        print "Exception Encountered While Running The Driver" 
        print e
               

        
        
