'''
Created on 05-May-2017

@author: nitinchoudhry

'''
from pyspark.sql import SparkSession
from Resources.Logger import *
from pyspark import SQLContext
from pyspark.sql.functions import *

class SparkExecutor():
    
    def __init__(self,SrcFile="../Configs/aadhar_data.csv"):

        print "PySpark Executor Initiated"
        print "Using Src File %s for PySpark Analytics" %SrcFile     
        self.SrcFile=SrcFile
        self.spark=SparkSession.builder.appName("Python Spark SQL basic example").config("spark.some.config.option", "some-value") .getOrCreate()
        self.sequelcontext=SQLContext(self.spark)
    
    
    def Run(self):
        
        
        logs("../Output/SparkLogs")
        self.logger=Initiate_logger("SparkLogs") 
        self.df=self.sequelcontext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true').load(self.SrcFile)
        self.logger.info("Successfully Created Data frame  from Src File")
        self.df.createOrReplaceTempView("TestTable")
        try:        
            self.Problem1()
        
        except Exception,e:    
            self.logger.error("Exception Encountered while executing the Problems")
            self.logger.error("Exception "+str(e))
    
    def Problem1(self):
        
        self.logger.info("Create a data frame using the file and provide its summary")
        
        self.logger.info("Executing df.describe().show()")
        self.df.describe().show()
        
        
        
    def Problem2(self):
        pass
        


    def Problem3(self):
        
        self.logger.info("Problem:Find the number of unique pincodes in the data")
        print "Problem:Find the number of unique pincodes in the data"
        sqlDF = self.spark.sql("select count(distinct pincode) from TestTable")
        sqlDF.show()
    
    
    
    def Problem4(self):
        self.logger.info("Problem:Find the number of Aadhaar registrations rejected in Uttar Pradesh and Maharashtra?")
        print "Problem:Find the number of Aadhaar registrations rejected in Uttar Pradesh and Maharashtra?"
        sqlDF = self.spark.sql('select sum(rejected) from TestTable where state="Uttar Pradesh" or state="Maharashtra"')
        sqlDF.show()