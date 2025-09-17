import discord 
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

from modals.raidLogFormModal import RaidLogFormModal


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("DISCORD_TOKEN")
    guild_id = os.getenv("GUILD_ID")
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    
    bot = commands.Bot(command_prefix="!", intents=intents)
    
    @bot.event
    async def on_ready():
        guild = discord.Object(id=guild_id)
        await bot.tree.sync(guild=guild)
        print("Bot ready and commands synced.")
        
    @bot.event
    async def on_member_join(member): 
        await member.send(f"Welcome to the server {member.name}")
    
    @bot.command()
    async def show_commands(ctx):
        await ctx.send("""!get_log => fetches log and returns it in chat\n\n!getLogSendToDm => fetches log and sends it to you as a dm""")
    
    @bot.tree.command(name="get_log")
    async def get_log(interaction: discord.Interaction):
        raid_log_form_modal = RaidLogFormModal()
        await interaction.response.send_modal(raid_log_form_modal)
    
    async def get_log_send_to_dm():
        pass
    #we use the token to get the bot here
    bot.run(token)

    
