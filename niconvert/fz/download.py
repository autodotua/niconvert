import requests
import re

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"}


class Download:
    def download(self, cid, filePath):
        if not bool(cid):
            raise Exception("cid为空")
        danmu_url = "https://comment.bilibili.com/" + cid + ".xml"
        xml = requests.get(danmu_url, headers=headers).content.decode('utf-8')
      
        with open(filePath, "wb+") as file:
            file.write(xml.encode("utf-8"))
        return filePath

    def getInfo(self, urlOrAv):
        html = self.getHtml(urlOrAv)
        title=re.search(r'"title":"([^"]+)","pubdate',html)
        pages=re.findall(r'"cid":(\d+),"page"[^\{]+"part":"([^"]+)"',html)
        if len(pages)==0:
            print("page is None")
            pages=[re.findall(r'"cid":(\d+),[^\{]+"title":"([^"]+)"',html)[0]]
        
        #print("page is"+pages)
        return {"title":None if title is None else title.group(1),"pages":list(map(lambda p: {"title":p[1],"cid":p[0]},pages))}
        # if "cid" in html:
        #     return re.search(r'"cid":(\d*)', html).group(1)
        # else:
        #     return "x"

    def getHtml(self,urlOrAv):
         html = requests.get(urlOrAv, headers=headers).content.decode('utf-8')
         return html
    def format_time(self, time_raw):
        hour = str(int(time_raw / 3600))
        if hour != '0':
            time_raw %= 3600
        minute = str(int(time_raw / 60))
        if minute != '0':
            time_raw %= 60
        if len(minute) == 1:
            minute = "0" + minute
        second = str(round(time_raw, 2))
        if '.' in second:
            if len(second.split('.')[0]) == 1:
                second = "0" + second
            if len(second.split('.')[1]) == 1:
                second = second + "0"
        else:
            if len(second) == 1:
                second = "0" + second + ".00"
            else:
                second = second + ".00"
        return hour + ':' + minute + ':' + second


if(__name__ == "__main__"):
    download = Download()
    download.download("https://www.bilibili.com/video/av88761848")
