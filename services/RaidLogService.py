import aiohttp
import os
from constants.constants import TEST_QUERY, GUILD_QUERY
from dotenv import load_dotenv
load_dotenv()
class RaidLogService:
    base_url = os.getenv("BASE_URL")
    public_uri = os.getenv("PUBLIC_DATA_URI")
    async def get_guild_raid_logs(self, access_token, variables):
        """Fetches data from wclogs API. Please provide a character name, server slug, and parameters"""
        headers = {"Authorization": f"Bearer {access_token}"}
        url = self.base_url + self.public_uri
        
        q_payload = {"query": GUILD_QUERY, "variables": variables}
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, json=q_payload) as res: 
                return await res.text()