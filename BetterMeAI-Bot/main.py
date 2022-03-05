from pydoc import describe
import discord
from discord.ext import commands
from discord import guild
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord.utils import get

from ai_bot import xuly
from editDB import *

# start
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=["mie,"], intents=intents)
slash = SlashCommand(bot, sync_commands=True)
#bot = discord.Client(intents=intents)


@slash.slash(
    name="talk",
    description="Chat with AI bot",
    guild_ids=[880360143768924210],
    options=[
        create_option(
            name="text",
            description="What do u want to say?",
            required=True,
            option_type=3
        )
    ]
)
async def _talkslash(ctx: SlashContext, text: str):

    talk_message = xuly(text)
    n_id = addToDB(text, talk_message)

    answer = "Id question: "+n_id+" \n"+talk_message

    await ctx.send(answer)


@slash.slash(
    name="dataset",
    description="Get AI dataset",
    guild_ids=[880360143768924210],
)
async def _dataset(ctx):
    await ctx.send(file=discord.File("data.csv"))


@slash.slash(
    name="nlu_dataset",
    description="Get AI dataset for train",
    guild_ids=[880360143768924210],
)
async def _nlu_dataset(ctx):
    await ctx.send(file=discord.File("nlu.yml"))


@slash.slash(
    name="train",
    description="Help us train the bot",
    guild_ids=[880360143768924210],
    options=[
        create_option(
            name="question_id",
            description="Question ID",
            required=True,
            option_type=4
        ),
        create_option(
            name="excepted_answer",
            description="Excepted Answer",
            required=True,
            option_type=3
        )
    ]
)
@bot.command(name="train")
async def _train(ctx, *, question_id: int, excepted_answer: str):
    n_id = int(question_id)
    data = str(excepted_answer)

    exceptedAnswer(n_id, data)
    await ctx.send("Add to training file successfully")

my_secret = "Hi hi không cho key đâu :)"
bot.run(my_secret)
