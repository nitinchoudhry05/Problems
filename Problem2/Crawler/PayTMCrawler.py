import BeautifulSoup
import urllib, requests
import time

class PayTMCrawler(object):


	def __init__(self):


		self.URLS=["https://paytm.com/shop/p/apple-iphone-7-32-gb-black-MOBAPPLE-IPHONEANAN1675118D805215?src=search-grid&tracker=organic%7C66781%7Ciphone%207%7Cgrid%7CSearch%7C%7C1%7Cproduction&site_id=1&child_site_id=1","https://paytm.com/shop/p/apple-iphone-6s-32-gb-rose-gold-MOBAPPLE-IPHONENGP197413C60399FB?src=search-grid&tracker=autosuggest%7C66781%7Capple%20iphone%206s%7Cgrid%7CSearch%7C%7C1%7Cproduction&site_id=1&child_site_id=1","https://paytm.com/shop/p/moto-g-turbo-edition-white-MOBMOTO-G-TURBOBALA561208B4E103ED?src=search-grid&tracker=organic%7C66781%7Cmoto%20g4%7Cgrid%7CSearch%7C%7C1%7Cproduction&site_id=1&child_site_id=1","https://paytm.com/shop/p/google-pixel-32-gb-quite-black-MOBGOOGLE-PIXELPASU525042B63E578?src=search-grid&tracker=autosuggest%7C66781%7Cgoogle%20pixel%7Cgrid%7CSearch%7C%7C1%7Cproduction&site_id=1&child_site_id=1","https://paytm.com/shop/p/apple-iphone-5s-16-gb-silver-Apple_IPHONE5S_16GB_Silver_22943?src=search-grid&tracker=organic%7C66781%7Ciphone%205s%7Cgrid%7CSearch%7C%7C1%7Cproduction&site_id=1&child_site_id=1"]	
		
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

    			prod_column=soup.find(attrs={'id':'app'})
				
    			p_name =soup.title.string
			#print p_name
			"""
			p_our_price = prod_column.find(attrs={'id':'priceblock_ourprice'})
			while p_name==None or p_our_price==None:
				p_name = prod_column.find(attrs={'id':'productTitle'})
                        
				p_our_price = prod_column.find(attrs={'id':'priceblock_ourprice'})
			"""
    			price = prod_column.find(attrs={'class':'_2CNI'})
			p_our_price=price.find(attrs={'class':'_1d5g'})
			
   			#p_sale_price = prod_column.find(attrs={'id':'priceblock_saleprice'})
    			#p_deal_price = prod_column.find(attrs={'id':'priceblock_dealprice'})
   			#p_misc_price =prod_column.find(attrs={'class':'a-color-price'})

			
    			if p_name:
        			prod_info['name'] = p_name
        			if p_our_price:
            				prod_info['price'] = p_our_price.text
				"""
        			elif p_sale_price:
            				prod_info['price'] = p_sale_price.text
        			elif p_deal_price:
            				prod_info['price'] = p_deal_price.text
        			else:
            				prod_info['price'] = p_misc_price.text
				"""
    			return prod_info




		except Exception,e:
			#print resp.text
                	#print "#########################"
			print e
			return prod_info
			



	def Run(self):
		Final={}
		i=0
		for URL in self.URLS:
			
			Final["Paytm-"+str(i)]=self.get_prod_info(URL)
			time.sleep(.01)
			i=i+1

		return Final	

"""
def main():


	D=PayTMCrawler()
	print D.Run()

	

main()
"""
