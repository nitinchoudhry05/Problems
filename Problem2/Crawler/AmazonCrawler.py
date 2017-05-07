import BeautifulSoup
import urllib, requests
import time

class AmazonCrawler(object):


	def __init__(self):

		self.URLS=["http://www.amazon.in/Apple-iPhone-7-Black-32GB/dp/B01LZKSVRB/ref=sr_1_1?s=electronics&ie=UTF8&qid=1494159010&sr=1-1&keywords=iphone+7","http://www.amazon.in/Apple-iPhone-6S-Space-Grey/dp/B01LX3A7CC/ref=sr_1_1?s=electronics&ie=UTF8&qid=1494159437&sr=1-1&keywords=iphone+6s","http://www.amazon.in/Moto-Play-4th-Gen-Black/dp/B01FM7GIR4/ref=sr_1_1?s=electronics&ie=UTF8&qid=1494159486&sr=1-1&keywords=moto+g","http://www.amazon.in/Google-Pixel-Quite-Black-32GB/dp/B01M5J1A1T/ref=sr_1_1?s=electronics&ie=UTF8&qid=1494159560&sr=1-1&keywords=google+pixel","http://www.amazon.in/Apple-iPhone-5s-Space-Grey/dp/B00FXLC9V4/ref=sr_1_1?s=electronics&ie=UTF8&qid=1494159589&sr=1-1&keywords=iphone+5"]

	def get_prod_info(self,url):

    	    	resp = requests.get(url)
		prod_info = {'name':'NotFound','price':'NotFound'}
	      	try:
			count=10
    			while "</div>" not in resp.text and count>0 :
				time.sleep(1)
				resp = requests.get(url)
				count -=1
				
    			soup = BeautifulSoup.BeautifulSoup(resp.text,fromEncoding='utf-8')
			count=10			
			while soup==None and count >0:
				count -=1
				soup = BeautifulSoup.BeautifulSoup(resp.text,fromEncoding='utf-8')    			

    			prod_column=soup.find(attrs={'id':'centerCol'})
				
    			p_name = prod_column.find(attrs={'id':'productTitle'})
    			p_our_price = prod_column.find(attrs={'id':'priceblock_ourprice'})

			
    			if p_name:
        			prod_info['name'] = p_name.text
        			if p_our_price:
            				prod_info['price'] = p_our_price.text
    			return prod_info




		except Exception,e:
			#print resp.text
                	#print "#########################"
			#print e
			return prod_info
			



	def Run(self):
		Final={}
		i=0
		for URL in self.URLS:
			
			Final["Amazon-"+str(i)]=self.get_prod_info(URL)
			time.sleep(.01)
			i=i+1

		return Final	

"""
def main():


	D=AmazonCrawler()
	print D.Run()

	

main()
"""
