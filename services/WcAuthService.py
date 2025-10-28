import requests 
import os
import json
import aiohttp, asyncio
from aiohttp import BasicAuth
class WcAuthService:
    _access_token: str = None
    
    async def getAccessToken(self):
        if self._access_token is None:
            client_id = os.getenv("WC_CLIENT_ID")
            client_pwd = os.getenv("WC_CLIENT_PWD")
            payload = {"grant_type": "client_credentials"}
            auth = BasicAuth(client_id, client_pwd)
            oauth_url = os.getenv("BASE_URL") + os.getenv("OAUTH_URI")
            async with aiohttp.ClientSession() as session:
                async with session.post(oauth_url, data=payload, auth=auth) as res:
                    if res.status == 200:
                        json_data = await res.json()
                        access_token = json_data.get("access_token")
                        return access_token
                    else:
                        print(f"Failed to retrieve access token. \n Status: {res.status()}")
                        return None
        else:
            return self._access_token