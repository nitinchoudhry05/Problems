from flask import Flask
from AmazonCrawler import AmazonCrawler
from SnapdealCrawler import SnapdealCrawler
from PayTMCrawler import PayTMCrawler
import json

Crawler1=AmazonCrawler()
Crawler2=SnapdealCrawler()
Crawler3=PayTMCrawler()
app = Flask(__name__)

@app.route("/MobilePrices")
def Prices():
    return GetPrices()

    #return str(Crawler1.Run())+"\n\n\n"+str(Crawler2.Run())


def GetPrices():

	First=Crawler1.Run()
	Second=Crawler2.Run()
	Third=Crawler3.Run()
	Phones=["Iphone 7","Iphone 6s","Moto G","Google Pixel","Iphone 5s"]
	Final={}
	count=0
	for element in Phones:
		tmp={}
		tmp["Amazon-"+str(count)]=First["Amazon-"+str(count)]
		tmp["Snapdeal-"+str(count)]=Second["Snapdeal-"+str(count)]
		tmp["Paytm-"+str(count)]=Third["Paytm-"+str(count)]
		Final[element]=tmp
		count+=1
	
	return str(Final)


	
if __name__ == "__main__":
    app.run()
