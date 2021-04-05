from discord.ext import commands
import os
import random

def pics():
    with open('images.txt', 'r') as f:
        lines = f.read().splitlines()
    random.shuffle(lines)
    yield from lines


def pineapple():
    p = pics()
    while True:
        try:
            yield p.__next__()
        except StopIteration:
            p = pics()
            yield p.__next__()


class PineappleBot(commands.Bot):
    async def on_ready(self):
        print("Ready as {} | ID: {}".format(self.user, self.user.id))



pineapples = pineapple()
bot = PineappleBot(
    'p'
)


@bot.command(name='ineapple', aliases=['p'])
async def pineapplecmd(ctx):
    await ctx.send(pineapples.__next__())



@bot.command(name='ineapples', aliases=['s'])
async def pineapplescmd(ctx, amount: int = None):
    if amount is None:
        amount = random.randint(1,5)
    for i in range(amount):
        await ctx.send(pineapples.__next__())


bot.run(os.getenv('TOKEN'))
