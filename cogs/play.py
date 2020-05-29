from discord.ext import commands
import sqlite3
from time import time, sleep
from threading import Thread
from discord import Embed
from colours import colours
from random import seed, choice
from datetime import datetime


class Play(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        seed(datetime.now())

        try:
            self.db = sqlite3.connect('quizzes.db')
        except sqlite3.Error as e:
            print(e)

        self.cur = self.db.cursor()

        # self.team_channels = [709725462296920075,
        #                       709725581326942228]

        # self.viewer_channel = 708721354702323752

        self.team_channels = [698232547821486131,
                              698232569681936454]

        self.viewer_channel = 698232508118204416

        self.TIME_LIMIT = 90

    @commands.command()
    async def play(self, ctx, quiz_id=0):
        if quiz_id == 0:
            await ctx.send("You must provide a quiz ID. `!play <quiz_id>`\n"
                           "To see a list of your quizzes, use `!quizzes`", delete_after=20.0)
            await ctx.message.delete()
            return

        self.cur.execute("SELECT owner FROM quizzes WHERE quiz_id=?", (quiz_id,))
        owner = self.cur.fetchone()

        if ctx.message.author.id == owner[0]:
            await ctx.message.delete()
            self.cur.execute("SELECT max(quiz_quest_num) FROM questions WHERE quiz_id=?", (quiz_id,))
            row = self.cur.fetchone()
            count = row[0]
            self.cur.execute("INSERT INTO playing VALUES (?, ?, ?, ?, ?)",
                             (owner[0], quiz_id, count, 1, 'N'))
            self.db.commit()
        else:
            await ctx.send("This quiz doesn't belong to you, buddy.", delete_after=20.0)

    @commands.command()
    async def end(self, ctx):
        await ctx.message.delete()
        self.cur.execute("DELETE FROM playing WHERE owner=?", (ctx.message.author.id,))
        self.db.commit()

    @commands.command()
    async def ask(self, ctx):

        owner = ctx.message.author.id
        await ctx.message.delete()
        self.cur.execute("SELECT quiz_id, questions, current_q, in_progress FROM playing WHERE owner=?", (owner,))
        quiz = self.cur.fetchone()

        if quiz is None:
            await ctx.send("You don't have an active quiz running. You can start one with `!play <quiz_id>`.\n"
                           "To see a list of your quizzes, use `!quizzes`")
            return

        if quiz[3] == 'Y':
            await ctx.send("A question is still in progress for this quiz.", delete_after=20.0)
            return

        if quiz[2] > quiz[1]:
            await ctx.send("No more questions left. Please end the quiz with `!end`", delete_after=30.0)
        else:
            thread = Thread(target=await self.run_question(quiz, owner))
            thread.start()

    @commands.command()
    async def force(self, ctx, q):
        await ctx.message.delete()

        try:
            q_int = int(q)
        except ValueError:
            await ctx.send(f'{q} is not a valid number.', delete_after=20.0)
            return

        self.cur.execute("UPDATE playing SET current_q=?, in_progress=? WHERE owner=?", (q_int, 'N',
                                                                                         ctx.message.author.id))
        self.db.commit()

    @commands.command()
    async def quizzes(self, ctx):
        await ctx.message.delete()

    @commands.command()
    async def test(self, ctx):
        await ctx.message.delete()
        for channel in self.team_channels:
            c = self.bot.get_channel(channel)
            await c.send('Bleep, bloop...', delete_after=10.0)

        c = self.bot.get_channel(self.viewer_channel)
        await c.send('Bleep, bloop...', delete_after=10.0)

    async def run_question(self, quiz, owner):
        self.cur.execute("SELECT * FROM questions WHERE quiz_id=? AND quiz_quest_num=?", (quiz[0], quiz[2]))
        question = self.cur.fetchone()

        embed = Embed(title=f'Question {quiz[2]}:',
                      colour=choice(colours),
                      description=f'{question[3]}')

        if question[4] != "":
            embed.set_image(url=question[4])

        for channel in self.team_channels:
            c = self.bot.get_channel(channel)
            await c.send(embed=embed)

        c = self.bot.get_channel(self.viewer_channel)
        await c.send(embed=embed)

        self.cur.execute("UPDATE playing SET in_progress=? WHERE owner=?", ('Y', owner))
        self.db.commit()
        asked_at = int(time())
        while (int(time()) - asked_at) < self.TIME_LIMIT:
            if (int(time()) - asked_at) % (self.TIME_LIMIT / 3) == 0 and int(time()) - asked_at != self.TIME_LIMIT:
                t = int(time()) - asked_at
                for channel in self.team_channels:
                    c = self.bot.get_channel(channel)
                    await c.send(f'**{self.TIME_LIMIT - t} seconds remaining...**')
                sleep(1)

        for channel in self.team_channels:
            c = self.bot.get_channel(channel)
            await c.send('🛑')
        self.cur.execute("UPDATE playing SET current_q=?, in_progress=? WHERE owner=?", (quiz[2] + 1, 'N',
                                                                                         owner))
        self.db.commit()

    @commands.command()
    async def test(self, ctx):
        await ctx.message.delete()

        for channel in self.team_channels:
            c = self.bot.get_channel(channel)
            await c.send('test')

        c = self.bot.get_channel(self.viewer_channel)
        await c.send('test')


def setup(bot):
    bot.add_cog(Play(bot))
