'''
Created on 05-May-2017

@author: nitinchoudhry
'''
from pyspark.sql import SparkSession
from Resources.Logger import *
from pyspark import SQLContext

class SparkSqlExecutor():
    
    def __init__(self,SrcFile="../Configs/aadhar_data.csv",QueryFile="../Configs/SparkSqlQueries",tablename="Test"):
    
        self.QueryFile=QueryFile
        self.SrcFile=SrcFile
        self.spark=SparkSession.builder.appName("Python Spark SQL basic example").config("spark.some.config.option", "some-value") .getOrCreate()
        self.table=tablename
        self.sequelcontext=SQLContext(self.spark)
    
    
    def Run(self):
        
        logs("../Output/SparkSqlLogs")
        self.logger=Initiate_logger("SparkSqlLogs")
        Lines=self.QueryFile.readlines()
        
        df=self.sequelcontext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true').load(self.SrcFile)
        df.createOrReplaceTempView("TestTable")
        try:
            for line in Lines:
                self.RunSparkSqlCommand(line.strip("\n").strip(","))
        
        except Exception,e:
            self.logger.error("Exception Encountered while Running Hive Queries")
            self.logger.error("Exception:"+str(e))
    
    
    def RunSparkSqlCommand(self,Query):
        
        self.logger.info("Executing Query :"+Query)
        
        
        try:
            sqlDF = self.spark.sql(Query)
            
            self.logger.info("#######################Result#################")        
                             
            self.logger.info(sqlDF.show())
            
        except Exception,e:
            self.logger.error("Failure While Execution of Query")
            self.logger.error(str(e))
            
        
    
        
        
        
        
            