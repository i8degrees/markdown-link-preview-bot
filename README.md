---
---

# markdown-link-preview-bot

![avatar](src/images/avatar.png)

A Discord bot that generates clean Markdown link previews for YouTube videos
that are shared in channels or DMs by extracting the title and author name
from each link. Here is an example:

After pasting the following two links to a channel (where this bot is active at):

```
https://www.youtube.com/watch?v=jEWFSv3ivTg
https://www.youtube.com/watch?v=YN7X0NfxjPc
```

The result is:

```markdown
1. [Draw fewer tiles - by using a Dual-Grid system!](https://www.youtube.com/watch?v=jEWFSv3ivTg) - by jess::codes
2. [Modular Isometric Pixel Art | Tutorial](https://www.youtube.com/watch?v=YN7X0NfxjPc) - by Brandon James Greer
```

Response messages that exceed `1,900` characters will be automatically chunked
into multiple messages. All known YouTube formats are accepted, such as
shorts, reels and standard notation.

## inspiration

This is useful for those of us that prefer disabling **Show embeds and link previews**
in our Discord client. I made an attempt at including the rendered
thumbnail URL at the end of each link, but Discord disallows this from
happening, so this is the end result of my implementation.

## usage

This project README walks you through setting up the repository, configuring
your Discord application with the required User and Guild installation
settings, enabling the necessary bot intents, and finally running the script.

### setup

**One-click installation**: Install the *markdown-link-preview-bot* Discord
bot with [one-click][0]. This requires that I am still running the bot at the
time you read this and may or may not be the case.

Alternatively, there is a Docker image you can build or pull down for local
usage. [i8degrees/markdown-link-preview-bot:latest][5].

Lastly, you may run the Python script on your own machine. See XXX header
section for how to go about doing this.

### Developers

#### 1. Discord Developer Portal Configuration

##### 2. Create and Configure the Bot

1. Head to the [Discord Developer Portal](https://discord.com/developers/applications) and click **New Application**. Give it a name and click **Create**.

2. Navigate to the **Bot** tab on the left sidebar:

* Scroll down to **Privileged Gateway Intents**.
* Enable the **Message Content Intent** toggle.
* Under the bot username section, click **Reset Token** to generate a new token, then copy it. Update the `TOKEN` variable in your `discord_bot.py` script with this new token.

##### 3. Configure Installation Settings & Scopes

1. Navigate to the **Installation** tab on the left sidebar.

2. Set up the default installation settings to support both User and Guild installs:

* **Install Types**: Enable both **Guild Install** and **User Install**.

* **User Install Scope**: Select `applications.commands`.

* **Guild Install Scope**: Select `applications.commands` and `bot`.

* **Default Permissions**: Select the following required permissions:

* **View Channels**
* **Send Messages**
* **Manage Messages**

3. Copy Discord's provided installation link (bootstrap link) from the Developer Portal to install the bot to your user account or servers.

##### 4. Running the Bot

Once dependencies are installed, your token is added to the script, and the bot is installed via Discord's bootstrap link, run the bot using the virtual environment:

```shell
venv/bin/python3 src/bot
```

#### 4. Repository Setup & Dependencies

Clone the repository and set up the Python virtual environment and dependencies:

```shell
git clone https://github.com/i8degrees/markdown-link-preview-bot.git
cd markdown-link-preview-bot
python3 -m venv venv
venv/bin/pip3 install -r requirements.txt
```

Copy the distributed `.env.dist` file to `.env`.

```shell
cp -av .env.dist .env
```

Consult the `.env.dist` file for details on what and how to set each
environment variable for this bot. The absolute minimum is to fill in the
`DISCORD_BOT_TOKEN` variable with your own token, as per the guide mentioned
in this document.

#### run

```shell
venv/bin/python3 src/bot
```

## reference links

[0]: https://discord.com/oauth2/authorize?client_id=1565541323333705780

