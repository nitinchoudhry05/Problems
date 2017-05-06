__author__ = 'nitin.choudhary'
###the script is being written in order to give the user the ability to use send commands to the name node setup to perform certain operations#####
#1. This will only work when the machine are enabled with no password command on the root user

import commands
from Logger  import *

class Commands():

    def __init__(self,machineIP="127.0.0.1",machineUser="",machinePaasword=""):
        
            self.logger=Initiate_logger("Commands")            
            try:
                self.getDatials(machineIP,machineUser,machinePaasword)
            except Exception ,e:
                print "Proceeding further to execute commands remotely"
                print e
                


    def getDatials(self,machineIP,machineUser,machinePaasword):
        #print machineIP,machineUser,machinePaasword
        self.IP=machineIP
        self.user=machineUser
        self.password=machinePaasword
        self.logger=Initiate_logger("Commands")
        #RemoteServerAuthenticator(self.IP,self.user,self.password)
        self.logger.info("Successfully Authenticated The Remote Server")


    def ShellCommand(self,command):
        self.logger.info("The user has asked to execute the shell command "+command)
        RemoteDetail="root@"+self.IP
        cmd= "ssh -o ConnectTimeout=300 -o StrictHostKeyChecking=no " + RemoteDetail +" '"+ command +"'"
        #print cmd
        (status,output)=commands.getstatusoutput(cmd)
        try:
            if status ==0:
                self.logger.info("Successfully Executed Command "+cmd)
                return status,output
            else:
                self.logger.error("Failed to execute Command "+cmd)
                return status,output
        except Exception,e:
                self.logger.error("Following exception occurred while executing the command "+cmd)
                self.logger.error("Exception:"+e)
                return status,output



    def Sparksql(self,command,host,port,db):
        self.logger.info("the user has asked to execute the sparksql  command"+command)
        sparksqlcmd= '/opt/spark/bin/beeline -u jdbc:hive2://'+host+':'+port+'/'+db+ ' -e "'+command+'"'
        return self.ShellCommand(sparksqlcmd)
    
    
    def HdfsCommand(self,command):
        
        self.logger.info("the user has asked to execute the HDFS  command"+command)
        hdfsCommand= 'hadoop dfs -'+command
        return self.ShellCommand(hdfsCommand)
    
    def ExecuteCommand(self,cmd):
        self.logger.info("The user has asked to execute the shell command "+cmd)
        (status,output)=commands.getstatusoutput(cmd)
        try:
            if status ==0:
                self.logger.info("Successfully Executed Command "+cmd)
                return status,output
            else:
                self.logger.error("Failed to execute Command "+cmd)
                return status,output
        except Exception,e:
                self.logger.error("Following exception occurred while executing the command "+cmd)
                self.logger.error("Exception:"+e)
                return status,output
    
