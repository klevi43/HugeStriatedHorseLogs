import discord
from discord.ui import Modal, TextInput
from services.WcAuthService import WcAuthService
from services.RaidLogService import RaidLogService
class RaidLogFormModal(Modal, title="Get Log For Raid"):
    
    
    char_name = TextInput(label="Character Name:", required=True, max_length=100, style=discord.TextStyle.short)
    server_slug = TextInput(label="Server Name:", required=True, max_length=100, style=discord.TextStyle.short)
    
    async def on_submit(self, interaction: discord.Interaction):
        auth_service = WcAuthService()
        rl_service = RaidLogService()
        access_token = await auth_service.getAccessToken()
        if access_token:
            res = await rl_service.get_player_raid_log(self.char_name, self.server_slug, access_token)
            await interaction.response.send_message(f"Here is your raid log {self.char_name} \n {res}")
        else:
            await interaction.response.send_message("Failed to retrieve access token")