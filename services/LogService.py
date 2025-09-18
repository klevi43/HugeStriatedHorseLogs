
import os, aiohttp
from constants.constants import TEST_QUERY, GUILD_QUERY
from dotenv import load_dotenv

load_dotenv()
class LogService:
   
    async def get_guild_raid_logs(self, access_token, variables):
        """Fetches data from wclogs API. Please provide a character name, server slug, and parameters"""
        headers = {"Authorization": f"Bearer {access_token}"}
        
        
        q_payload = {"query": GUILD_QUERY, "variables": variables}
        async with aiohttp.ClientSession() as session:
            async with session.get(public_api_url, headers=headers, json=q_payload) as res: 
                return await res.text()
    
    
    async def get_last_guild_raid_log(self, access_token):
        """Fetches data for the last completed raid. Please provide the access token"""
        headers = {"Authorization": f"Bearer {access_token}"}
        print(public_api_url)
        print(session)