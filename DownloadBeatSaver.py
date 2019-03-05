import requests
import bs4
import re
import json


def download(url, pagesPre, pagesEnd,Ranting , path):
    while pagesPre <= pagesEnd:
        #页数，和请求对应页数的网页
        pageIndex = pagesPre * 20
        pageIndex = str(pageIndex)
        urlPage = url + pageIndex
        r = requests.get(urlPage)

        #获取页面
        soup = bs4.BeautifulSoup(r.text, 'html.parser')
        versionDivList = soup.find_all("td" ,attrs={'class': 'has-text-right'})
        i=0
        while i < len(versionDivList):
            #获取歌曲version
            version = versionDivList[i].text[9:]
            #进入beatsaberApi页面，获取歌曲详细信息
            apiUrl = "https://beatsaver.com/api/songs/detail/" + version
            apiR = requests.get(apiUrl)
            apiJson = json.loads(apiR.text)
            #获取需要的属性
            songID = apiJson['song']['id']
            songName = apiJson['song']['name']
            downVotes = apiJson['song']['downVotes']
            upVotes = apiJson['song']['upVotes']
            downloadUrl = apiJson['song']['downloadUrl']
            playedCount = apiJson['song']['playedCount']
            #计算歌曲评分
            PopularityRating = (upVotes + 5) * 100 / (upVotes + downVotes + 10)
            #下载信息题是
            print("正在下载第:",pagesPre,"页,总计:",pagesEnd,"页")
            print("正在下载第:",i+1,"首歌,该页总共:", len(versionDivList),"首歌," + songName)
            print(PopularityRating)
            #进行下载
            #如果评分高于规定值，且至少有一个人玩过
            if(PopularityRating >= Ranting and playedCount > 1):
                downloadRequest = requests.get(downloadUrl)
                with open(path + str(songID) + ".zip", "wb") as f:
                    f.write(downloadRequest.content)
                print("下载完成")
                downloadRequest.close()
            else:
                print("评分过低不进行下载")
            i += 1
        pagesPre += 1
        r.close()

def downloadFromSearch(path):
    r = ""
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    downloadList = soup.find_all("a", attrs={'type': 'button', 'class': 'btn btn-link'})
    print(downloadList)


url = "https://beatsaver.com/browse/played/"
#下载前多少页的音乐
pagesPre = 0
pagesEnd = 30
path = 'trainData/BeatSaver/'
download(url, pagesPre, pagesEnd, 80.0, path)