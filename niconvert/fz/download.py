import requests
import re

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"}


class Download:
    def download(self, url, filePath=None):
        cid = self.get_cid(url)
        if cid == "x":
            print("cid not found")
            exit(1)
        print("cid is "+cid)
        danmu_url = "https://comment.bilibili.com/" + cid + ".xml"
        xml = requests.get(danmu_url, headers=headers).content.decode('utf-8')
        # ass = generate_ass(danmu_list)
        # with open(cid + ".ass", "wb+") as ass_file:
        #     ass_file.write(ass.encode("utf-8"))
        if filePath is None or len(filePath) == 0:
            filePath = cid + ".xml"
        with open(filePath, "wb+") as file:
            file.write(xml.encode("utf-8"))

    def get_cid(self, url):
        html = requests.get(url, headers=headers).content.decode('utf-8')
        if "cid" in html:
            return re.search(r'"cid":(\d*)', html).group(1)
        else:
            return "x"

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
