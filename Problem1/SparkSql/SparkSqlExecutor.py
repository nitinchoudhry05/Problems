'''
Created on 05-May-2017

@author: nitinchoudhry
'''
import sys
sys.path.append("../")
from pyspark.sql import SparkSession
from Resources.Logger import *
from pyspark import SQLContext

class SparkSqlExecutor():
    
    def __init__(self,SrcFile="../Configs/aadhaar_data.csv",QueryFile="../Configs/SparkSqlQueries",tablename="Test"):
    
        self.QueryFile=open(QueryFile,"r")
        self.SrcFile=SrcFile
        self.spark=SparkSession.builder.appName("Python Spark SQL basic example").config("spark.some.config.option", "some-value") .getOrCreate()
        self.table=tablename
        self.sequelcontext=SQLContext(self.spark)
    
    
    def Run(self):
        
        logs("../Output/SparkSqlLogs")
        self.logger=Initiate_logger("SparkSqlLogs")
        Lines=self.QueryFile.readlines()
        df=self.sequelcontext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true').load(self.SrcFile)
        df.createOrReplaceTempView(self.table)
        try:
            for line in Lines:
                self.logger.info("Running command :"+line)
                print "Running command :"+line
                sqlDF = self.spark.sql(line.strip("\n").strip(";"))
                sqlDF.coalesce(1).write.format("com.databricks.spark.csv").option("header", "true").mode("append").save("../Output/SparkSqlResutls")
                self.logger.info("Successfully Ran :"+line)
        except Exception,e:
            self.logger.error("Exception Encountered while Running Hive Queries")
            self.logger.error("Exception:"+str(e))
    
    
    
        
        
        
        
            
