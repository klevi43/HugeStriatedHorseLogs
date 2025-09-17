import discord
from discord.ui import Modal, TextInput
class RaidLogFormModal(Modal, title="Get Log For Raid"):
    
    
    char_name = TextInput(label="Character Name:", required=True, max_length=100, style=discord.TextStyle.short)
    