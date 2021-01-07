import aiohttp
import asyncio
import json
import sys
import colorama
from colorama import Fore
colorama.init()

#To Ommit the Event Closed because of using aiohttp 
if sys.version_info[0] == 3 and sys.version_info[1] >=8 and sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


url = 'https://api.myip.com'

async def check_ip():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            r = await resp.text()
            results = json.loads(r)
            ip = results['ip']
            country = results['country']
            country_code = results['cc']
            print(Fore.GREEN+'[+]'+Fore.RESET+ ' Your Public Ip: '+Fore.LIGHTCYAN_EX+f'{ip}\n'+Fore.RESET+Fore.GREEN+
                  '[+]'+Fore.RESET+ ' Your Country:'+f'{country}\n'+Fore.GREEN+'[+]'+Fore.RESET+ ' Your Country Code:'+f'{country_code}\n')
            
asyncio.run(check_ip())                       