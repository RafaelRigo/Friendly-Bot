import discord
from discord.ext import commands
import json
import requests
import random


class ZenQuotes(commands.Cog):
    """All zen quotes commands"""
    @commands.command(
        name='zenquote',
        brief='A command to get a random zen quote',
        help='Use this command for me to send a random zen quote :)'
    )
    async def zenquote(self, ctx):
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + "\n*-" + json_data[0]['a'] + "*"
        embed = discord.Embed(title='Daily quote', url='https://zenquotes.io', description=quote, color=discord.Colour.yellow())
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text='Quote generated by https://zenquotes.io')
        try:
            await ctx.send(embed)
        except:
            await ctx.send("An error occurred…")

    @commands.command(
        name='dailyquote',
        brief='A command to get the daily zen quote',
        help='Use this command for me to send the daily zen quote'
    )
    async def dailyquote(self, ctx):
        response = requests.get("https://zenquotes.io/api/today")
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + '\n*-' + json_data[0]['a'] + '*'
        embed = discord.Embed(title='Daily quote', url='https://zenquotes.io', description=quote, color=discord.Colour.yellow())
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text='Quote generated by https://zenquotes.io')
        try:
            await ctx.send(embed)
        except:
            await ctx.send("An error occurred…")
