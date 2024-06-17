import os
import discord

from dice_bot_pyohio import config

# 1. Instantiate Discord bot object
discord_bot: discord.Bot = discord.Bot()

# 3. Discord bot first goes to the `on_ready` method
@discord_bot.event # Decorator that waits for events to happen in Discord
async def on_ready():
    print("Starting up the bot!")


if __name__ == "__main__":
    # 2. Pass Discord api token to bot (wrap in try/catch block to be safe)
    try:
        # 2.1. The Bot run command will actually start up the discord bot lifecycle
        discord_bot.run(os.getenv(f"{config.DISCORD_TOKEN}"))
    except RuntimeError as run_err:
        print(run_err)
