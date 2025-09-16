import discord 
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("DISCORD_TOKEN")
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    
    
    bot = commands.Bot(command_prefix="!", intents=intents)
    @bot.event
    async def on_ready():
        print(f"Ready to go in ,  {bot.user.name}")
        
    @bot.event
    async def on_member_join(member): 
        await member.send(f"Welcome to the server {member.name}")
    
    @bot.command()
    async def show_commands(ctx):
        await ctx.send("""!get_log => fetches log and returns it in chat\n\n!get_log_for_me => fetches log and sends it to you as a dm""")
    @bot.command()
    async def get_log(ctx):
        await ctx.send(f"Showing the log form for {ctx.author.mention}")
    
    @bot.command()
    async def get_log_for_me(ctx):
        await ctx.author.send(f"Here is the log form for {ctx.author.mention}")

    #we use the token to get the bot here
    bot.run(token, log_handler=handler, log_level=logging.DEBUG)

    
