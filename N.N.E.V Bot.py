import discord
import random
from discord.ext import commands

description = '''Este es un codigo con vsc para lanzar imagenes'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix = '#', description = description, intents = intents)

links_estudios = [
    'https://energy.mit.edu/area/nuclear/',
    'https://ourworldindata.org/safest-sources-of-energy',
    'https://www.health.harvard.edu/cancer/radiation-risk-from-medical-imaging',
    'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6194698/'
]

links_videos = [
    'https://www.youtube.com/watch?v=J3znG6_vla0',
    'https://www.youtube.com/watch?v=glM80kRWbes',
    'https://www.youtube.com/watch?v=IzQ3gFRj0Bc'

]

@bot.event
async def on_ready():
    print(f'Logged as: {bot.user} (ID: {bot.user.id}) ')


@bot.command(name='com')
async def com(ctx):
    embed = discord.Embed(
        title="Comandos",
        description="Estos son los comandos disponibles",
        color=discord.Color.green()
    )
    embed.add_field(name="#com", value="Muestra los comandos del bot", inline=False)
    embed.add_field(name="#info_v", value="Da un link a un video sumamente detallado sobre la energia nuclear", inline=False)
    embed.add_field(name="#info", value="Da un link a un estudio sobre la energia nuclear o un estudio relacionado con ella", inline=False)
    embed.add_field(name="#video_al", value="Da un link a un video aleatorio sobre la energia nuclear ", inline=False)

    await ctx.send(embed=embed)


@bot.command(name='info_v')
async def info_v(ctx):
    slideshow_url = 'https://www.youtube.com/watch?v=yMmB36Nxvy8'
    embed = discord.Embed(
        title="Video Informatico",
        description="Link de video informatico sobre la enegia nuclear:",
        color=discord.Color.blue()
    )
    embed.add_field(name="Video", value=f"[Mira el video]({slideshow_url})", inline=False)
    await ctx.send(embed=embed)


@bot.command(name='info')
async def info(ctx):
    slideshow_url = random.choice(links_estudios)
    embed = discord.Embed(
        title="Pagina Informatica",
        description="Link de un estudio aleatoreo sobre la energia nuclear:",
        color=discord.Color.blue()
    )
    embed.add_field(name="Estudio", value=f"[NUCLEAR ENERGY]({slideshow_url})", inline=False)
    await ctx.send(embed=embed)


@bot.command(name='video_al')
async def video_al(ctx):
    slideshow_url = random.choice(links_videos)
    embed = discord.Embed(
        title="Un video aleatorio",
        description="Un video aleatorio sobre la energia nuclear",
        color=discord.Color.blue()
    )
    embed.add_field(name="Video", value=f"[NUCLEAR]({slideshow_url})", inline=False)
    await ctx.send(embed=embed)




bot.run('Discord Token') 
