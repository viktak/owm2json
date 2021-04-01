#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests

import secrets

import sys
sys.path.append('/home/dev/python/owm2json/src/')

import owm2json

apinames = ["air_pollution", "onecall", "roadrisk"]

myOWM = owm2json.owmRequestor(apinames, secrets.lat, secrets.lon, secrets.appid)

print(myOWM.GetData())
