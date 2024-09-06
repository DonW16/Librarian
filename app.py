import discord
from discord import app_commands
from collections import Counter
import datetime
import random
import os
#import pytz
import asyncio

supported_urls = []

intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync()
    print(f'Logged in as {client.user.name}')

@tree.command(name="play", description="Play URL from YouTube, Spotify, SoundCloud, Odyssey.")
@app_commands.describe(url="The URL of the video to play.")
async def play(interaction: discord.Interaction, url: str):
    try:
        # Check if the user is in a voice channel
        if interaction.user.voice is None:
            await interaction.response.send_message("You are not in a voice channel.")
            return

        # Get the voice channel the user is in
        voice_channel = interaction.user.voice.channel

        # Connect to the voice channel
        voice_client = await voice_channel.connect()

        # Play the YouTube video
        voice_client.play(discord.FFmpegPCMAudio(url))

        # Send a message to indicate that the video is playing
        await interaction.response.send_message(f"Now playing: {url}")

        # Wait for the video to finish playing
        while voice_client.is_playing():
            await asyncio.sleep(1)

        # Disconnect from the voice channel
        await voice_client.disconnect()

    except Exception as e:
        await interaction.response.send_message(f"An error occurred: {str(e)}")

    await tree.sync()

@tree.command(name="stats", description=f"Get server stats.")
async def stats(interaction: discord.Interaction):
    await stats(interaction)
    await tree.sync()

@tree.command(name="archive-url", description=f"Archive URL on the server.")
async def archive(interaction: discord.Interaction):
    await archive(interaction)
    await tree.sync()

@tree.command(name="archive-list", description=f"List all archived for the server.")
async def archive(interaction: discord.Interaction):
    await archive(interaction)
    await tree.sync()

@tree.command(name="archive-filter", description=f"Specify a filter")
async def archive(interaction: discord.Interaction):
    await archive(interaction)
    await tree.sync()

@tree.command(name="auto-archive-filter", description=f"Specify a Regex filter to automatically archive URLs on the Discord server.")
async def archive(interaction: discord.Interaction):
    await archive(interaction)
    await tree.sync()

@tree.command(name="rss-add", description=f"Add RSS feed to the Discord server.")
async def archive(interaction: discord.Interaction):
    await archive(interaction)
    await tree.sync()

@tree.command(name="rss-remove", description=f"Remove RSS feed.")
async def archive(interaction: discord.Interaction):
    await archive(interaction)
    await tree.sync()

@tree.command(name="nitter-add", description=f"Add Twitter account feed to the Discord server.")
async def archive(interaction: discord.Interaction):
    await archive(interaction)
    await tree.sync()

@tree.command(name="nitter-remove", description=f"Remove Twitter account feed.")
async def archive(interaction: discord.Interaction):
    await archive(interaction)
    await tree.sync()

@tree.command(name="video", description=f"Play video on server, via sharescreen.")
async def archive(interaction: discord.Interaction):
    await archive(interaction)
    await tree.sync()

# async def main():
#     # Schedule the task
#     task = asyncio.create_task()
#     # Optionally, await the task if you want to wait for its completion
#     await task

if __name__ == "__main__":
    # Run the main coroutine, which will start the event loop
    # asyncio.run(main())

    # Fetch discord token via os.env
    token = os.getenv(str('DISCORD_BOT_TOKEN'))
    # Run the client with the token
    client.run(token)