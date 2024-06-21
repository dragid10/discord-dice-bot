import os
import discord

from dice_bot_pyohio import config, helpers

# 1. Instantiate Discord bot object
discord_bot: discord.Bot = discord.Bot()

# ========== BOT ==========
# 3. Discord bot first goes to the `on_ready` method
@discord_bot.event # Decorator that waits for events to happen in Discord
async def on_ready():
    print(f"Starting up the bot: {discord_bot.user}")

# 4. Create a simple testing command so we know the bot is alive and well
# Command name is the function name if not specified in the command decorator
@discord_bot.command(description="Sends the bot's latency.")
async def ping(context: discord.ApplicationContext):
    """Sends the bot's latency. Invoked by the user when they type `/ping`

    Args:
        context (discord.ApplicationContext): The discord application context. Represents the context in which a command is being invoked und
    """
    await context.respond(f"Pong! Latency is {discord_bot.latency:.2f} seconds")


# 5. Create a command that the user can invoke to roll the dice
@discord_bot.command(description="Roll the dice that is passed in by the user. Example: 2d10")
@discord.option("user_roll", type=discord.SlashCommandOptionType.string)
async def roll(context: discord.ApplicationContext, user_roll: str) -> list[int]:
    """Parse the user's roll and return the result.

    Args:
        context (discord.ApplicationContext): The discord application context. Represents the context in which a command is being invoked und
        user_roll (str): The user's roll input
    """

    # 5.1. Remove any spaces from the user's roll
    user_roll: str = user_roll.replace(" ", "").strip()

    # 6. Check if the user's roll is valid
    valid_roll: bool = helpers.is_valid_roll(user_roll)

    # 6.1 If the user's roll is not valid, send a message to the user
    if not valid_roll:
        await context.respond(f"Invalid roll: {user_roll}.\nPlease enter a valid roll like 1d20, 2d6, or 3d20 + 6.")
        return None
    print("This is a valid roll")


    # Parse the user's roll since it is valid
    calculated_roll: list[int] = helpers.parse_dice_roll(user_roll)
    print(f"Total result: {calculated_roll}")
    await context.respond(f"[{user_roll}]={calculated_roll}")
# ========== END BOT ==========

if __name__ == "__main__":
    # 2. Pass Discord api token to bot (wrap in try/catch block to be safe)
    try:
        # 2.1. The Bot run command will actually start up the discord bot lifecycle
        discord_bot.run(config.DISCORD_TOKEN)
    except RuntimeError as run_err:
        print(run_err)
