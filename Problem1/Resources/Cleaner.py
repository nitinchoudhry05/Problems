'''
Created on 05-May-2017

@author: nitinchoudhry
'''
import commands
import os

class Cleaner():
    
    
    def __init__(self,File):
      
        if os.path.exists("../Output") and os.path.exists("../OldOutput"):
            status,output=commands.getstatusoutput("mv ../Output/"+File+"* ../OldOutput")
            if status==0:
                print "Successfully Cleaned the Output Folder"
            else:
                print "Unable To Clean OutPut Folder "
                print "Reason "+str(output)
        
        else:
            os.mkdir("../Output")
            os.mkdir("../OldOutput")
                        
        
    
      