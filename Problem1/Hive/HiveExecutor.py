'''
Created on 05-May-2017
@author: nitinchoudhry
'''
import sys
sys.path.append("../")
from Resources.Logger import *
import pyhs2


class HiveExecutor(object):
    
    
    def __init__(self,hiveserver="localhost",port="10000",user="hadoop",paswword="",dbname="xebia",QueryFile="../Configs/HiveQueries"):
        
        self.QueryFile=open(QueryFile,"r")
        self.hiveServer = hiveserver
        self.port = port
        self.user = user
        self.password = paswword
        self.dbname = dbname
        Connection=pyhs2.connect(host=self.hiveServer,
                                  port=self.port,
                                  authMechanism="PLAIN",
                                  user=self.user,
                                  password=self.password,
                                  database=self.dbname)
        self.Cursor=Connection.cursor()
        
        
        
    
    def Run(self):
        
        logs("../Output/HiveLogs")
        self.logger=Initiate_logger("HiveLogs")
        Lines=self.QueryFile.readlines()
        try:
            for line in Lines:
                self.RunHiveCommand(line.strip("\n"))
        
            self.Cursor.close()
        except Exception,e:
            self.logger.error("Exception Encountered while Running Hive Queries")
            self.logger.error("Exception:"+str(e))
        
    def RunHiveCommand(self,Query):
        
        self.logger.info("Executing Query :"+Query)
        
        
        try:
            self.Cursor.execute(Query)
            self.logger.info("#######################Result#################")
            Result=""
            for i in self.Cursor.fetch():
                Result+= i+"\n"
        
                             
            self.logger.info(Result)
            
        except Exception,e:
            self.logger.error("Failure While Execution of Query")
            self.logger.error(str(e))
            
        
        
        
            
    
    
        
        