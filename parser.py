import time
import csv
import requests
import config
from bs4 import BeautifulSoup

start = time.time()
start_tuple=time.localtime()
start_time = time.strftime("%Y-%m-%d %H:%M:%S", start_tuple)

# url_list=open('list.txt', 'r')
# uniqe=[]
# for ele in url_list:
#     uniqe.append(ele)
# url=set(uniqe)
# new_list=open('url.txt', 'a')
# for ele in url:
#     new_list.write(ele)

url=open('url.txt', 'r')
for elemt in url:
    page=requests.get(elemt, proxies=config.proxies, allow_redirects=False)
    # if page.status_code == 200:
    #     print(elemt+': Success!')
    # elif page.status_code == 404:
    #     print(elemt+': Not Found.')
    soup = BeautifulSoup(page.content, 'html.parser')
    mydivs = soup.find_all("div", {"class": "product-layout"})
    
    for i in range(0,len(mydivs)):
        # print(mydivs)#visi produkti
        # print(mydivs[i])#atsevisks produkts
        item_title=mydivs[i].find('img').get('alt')#item_title
        item_url=mydivs[i].find('a').get('href')#item_url
        img_url=mydivs[i].find('img').get('src')#img_url
        item_price=mydivs[i].find("p", {"class": "price"}).get_text().rstrip().strip()#item_price
        line=(item_title+"|"+item_price+"|"+item_url+"|"+img_url)
        with open('test.csv', mode='a') as csv_file:#file name must be specified
            csv_file.write(line)
            csv_file.write('\n')

end = time.time()
end_tuple = time.localtime()
end_time = time.strftime("%Y-%m-%d %H:%M:%S", end_tuple)
print("Script ended: "+end_time)
print("Script running time: "+time.strftime('%H:%M:%S', time.gmtime(end - start))) 