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
    mypic = soup.find_all("a", {"class": "thumbnail"})
    img_url = mypic[0].find('img').get('src')
    mytable = soup.find_all("div", {"class": "tab-pane active"})
    description = mytable[0].find_all('p')[0].get_text().rstrip().strip()
    publisher = mytable[0].find_all('td')[1].get_text()
    author = mytable[0].find_all('td')[3].get_text()
    serie = mytable[0].find_all('td')[5].get_text()
    year = mytable[0].find_all('td')[7].get_text()
    pages = mytable[0].find_all('td')[9].get_text()
    ISBN = mytable[0].find_all('td')[11].get_text()
    vol = mytable[0].find_all('td')[13].get_text()
    cover = mytable[0].find_all('td')[15].get_text()
    weight = mytable[0].find_all('td')[17].get_text()
    print("description: "+description)
    print("img_url: "+img_url)
    print("publisher: "+publisher)
    print("author: "+author)
    print("serie: "+serie) 
    print("year: "+year) 
    print("pages: "+pages)
    print("ISBN: "+ISBN)
    print("number of volumes: "+vol)
    print("cover: "+cover)
    print("weight: "+weight)
    # print(len(mytable))
    # print(dir(mytable))
    # for i in range(0,len(mydivs)):
        # print(mydivs)#visi produkti
        # print(mydivs[i])#atsevisks produkts
        # item_title=mydivs[i].find('img').get('alt')#item_title
        # item_url=mydivs[i].find('a').get('href')#item_url
        # img_url=mydivs[i].find('img').get('src')#img_url
        # item_price=mydivs[i].find("p", {"class": "price"}).get_text().rstrip().strip()#item_price
        # line=(item_title+"|"+item_price+"|"+item_url+"|"+img_url)
        # with open('test.csv', mode='a') as csv_file:#file name must be specified
        #     csv_file.write(line)
        #     csv_file.write('\n')

end = time.time()
end_tuple = time.localtime()
end_time = time.strftime("%Y-%m-%d %H:%M:%S", end_tuple)
print("Script ended: "+end_time)
print("Script running time: "+time.strftime('%H:%M:%S', time.gmtime(end - start))) 