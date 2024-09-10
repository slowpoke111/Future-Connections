import aiohttp
import asyncio
from datetime import datetime, timedelta

async def fetch_connections_solution(future=1):
    today = datetime.now()
    target_date = today + timedelta(days=future)
    date_str = target_date.strftime("%Y-%m-%d")

    url = f"https://www.nytimes.com/svc/connections/v2/{date_str}.json"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                return data["categories"]
    except Exception as error:
        print("Error fetching the Connections solution:", error)
        raise Exception(error)


async def main(future=1):
    categories = await fetch_connections_solution(future=future)
    print(categories)


if __name__ == "__main__":
    asyncio.run(main(future=1))
