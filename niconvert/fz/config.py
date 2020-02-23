import os
import json


class Config:
    def __init__(self):
        pass

    def get():

        if os.path.isfile("config.json"):
            try:
                with open("config.json") as file:
                    data = json.load(file)
                    return data
            except:
                pass

        data = {
            "normal": {"title": r'"title":"([^"]+)","pubdate',
                       "pages": r'"cid":(\d+),"page"[^\{]+"part":"([^"]+)"'},
            "movie": {"title": r'"ssId":[0-9]+,"title":"([^"]+)"',
                      "pages": r'"cid":(\d+),[^\{]+"title":"([^"]+)"'},
            "custom": {"title": '', "pages": ''},
            "format": "[title] - [cid] - [pagetitle].xml"}
        with open('config.json', 'w') as file:
            json.dump(data, file)
        return data

    def save(config):
        with open('config.json', 'w') as file:
            json.dump(config, file)
