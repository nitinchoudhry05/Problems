"""
author="Nitin Choudhry"

"""
import sys
sys.path.append("../")
from Resources import pyhs2

class hivetable:
    
    
    
        def __init__(self,hiveserver="",port="10000",user="hive",paswword="hive@123",dbname="default",logger):
            self.hiveServer = hiveserver
            self.port = port
            self.user = user
            self.password = paswword
            self.dbname = dbname
            self.Logger=logger
        
        def getpartitionstring(self,parts):
                retstr=""
                for key in parts:
                        lit=parts[key]
                        if(lit.replace("-","").replace(".","").isdigit()):
                            retstr+=key+"="+lit+","
                        else:
                            retstr+=key+"=\'"+parts[key]+"\',"
                return retstr[:-1]

        def getpartitioncols(self,parts):
                retstr=""
                for key in parts:
                        retstr+=key+" "+parts[key]+","
                return retstr[:-1]

        def runHiveCommand(self, queries):
                status = 0
                try:
                    with pyhs2.connect(host=self.hiveServer,
                                  port=self.port,
                                  authMechanism="PLAIN",
                                  user=self.user,
                                  password=self.password,
                                  database=self.dbname) as conn:
                        with conn.cursor() as cur:
                            queryList = []
                            queryList = queries.split(";")
                            for query in queryList:
                                if query != '' and query != ' ':   
                                 
                                    try:
                                        self.Logger.info("Executing Query")
                                        cur.execute(query)
                                    except Exception as e:
                                        status = e.errorCode
                                        print ("Hive Query Failed:"+query)
                                        print(e.errorMessage)
                                else:
                                    print ("Hive Query Successful")
                except:
                    print ("Hive Query Failed:"+query)
                    status = 1 
                return status


        def create(self,table,serialclass,fileformat,partitionkeys, hiveServer):
                self.hiveServer = hiveServer

                query="CREATE EXTERNAL TABLE "+table+" PARTITIONED BY ("+self.getpartitioncols(partitionkeys)
                query+=") ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.thrift.ThriftDeserializer'"
                query+=" WITH SERDEPROPERTIES(\'serialization.format\'=\'"
                query+=fileformat+"\',\'serialization.class\'=\'"
                query+=serialclass+"\') STORED AS SEQUENCEFILE;"

                self.runHiveCommand (query)

        
