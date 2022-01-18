import httpx
import string
import requests
import threading
import random
import discum
import time
from itertools import cycle 
from fakecookies import fcs
from multiprocessing.dummy import Pool as ThreadPool
import hfuck as hcaptcha
import redis
from colorama import Fore, Back, Style
import os, time
import json
from colorama import init
from termcolor import colored
import base64
from time import time
init()
import discord
from httpx import Client
from base64 import b64encode
import secrets
from pypresence import Presence

rpc = Presence("855983945463103498")
rpc.connect()

def logo():
	logomenu = Fore.CYAN +"""                                           by Discord.Link/200IQ
                            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                            █▄─▀█▀─▄██▀▄─██─▄▄▄▄█─▄▄▄▄███─▄▄▄▄█▄─▄▄─█▄─▀█▄─▄█
                            ██─█▄█─███─▀─██▄▄▄▄─█▄▄▄▄─███─██▄─██─▄█▀██─█▄▀─██ 
                            ▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀       																		
"""
	print(logomenu)



def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))
with open('Invite.json', 'r+', encoding='utf-8') as configfile:
    config = json.load(configfile)


proxyListx = []
sison = httpx
lock = threading.Lock()
imagestoencode = []

#destruction updated this 1/10/2021
def register(proxy):
    HCAPTCHA_BYPASS_TOKEN = "Z0D+pHOrfSQbCwPL8bCS1VDTDG0GSK9pz/9S0gUJkNlaDEAZGtHBY1D8y32ey7R/pr13fMMF2y1KjzNjMQdihOcfYWibMMRDsMQHASN6xfd8lFfKxkoxHnqVcAXHY/opbcLB8JRtg5bgM0PqirzxYPRGDsutjZDckNANoI7YhpDvo8SnSP38nl7OjByHDUMHaaAUGSlBTpyAkKEU18X4xF5OjrEQFBm6wvqOtgf2Bazr24uK+6glIwulsUga00MenOCb55DrTfc5D0M/DWpnGkGNAJuJAjg0/zXtKbIYOOwnUbNbMRMa3s+3DBoLrKvSYnbZgHFFQIh+WMM0lpedBRAFNKI3g37nHylgKUAAlTDJJU+c8Te8UAuq3imzUAQycKH9NOEx3xWQCMBP+HKOIawYUObudsW+CqFavzE+uwH0P9C5+drR5fqumsodLjHbfJjKLy8yomwnczGwGx5GBA8flDqTWQufUoxNRfOcTfE0iiwA0gtAvNxhtWNkGLEW3Rb6GOmNeyObxryZkPkpJw==l1AmWRWQqVjeOZLO"
    SOLVER_PARAMS = dict(database=redis.Redis(host='127.0.0.1', port=6379, db=4), min_answers=0, collect_data=True)
    CHALLENGE_PARAMS = dict(sitekey="f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34", page_url="https://discord.com",