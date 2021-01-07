import aiohttp
import asyncio
import json
import sys

#To Ommit the Event Closed because of using aiohttp 
if sys.version_info[0] == 3 and sys.version_info[1] >=8 and sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(async.WindowsSelectorEventLoopPolicy())


url = 'https://api.myip.com'

async def check_ip():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            r = await resp.text()
            results = json.loads(r)
            print(results)
asyncio.run(check_ip())                       