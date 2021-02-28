import discord
import asyncio
from discord.ext import commands, tasks
from discord.ext.commands import BucketType, CooldownMapping
from discord_slash import cog_ext, SlashContext, manage_commands
from discord.ext.commands.errors import MissingPermissions

class SlashCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    #on_ready event example
    @commands.Cog.listener()
    async def on_ready(self):
        print('<SlashCommands> Test module loaded!')
    
    #fill with id's of guilds where you want to use slash commands
    guild_id = [320574287046115328]

    @cog_ext.cog_slash(
        name="test",
        guild_ids=guild_id,  
        description="Test command.", 
        options=[
            manage_commands.create_option("option1", "Member example.", discord.Member, True),
            manage_commands.create_option("option2", "Bool example.", bool, True),
            manage_commands.create_option("option3", "String example.", str, False) #if set to False it't optional
            ])
    @commands.has_permissions(administrator=True) #right now we have to use discord.ext check
    async def _test(self, ctx, member : discord.Member):
        try:
            await ctx.respond(True)
            
        except Exception as E:
            print(E)

    #error handler
    @commands.Cog.listener()
    async def on_slash_command_error(self, ctx: SlashContext, error):
        try:
            await ctx.respond(True)
            if isinstance(error, MissingPermissions):
                mess = await ctx.send(f":exclamation: Missing permissions: `{','.join(error.missing_perms)}`!")
                await asyncio.sleep(5)
                await mess.delete()
        except Exception as E:
            print(E)  


def setup(client):
    client.add_cog(SlashCommands(client))
