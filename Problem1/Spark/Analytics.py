'''
Created on 08-May-2017

@author: nitinchoudhry
'''



import sys
sys.path.append("../")
from pyspark.sql import SparkSession
from Resources.Logger import *
from pyspark import SQLContext
from pyspark.sql.functions import *

class Analytics():
    
    def __init__(self,SrcFile="../Configs/aadhaar_data.csv"):

        print "Analytics Initiated"
        print "Using Src File %s for Pyspark Analytics" %SrcFile     
        self.SrcFile=SrcFile
        self.spark=SparkSession.builder.appName("Analytics").config("spark.some.config.option", "some-value") .getOrCreate()
        self.sequelcontext=SQLContext(self.spark)
    
    
    def Run(self):
        
        
        logs("../Output/AnalyticsLogs")
        self.logger=Initiate_logger("AnalyticsLogs") 
        self.df=self.sequelcontext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true').load(self.SrcFile)
        self.logger.info("Successfully Created Data frame  from Src File")
        self.df.createOrReplaceTempView("TestTable")
        try:        
            self.Problem1()
            self.Problem2()
            self.Problem3()
            self.Problem4()
            self.Problem5()
        
        except Exception,e:    
            self.logger.error("Exception Encountered while executing the Problems")
            self.logger.error("Exception "+str(e))
    
    def Problem1(self):
        
        self.logger.info("The top 3 states where the percentage of Aadhaar cards being generated for males is the highest.")
        print "The top 3 states where the percentage of Aadhaar cards being generated for males is the highest"
        self.One=self.df.select("aadhaar_generated","state").filter("gender='M'").groupby("state").sum()
        self.OneResult=self.One.sort(self.One[1].desc()).limit(3)
        self.OneResult.show()
        
        
        
        
        
    def Problem2(self):
        
        self.logger.info("In each of these 3 states, identify the top 3 districts where the percentage of Aadhaar cards being rejected for females is the highest.")
        print "In each of these 3 states, identify the top 3 districts where the percentage of Aadhaar cards being rejected for females is the highest."
        
        for row in self.OneResult.collect():
            state=row["state"]
            self.second=self.df.select("rejected","district").filter("state='"+state+"'").filter("gender='F'").groupby("district").sum()
            self.secondResult=self.second.sort(self.second[1].desc()).limit(3)
            self.secondResult.show()
        


    def Problem3(self):
        
        self.logger.info("The top 3 states where the percentage of Aadhaar cards being generated for Females is the highest.")
        print "The top 3 states where the percentage of Aadhaar cards being generated for Females is the highest"
        self.third=self.df.select("aadhaar_generated","state").filter("gender='F'").groupby("state").sum()
        self.thirdResult=self.third.sort(self.third[1].desc()).limit(3)
        self.thirdResult.show()
        
    
    
    
    def Problem4(self):
        
        self.logger.info("In each of these 3 states, identify the top 3 districts where the percentage of Aadhaar cards being rejected for males is the highest.")
        print "In each of these 3 states, identify the top 3 districts where the percentage of Aadhaar cards being rejected for males is the highest."
        
        for row in self.thirdResult.collect():
            state=row["state"]
            self.fourth=self.df.select("rejected","district").filter("state='"+state+"'").filter("gender='M'").groupby("district").sum()
            self.fourthResult=self.fourth.sort(self.fourth[1].desc()).limit(3)
            self.fourthResult.show()
            
            
            

    def Problem5(self):
	pass            
            
        
