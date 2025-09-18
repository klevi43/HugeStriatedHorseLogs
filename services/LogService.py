
import os, aiohttp
from constants.constants import GET_FIGHT_IDS_QUERY, GUILD_QUERY, GET_LAST_RAID_LOG_QUERY
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
        public_api_url = os.getenv("BASE_URL") + os.getenv("PUBLIC_DATA_URI")
        q_payload = {"query": GET_LAST_RAID_LOG_QUERY}
        async with aiohttp.ClientSession() as session: 
            async with session:
                fight_query = {"query": GET_FIGHT_IDS_QUERY}
                fight_query_res = await session.post(public_api_url, headers=headers, json=fight_query)
                fight_id_list_json = await fight_query_res.json()
                fight_id_list = [f["id"] for f in fight_id_list_json["data"]["reportData"]["reports"]["data"][0]["fights"]]
                damage_query = {"query": GET_LAST_RAID_LOG_QUERY, "variables": {"fightIDs": fight_id_list}}
                damage_res = await session.post(public_api_url, headers=headers, json=damage_query)
                data = await damage_res.json()
                print(data["data"]["reportData"]["reports"]["data"][0]["rankings"]["data"][0].get("roles"))
                boss_data = self._extract_json_data(data).get("encounter")
                tank_data = self._extract_json_data(data).get("roles").get("tanks")
                dps_data = self._extract_json_data(data).get("roles").get("dps")
                healer_data = self._extract_json_data(data).get("roles").get("healers")
                #table = data["data"]["reportData"]["reports"]["data"][0]["table"]
                
                return [boss_data, tank_data, healer_data]
    def _extract_json_data(self, data):
        return data["data"]["reportData"]["reports"]["data"][0]["rankings"]["data"][0]