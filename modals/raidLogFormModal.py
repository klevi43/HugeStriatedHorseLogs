import discord
from discord.ui import Modal, TextInput
from services.WcAuthService import WcAuthService
from services.RaidLogService import RaidLogService
from constants.constants import REPORT_CODE, NORMAL_DIFFICULTY
class RaidLogFormModal(Modal, title="Get Log For Raid"):
    
    
    guild_name = TextInput(label="Guild Name:", required=True, max_length=100, style=discord.TextStyle.short)
    guild_server_slug = TextInput(label="Guild Server Name:", required=True, max_length=100, style=discord.TextStyle.short)
    
    async def on_submit(self, interaction: discord.Interaction):
        auth_service = WcAuthService()
        rl_service = RaidLogService()
        access_token = await auth_service.getAccessToken()
        if access_token:
            res = await rl_service.get_guild_raid_logs(access_token, { "guildName": self.guild_name.value, "guildServerSlug": self.guild_server_slug.value})
            await interaction.response.send_message(f"Here is your raid log \n {res}")
        else:
            await interaction.response.send_message("Failed to retrieve access token")