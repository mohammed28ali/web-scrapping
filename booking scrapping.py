# 1st step install and import modules
#--install beautifulsoup4
#--install requests
#--install lxml
from bs4 import BeautifulSoup
import requests
import csv
from itertools import zip_longest

hotel_name=[]
hotel_price=[]
hotel_review=[]

#2nd step use requests to fetch the url
result = requests.get("https://www.booking.com/searchresults.html?aid=376381&label=bookings-naam-0U48THtFadjZBwJ4BHv4SgS267724713972%3Apl%3Ata%3Ap1%3Ap22%2C563%2C000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1005386%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YV19IumoQ3O5HnTajxNh2ss&sid=46866454347a409e18d765bb193f7e9f&sb=1&src=searchresults&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fsearchresults.html%3Faid%3D376381%3Blabel%3Dbookings-naam-0U48THtFadjZBwJ4BHv4SgS267724713972%253Apl%253Ata%253Ap1%253Ap22%252C563%252C000%253Aac%253Aap%253Aneg%253Afi%253Atikwd-65526620%253Alp1005386%253Ali%253Adec%253Adm%253Appccp%253DUmFuZG9tSVYkc2RlIyh9YV19IumoQ3O5HnTajxNh2ss%3Bsid%3D46866454347a409e18d765bb193f7e9f%3Btmpl%3Dsearchresults%3Bclass_interval%3D1%3Bdest_id%3D-302053%3Bdest_type%3Dcity%3Bdtdisc%3D0%3Bgroup_adults%3D2%3Bgroup_children%3D0%3Binac%3D0%3Bindex_postcard%3D0%3Blabel_click%3Dundef%3Bno_rooms%3D1%3Boffset%3D0%3Bpostcard%3D0%3Braw_dest_type%3Dcity%3Broom1%3DA%252CA%3Bsb_price_type%3Dtotal%3Bshw_aparth%3D1%3Bslp_r_match%3D0%3Bsrpvid%3D65fb9d77eb11013a%3Bss_all%3D0%3Bssb%3Dempty%3Bsshis%3D0%26%3B&ss=Sharm+El+Sheikh&is_ski_area=0&ssne=Sharm+El+Sheikh&ssne_untouched=Sharm+El+Sheikh&city=-302053&checkin_year=2022&checkin_month=3&checkin_monthday=26&checkout_year=2022&checkout_month=3&checkout_monthday=31&group_adults=1&group_children=0&no_rooms=1&from_sf=1&sr_change_search=2")

#3rd step save page content/markup
src=result.content 

#4th step create soup object to parse content and pass paremeter to constructor
soup = BeautifulSoup(src, "lxml")

#5th step find the elements containing info we need
hotel_names=soup.find_all("div",{"class":"fde444d7ef _c445487e2"})
hotel_prices=soup.find_all("span",{"class":"fde444d7ef _e885fdc12"})
hotel_reviews=soup.find_all("div",{"_9c5f726ff _192b3a196 f1cbb919ef"})

#6th step loop over returned lists to extract needed info into other lists
for i in range(len(hotel_names)):
    hotel_name.append(hotel_names[i].text)
    hotel_price.append(hotel_prices[i].text)
    hotel_review.append(hotel_reviews[i].text)

#7th step create csv file and fill with values
file_list=[hotel_name,hotel_price,hotel_review]
exported=zip_longest(*file_list)
with open("F:\Collage\Fourth year\web scrapping project/test22.csv","w")as myfile:
    wr=csv.writer(myfile)
    wr.writerow(['hotels names','hotels prices','hotel reviews'])
    wr.writerows(exported)


#x =[1,2,3]
#y =['a','b','c']
#z =[x,y]
#unpacking
#*z ---> [[1,2,3],['a','b','c']]
#zip_logest(*z)--->[1,'a'][2,'b'][3,'c']












 # links.append(job_titles[i].find("a").attrs['href'])

#for link in links:
    #result = requests.get(link)
    #src =result.content
    #soup=BeautifulSoup(src,"lxml")
    #salaries=soup.find("span",{"class":"css-4xky9y"})
    #salary.append(salaries.text.strip())
    #requirements=soup.find("div",{"css-1t5f0fr"}).ul
    #respon_text=""
    #for li in requirements.find_all("li"):
    #   respon_text +=li.text +'|'
    #responsibility.append(respon_text)