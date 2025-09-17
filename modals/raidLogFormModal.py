import discord
from discord.ui import Modal, TextInput
from services.WcAuthService import WcAuthService
class RaidLogFormModal(Modal, title="Get Log For Raid"):
    
    
    char_name = TextInput(label="Character Name:", required=True, max_length=100, style=discord.TextStyle.short)
    
    
    async def on_submit(self, interaction: discord.Interaction):
        auth_service = WcAuthService()
        access_token = await auth_service.getAccessToken()
        if access_token:
            await interaction.response.send_message(f"Here is your raid log {self.char_name}")
        else:
            await interaction.response.send_message("Failed to retrieve access token")