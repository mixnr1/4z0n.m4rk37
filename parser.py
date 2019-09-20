import time
import csv
import requests
import config
from bs4 import BeautifulSoup

start = time.time()
start_tuple=time.localtime()
start_time = time.strftime("%Y-%m-%d %H:%M:%S", start_tuple)
url=open('url.txt', 'r')
for elemt in url:
    page=requests.get(elemt, proxies=config.proxies, allow_redirects=False)
    soup = BeautifulSoup(page.content, 'html.parser')
    item_pic = soup.find_all("a", {"class": "thumbnail"})
    item_name = soup.find(itemprop="name").get_text()
    item_price = soup.find(itemprop="price").get_text()
    img_url = item_pic[0].find('img').get('src')
    mytable = soup.find_all("div", {"class": "tab-pane active"})
    description = mytable[0].find_all('p')[0].get_text().rstrip().strip()
    publisher = mytable[0].find_all('td')[1].get_text().rstrip().strip()
    author = mytable[0].find_all('td')[3].get_text().rstrip().strip()
    serie = mytable[0].find_all('td')[5].get_text().rstrip().strip()
    year = mytable[0].find_all('td')[7].get_text().rstrip().strip()
    pages = mytable[0].find_all('td')[9].get_text().rstrip().strip()
    ISBN = mytable[0].find_all('td')[11].get_text().rstrip().strip()
    vol = mytable[0].find_all('td')[13].get_text().rstrip().strip()
    cover = mytable[0].find_all('td')[15].get_text().rstrip().strip()
    weight = mytable[0].find_all('td')[17].get_text().rstrip().strip()
    line=(item_name + "|" + \
        item_price + "|" + \
        elemt.replace('\n', '').replace('\r', '') + "|" + \
        img_url + "|" + \
        publisher + "|" + \
        author + "|" + \
        serie + "|" + \
        year + "|" + \
        pages + "|" + \
        ISBN + "|" + \
        vol + "|" + \
        cover + "|" + \
        weight+ "|" + \
        description.replace('\n', ' ').replace('\r', '')) 
    with open('test.csv', mode='a') as csv_file:#file name must be specified
        csv_file.write(line)
        csv_file.write('\n')

end = time.time()
end_tuple = time.localtime()
end_time = time.strftime("%Y-%m-%d %H:%M:%S", end_tuple)
print("Script ended: "+end_time)
print("Script running time: "+time.strftime('%H:%M:%S', time.gmtime(end - start))) 