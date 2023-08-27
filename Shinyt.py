import discord
import re

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    words_to_detect = ('Shiny', '_**visitor**_', '_**misterious**_', '_**30**_', 'visitor')

    pattern = re.compile('|'.join(map(re.escape, words_to_detect)), re.IGNORECASE)

    if pattern.search(message.content) and message.author.bot:
        user_id_1 = '265686958267695104'
        user_id_2 = '384369634180333568'
        user_id_3 = '384369634180333568'
        user_1 = await bot.fetch_user(user_id_1)
        user_2 = await bot.fetch_user(user_id_2)
        user_3 = await bot.fetch_user(user_id_3)
        mention_1 = user_1.mention
        mention_2 = user_2.mention
        mention_3 = user_3.mention
        await message.channel.send(f'{mention_1} and {mention_2} and {mention_3} (including bots) mentioned the word!')

    for embed in message.embeds:
        if any(pattern.search(value) for value in (embed.title, embed.description)):
            user_id_1 = '265686958267695104'
            user_id_2 = '384369634180333568'
            user_id_3 = '384369634180333568'
            user_1 = await bot.fetch_user(user_id_1)
            user_2 = await bot.fetch_user(user_id_2)
            user_3 = await bot.fetch_user(user_id_3)
            mention_1 = user_1.mention
            mention_2 = user_2.mention
            mention_3 = user_3.mention
            await message.channel.send(f'{mention_1} and {mention_2} and {mention_3} (including bots) mentioned the word in an embed!')
    
    if "_**visitor**_" in message.content:
        user_id_1 = '265686958267695104'
        user_id_2 = '384369634180333568'
        user_id_3 = '384369634180333568'
        user_1 = await bot.fetch_user(user_id_1)
        user_2 = await bot.fetch_user(user_id_2)
        user_3 = await bot.fetch_user(user_id_3)
        mention_1 = user_1.mention
        mention_2 = user_2.mention
        mention_3 = user_3.mention
        await message.channel.send(f'{mention_1} and {mention_2} and {mention_3} (including bots) mentioned the word within _****_!')
    
    await bot.process_commands(message)

@bot.command()
async def say(ctx, *, message):
    allowed_users = ['265686958267695104']

    if str(ctx.author.id) in allowed_users:
        await ctx.send(message)
        await ctx.message.delete()

bot.run('ODc5ODI2MjcyODE2MDc0ODYz.GqzyL-.7DAmOOMeHlobnvcrRormJRshBde_UbunR9lEjE')
