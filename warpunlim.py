# Aurthor : revWhiteSHadow @TG (White9Shadow @ Github)
# A tool to get unlimited gb on warp(1.1.1.1).
# Build Device : Ubuntu + Android 
# Tools that test With : Termux ,Android Terminal , Net Hunter terminal , Ubuntu Terminal,Kali,vs code, windows, mac, Iphone
# This is a licanced script under GPL V3 , If you are using any part of this script use proper credit 

from datetime import datetime
from json import dumps
from random import choice, randint
from string import ascii_letters, digits
from time import sleep
import httpx

ascii_art = """

 __          __     _____  _____          
 \ \        / /\   |  __ \|  __ \     _   
  \ \  /\  / /  \  | |__) | |__) |  _| |_ 
   \ \/  \/ / /\ \ |  _  /|  ___/  |_   _|
    \  /\  / ____ \| | \ \| |        |_|  
     \/  \/_/    \_\_|  \_\_|             
"""
print(ascii_art)
print("1111 / Warp Vpn WARP+ Unlimited GB")
print("")
print("Script : by revWhiteShadow")
print("Codename : motherfucker rem01gaming ")
print("")
print("Website : www.godTspeed.xyz")
print("Website : www.magiskflash.com")
print("Telegram : @godTspeed")
print("Telegram : @godspeedmode")
print("")
print("For WARP client ID, go to 1.1.1.1 settings, advanced diagnostics, copy the IP and paste it below.")
WARP_CLIENT_ID = input("Please enter your WARP client ID: ")
SUCCESS_COUNT, FAIL_COUNT = 0, 0
def genString(stringLength):
    letters = ascii_letters + digits
    return ''.join(choice(letters) for _ in range(stringLength))
def digitString(stringLength):
    digit = digits
    return ''.join(choice(digit) for _ in range(stringLength))
url = f"https://api.cloudflareclient.com/v0a{digitString(3)}/reg"
while True:
    try:
        install_id = genString(22)
        body = {
            "key": f"{genString(43)}=",
            "install_id": install_id,
            "fcm_token": f"{install_id}:APA91b{genString(134)}",
            "referrer": WARP_CLIENT_ID,
            "warp_enabled": False,
            "tos": f"{datetime.now().isoformat()[:-3]}+02:00",
            "type": "Android",
            "locale": "es_ES"
        }
        data = dumps(body).encode("utf8")
        headers = {
            "Content-Type": "application/json; charset=UTF-8",
            "Host": "api.cloudflareclient.com",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.12.1"
        }
        response = httpx.post(url, data=data, headers=headers)
    except Exception as error_code:
        print(f"Error: {error_code}")
        FAIL_COUNT += 1
        continue
    if response.status_code == 200:
        SUCCESS_COUNT += 1
        print(f"PASSED: +1GB (total: {SUCCESS_COUNT}GB, failed: {FAIL_COUNT})")
    else:
        print(f"FAILED: {response.status_code}")
        FAIL_COUNT += 1
    cooldown_time = 5
    print(f"Sleep: {cooldown_time} seconds.")
    sleep(cooldown_time)
