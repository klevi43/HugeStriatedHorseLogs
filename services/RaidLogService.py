import aiohttp
import os
from dotenv import load_dotenv
load_dotenv()

class RaidLogService:
    base_url = os.getenv("BASE_URL")
    public_uri = os.getenv("PUBLIC_DATA_URI")
    async def get_player_raid_log(self, char_name: str, server_slug: str, access_token):
        """Fetches data from wclogs API. Please provide a character name, server slug, and parameters"""
        print(access_token)
        headers = {"Authorization": f"Bearer {access_token}"}
        url = self.base_url + self.public_uri
        query = f"""
            {{
                characterData {{
                    character(name: "{char_name}", serverSlug: "{server_slug}", serverRegion: "us") {{
                        name
                        classID
                        server {{
                            name
                        }}
                    }}
                }}
            }}
        """
        q_payload = {"query": query}
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, data=q_payload) as res: 
                return await res.text()