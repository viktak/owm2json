import json
import requests
import subprocess

from . import version

class owmRequestor:

    def __init__(self, apinames, lat, lon, appid):
        #   Init variables
        self.apinames = apinames
        self.lat = lat
        self.lon = lon
        self.appid = appid
        self.data = "{"

    def GetData(self):
        self.data +="\"module\":{"
        self.data +="\"version\":\""
        self.data += version.currentVersion
        self.data +="\""
        self.data +="},"
        #   Call each OpenWeatherMap API in the list
        #   and build a JSON string containing all the results 
        for apiname in self.apinames:
            self.data += "\"" + apiname + "\":"
            self.data += requests.get(f"https://api.openweathermap.org/data/2.5/{apiname}?lat={self.lat}&lon={self.lon}&appid={self.appid}").text
            self.data += ","
        
        #   Remove the last comma ","
        self.data = self.data[:-1]  

        #   Finish JSON string
        self.data += "}"

        #   Return JSON string containing all the result
        return (self.data)

