import BeautifulSoup
import urllib, requests
import time

class SnapdealCrawler(object):


	def __init__(self):

		self.URLS=["https://www.snapdeal.com/product/apple-iphone-7-32gb-gold/5764608149132713628","https://www.snapdeal.com/product/iphone-6s-16gb/663413326062#bcrumbSearch:iphone%206s","https://www.snapdeal.com/product/moto-g-turbo-edition-16gb/5764608204463464199#bcrumbSearch:moto%20g","https://www.snapdeal.com/product/google-pixel-32gb-quite-black/5764608168240071437#bcrumbSearch:google%20pixel","https://www.snapdeal.com/product/apple-iphone-5s-16-gb/347830397"]
		
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

    			prod_column=soup.find(attrs={'id':'productOverview'})
				
    			p_name =soup.title.string
    			price = prod_column.find(attrs={'class':'pdp-final-price'})
			p_our_price=price.find(attrs={'itemprop':'price'})
			

			
    			if p_name:
        			prod_info['name'] = p_name
        			if p_our_price:
            				prod_info['price'] = p_our_price.text
    			return prod_info




		except Exception,e:
			print e
			return prod_info
			



	def Run(self):
		Final={}
		i=0
		for URL in self.URLS:
			
			Final["Snapdeal-"+str(i)]=self.get_prod_info(URL)
			time.sleep(.01)
			i=i+1

		return Final	

"""
def main():


	D=SnapdealCrawler()
	print D.Run()

	

main()
"""
