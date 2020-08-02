import os
from discord.ext import commands

bot = commands.Bot(command_prefix="Your Bot Prefix")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print("Logged in as {}({})".format(bot.user.name, bot.user.id))

@bot.command()
async def hi(ctx):
    await ctx.send("hello")

if __name__ == "__main__":
    bot.run(TOKEN)
