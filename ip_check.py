import aiohttp
import asyncio
import json
i

url = 'https://api.myip.com'

async def check_ip():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            r = await resp.text()
            results = json.loads(r)
            print(results)
asyncio.run(check_ip())                       