# discord_bot.py:jeff
#

import os
import re
import requests
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Source any .env found in this directory where this script is located.
load_dotenv()

DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1")
EXPERIMENTAL = os.getenv("EXPERIMENTAL", "False").lower() in ("true", "1")
SUPPRESS_EMBED = os.getenv("SUPPRESS_EMBED", "False").lower() in ("true", "1")
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN", "")

# Regex pattern to detect standard, short, and shorts YouTube links
YOUTUBE_REGEX = r'(https?://(?:www\.)?youtube\.com/watch\?v=[\w-]+|https?://youtu\.be/[\w-]+|https?://(?:www\.)?youtube\.com/shorts/[\w-]+)'

OEMBED_API_BASE_URL: str = "https://www.youtube.com/oembed"
OEMBED_API_FORMAT: str = "json"

# Setup bot intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

if DEBUG:
    print(f'DEBUG: {DEBUG}')
    print(f'EXPERIMENTAL: {EXPERIMENTAL}')
    print(f'SUPPRESS_EMBED: {SUPPRESS_EMBED}')

def get_youtube_metadata(url) -> dict:
    """Fetches the video metadata using YouTube's oEmbed API with exception handling."""
    result: dict = {
        'title': 'Unknown title',
        'author_name': 'Unknown author',
        #'thumbnail_url': "",
    }
    final_api_url: str = f'{OEMBED_API_BASE_URL}?url={url}&format={OEMBED_API_FORMAT}'
    if DEBUG:
        print(f'final_api_url: {final_api_url}')

    try:
        response = requests.get(final_api_url, timeout=5)
        # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        response.raise_for_status()
        res = response.json()

        result["title"] = res.get("title", "Unknown title")
        result["author_name"] = res.get("author_name", "Unknown author")
        #if bool(EXPERIMENTAL) == True:
            #result["thumbnail_url"] = res.get("thumbnail_url", "")
        return result
    except requests.exceptions.RequestException as e:
        print(f"Error fetching YouTube title for {url}: {e}")
        return None
    except (ValueError, KeyError) as e:
        print(f"Error parsing API response for {url}: {e}")
        return None

def split_response_lines(lines, limit=1900) -> list:
    """Chunks a list of lines into chunks that stay safely under the character limit."""
    chunks = []
    current_chunk = []
    current_length = 0

    for line in lines:
        # +1 accounts for the newline character added during joining
        if current_length + len(line) + 1 > limit:
            chunks.append("\n".join(current_chunk))
            current_chunk = [line]
            current_length = len(line)
        else:
            current_chunk.append(line)
            current_length += len(line) + 1

    if current_chunk:
        chunks.append("\n".join(current_chunk))

    return chunks

@bot.event
async def on_ready():
    print(f'Bot is logged in as {bot.user.name} ({bot.user.id})')
    print('Listening for YouTube links...')

@bot.event
async def on_message(message):
    # Ignore messages sent by the bot itself to prevent infinite loops
    if message.author == bot.user:
        return

    # Find ALL occurrences of YouTube links in the message text
    matches = list(re.finditer(YOUTUBE_REGEX, message.content))

    if matches:
        # Optional: Suppress original link embeds to keep chat clean
        if SUPPRESS_EMBED:
            try:
                await message.edit(suppress=True)
            except discord.Forbidden:
                pass

        response_lines = []

        # Process each hyperlink found in the message
        for response_counter, match in enumerate(matches, start=1):
            youtube_url = match.group(0)
            res = get_youtube_metadata(youtube_url)

            # Format to Discord Markdown: [Title](URL)
            # '<' and '>' prevent Discord from creating default massive embeds
            # for every link
            if res and res.get("title"):
                title = res["title"]
                author = res.get("author_name", "")
                author_str = f" - by {author}" if author else ""
                markdown_link = f"{response_counter}. [{title}]({youtube_url}){author_str}"
            else:
                markdown_link = f"{response_counter}. [Could not fetch title]({youtube_url})"
            # Discord does not render Markdown image syntax, nor does it
            # allow image tags to be rendered in a channel.
            #if bool(EXPERIMENTAL) == True:
            #    if res and res["thumbnail_url"] and len(res["thumbnail_url"]) > 0:
            #        markdown_link += "\n"
            #        markdown_link += f"![Thumbnail]({res["thumbnail_url"]})"
            #    else:
            #        # Fallback if the title couldn't be fetched due to an API error
            #        response_lines.append(f"{response_counter}. [Could not fetch thumbnail)](<{youtube_url}>)")

            response_lines.append(markdown_link)

        # Final phase of processing: send the response lines back to the
        # channel in a single message
        if response_lines:
            # Split lines into chunks under 1900 characters to be completely
            # safe
            message_chunks = split_response_lines(response_lines, limit=1900)
            # Send the chunks out sequentially
            for index, chunk in enumerate(message_chunks):
                if DEBUG:
                    print(f"Sending chunk {index + 1}:\n{chunk}")

                # Use standard reply for the first chunk, and normal channel
                # sends for overflows
                if index == 0:
                    await message.reply(chunk, mention_author=False)
                else:
                    await message.channel.send(chunk)

    # Crucial to let other bot commands function normally
    await bot.process_commands(message)

if __name__ == "__main__":
    if len(DISCORD_BOT_TOKEN) < 1:
        print("ERROR: DISCORD_BOT_TOKEN is not set. Please set it in the .env file.")
    else:
        bot.run(DISCORD_BOT_TOKEN)
