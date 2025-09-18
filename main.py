import discord 
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os, aiohttp
from containers.container import log_service, session
from modals.raidLogFormModal import RaidLogFormModal

def main():
    load_dotenv()
    token = os.getenv("DISCORD_TOKEN")
    guild_id = os.getenv("GUILD_ID")
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    public_api_url = os.getenv("BASE_URL") + os.getenv("PUBLIC_DATA_URI")
    
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
    
    @bot.tree.command(name="get_last_raid_log")
    async def get_last_raid_log(interaction: discord.Interaction):
        log_service.get_last_guild_raid_log("abc")
    
    
    async def get_log_send_to_dm():
        pass
    #we use the token to get the bot here
    bot.run(token)
    
if __name__ == "__main__":
    main()
    
