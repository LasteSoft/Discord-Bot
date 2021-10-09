import discord
from discord.ext import commands

Bot = commands.Bot(command_prefix="TA!", intents=discord.Intents.all(), help_command=None)
Responses = {
  "こんにちは": "こんにちは！",
  "こんばんは": "こんばんは！",
  "おやすみ": "お休みー",
  "疲れた": "お疲れ様ー"
}
@Bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  
  for rk, rv in Responses.items():
    if rk in message.content:
      await message.reply(rv)
      
  await bot.process_commands(message)
@Bot.event
async def on_ready():
  print("Tearokoがオンラインになりました！")
  game = discord.Game(f"TA! | {len(bot.guilds)}サーバー | {len{bot.users)}ユーザー | 作成者: aroko1#6837")
  await bot.change_presence(activity=game, status=discord.Status.do_not_disturb)

@Bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingPermissions):
        embed = discord.Embed(title=":x: 失敗 -MissingPermissions", description="実行者の必要な権限が無いため実行出来ません。", timestamp=ctx.message.created_at, color=discord.Colour.red())
        embed.set_footer(text="お困りの場合は、@aroko1#6837をメンションしてください。")
        await ctx.send(embed=embed)
    elif isinstance(error, discord.ext.commands.errors.BotMissingPermissions):
        embed = discord.Embed(title=":x: 失敗 -BotMissingPermissions", description=f"Botの必要な権限が無いため実行出来ません。", timestamp=ctx.message.created_at, color=discord.Colour.red())
        embed.set_footer(text="お困りの場合は、@aroko1#6837をメンションしてください。")
        await ctx.send(embed=embed)
    elif isinstance(error, discord.ext.commands.errors.CommandNotFound):
        embed = discord.Embed(title=":x: 失敗 -CommandNotFound", description=f"不明なコマンドもしくは現在使用不可能なコマンドです。", timestamp=ctx.message.created_at, color=discord.Colour.red())
        embed.set_footer(text="お困りの場合は、@aroko1#6837をメンションしてください。")
        await ctx.send(embed=embed)
    elif isinstance(error, discord.ext.commands.errors.MemberNotFound):
        embed = discord.Embed(title=":x: 失敗 -MemberNotFound", description=f"指定されたメンバーが見つかりません。", timestamp=ctx.message.created_at, color=discord.Colour.red())
        embed.set_footer(text="お困りの場合は、@aroko1#6837をメンションしてください。")
        await ctx.send(embed=embed)
    elif isinstance(error, discord.ext.commands.errors.BadArgument):
        embed = discord.Embed(title=":x: 失敗 -BadArgument", description=f"指定された引数がエラーを起こしているため実行出来ません。", timestamp=ctx.message.created_at, color=discord.Colour.red())
        embed.set_footer(text="お困りの場合は、@aroko1#6837をメンションしてください。")
        await ctx.send(embed=embed) 
    elif isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        embed = discord.Embed(title=":x: 失敗 -BadArgument", description=f"指定された引数が足りないため実行出来ません。", timestamp=ctx.message.created_at, color=discord.Colour.red())
        embed.set_footer(text="お困りの場合は、@aroko1#6837をメンションしてください。")
        await ctx.send(embed=embed) 
    elif isinstance(error, discord.ext.commands.errors.CommandInvokeError):
        embed = discord.Embed(title=":x: 失敗 -CommandInvokeError", description=f"コマンドには属性がないため実行できません。", timestamp=ctx.message.created_at, color=discord.Colour.red())
        embed.set_footer(text="お困りの場合は、@aroko1#6837をメンションしてください。")
        await ctx.send(embed=embed)
    else:
        raise error
@bot.command()
async def help(ctx):
    guild = ctx.message.guild
    embed = discord.Embed(title=f"コマンド一覧 - {guild.name}", timestamp=ctx.message.created_at, color=discord.Colour.dark_blue(), inline=False)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.add_field(name="ここに移行しました", value="creating", inline=False)
    embed.set_footer(text=f" 実行者: {ctx.author} ", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
