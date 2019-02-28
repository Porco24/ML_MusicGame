import requests
import bs4


def download(url, pagesPre, pagesEnd , path):
    while pagesPre <= pagesEnd:
        #页数，和请求对应页数的网页
        pageIndex = pagesPre * 20
        pageIndex = str(pageIndex)
        urlPage = url + pageIndex
        r = requests.get(urlPage)

        #查找歌曲Div
        soup = bs4.BeautifulSoup(r.text, 'html.parser')
        #获取下载链接(未清洗)
        downloadList = soup.find_all("a" ,attrs={'role':'button','class': 'button'})

        #清洗数据，删除dowloadList中不是下载链接的列表
        downloadList.pop(0)
        downloadListIndex = 0
        i = 0
        while i < len(downloadList):
            #如果不是下载链接，则Pop
            if(downloadListIndex != 0):
                downloadList.pop(i)
                i -= 1

            downloadListIndex += 1
            i += 1
            if (downloadListIndex == 3):
                downloadListIndex = 0

        #进行下载
        songIndex = 1
        for i in downloadList:
            print("第:",pagesPre,"页,总计:",pagesEnd,"页")
            print("第:",songIndex,"首歌,该页总共:", len(downloadList),"首歌")
            downloadUrl = str(i)
            downloadUrl = downloadUrl[24:-32]
            fileName = downloadUrl[downloadUrl.rfind("/")+1:]
            downloadRequest = requests.get(downloadUrl)
            with open(path+fileName+".zip", "wb") as f:
                f.write(downloadRequest.content)
            print(fileName)
            print(downloadUrl)
            print("下载完成")
            songIndex += 1
            downloadRequest.close()
        pagesPre += 1
        r.close()


url = "https://beatsaver.com/browse/played/"
#下载前多少页的音乐
pagesPre = 19
pagesEnd = 30
path = 'trainData/BeatSaver/'
download(url, pagesPre, pagesEnd, path)