import discord
from discord.ext import commands
import re

class MediaReactionBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', intents=discord.Intents.all())

    @property
    def emojis(self):
        return self._emojis

    @emojis.setter
    def emojis(self, emojis):
        self._emojis = emojis

    @property
    def channels(self):
        return self._channels

    @channels.setter
    def channels(self, channels):
        self._channels = channels

    async def on_message(self, message):
        if message.channel.id in self._channels:
            # Check for both attachments and links
            if message.attachments:
                if message.attachments[0].filename.endswith(('.jpg', '.jpeg', '.png', '.mp4', '.mov', '.webm')):
                    for emoji in self._emojis:
                        await message.add_reaction(emoji)
            elif re.search(r"(https?:\/\/[^\s]+\.(?:jpg|jpeg|png|mp4|mov|webm))", message.content):
                link = re.search(r"(https?:\/\/[^\s]+\.(?:jpg|jpeg|png|mp4|mov|webm))", message.content).group(1)
                for emoji in self._emojis:
                    await message.add_reaction(emoji)

if __name__ == '__main__':
    bot = MediaReactionBot()
    bot.channels = [1014635028367548526, 1014635232923746304]  # Replace with your channel IDs
    bot.emojis = ['👍', '👎', '🗑️']  # Replace with your desired emojis
    bot.run(token)
