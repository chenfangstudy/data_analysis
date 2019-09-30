from bs4 import BeautifulSoup
import requests
import csv
import bs4
 
 
#检查url地址
def check_link(url):
    try:
        
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('无法链接服务器！！！')
 


 
#爬取资源
def get_contents(ulist,rurl):
    soup = BeautifulSoup(rurl,'lxml')
    title = soup.find('title').get_text()
    ulist.append(title)
    trs = soup.find_all('tr')
    for tr in trs:
        ui = []
        for td in tr:
            ui.append( td.string)
        uii = [x for x in ui if x!=None]
        result_temp = [x.strip() for x in uii if x.strip()!='']
        ulist.append(result_temp)
    
#保存资源
def save_contents(urlist):
    with open(urlist[0]+".csv",'w') as f:
        writer = csv.writer(f)
        writer.writerow([urlist[0]])
        for i in range(len(urlist)-1):
            writer.writerow(urlist[i+1])
 
def main():
    urli = []
    url = "http://cbadata.sports.sohu.com/ranking/teams_detail/?spm=smpc.fb-sports-home.ranklist-2.1.1569764142049TfucJrk"
    rs = check_link(url)
    get_contents(urli,rs)
    save_contents(urli)
 
main()

