__author__ = 'nitin.choudhary'

import logging
import logging.handlers


def Initiate_logger(name):
        logger = logging.getLogger(name)
        print "Loger object is created with the name "+name
        return logger

def logs(Filename):
        file=open(Filename,"w+")
        logging.getLogger().handlers = []
        FORMAT = '%(levelname)s : %(name)s %(asctime)-15s %(funcName)s:: %(message)s'
        logging.basicConfig(filename=Filename,level=logging.DEBUG, format=FORMAT)
