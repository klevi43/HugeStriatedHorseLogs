import discord 
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os, aiohttp
from containers.container import log_service, wc_auth_service
from modals.raidLogFormModal import RaidLogFormModal

def main():
    load_dotenv()
    token = os.getenv("DISCORD_TOKEN")
    guild_id = os.getenv("GUILD_ID")
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
      
    bot = commands.Bot(command_prefix="!", intents=intents)
    
    @bot.event
    async def on_ready():
        await bot.tree.sync()
        print("Bot ready and commands synced.")
        
    @bot.event
    async def on_member_join(member): 
        await member.send(f"Welcome to the server {member.name}")
    
    @bot.command()
    async def show_commands(ctx):
        await ctx.send("""!get_log_blorp => fetches log and returns it in chat\n\n!getLogSendToDm => fetches log and sends it to you as a dm""")
    
    @bot.tree.command(name="get_log")
    async def get_log(interaction: discord.Interaction):
        raid_log_form_modal = RaidLogFormModal()
        await interaction.response.send_modal(raid_log_form_modal)
    
    @bot.tree.command(name="get_last_raid_log")
    async def get_last_raid_log(interaction: discord.Interaction):
        await interaction.response.defer()
        token = await wc_auth_service.getAccessToken()
        res = await log_service.get_last_guild_raid_log(token)
        await interaction.followup.send(res)
    
    async def get_log_send_to_dm():
        pass
    #we use the token to get the bot here
    bot.run(token)
    
if __name__ == "__main__":
    main()
    
