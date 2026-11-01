---
---

# markdown-link-preview

![avatar](avatar.png)

This project README walks you through setting up the repository, configuring your Discord application with the required User and Guild installation settings, enabling the necessary bot intents, and finally running the script.

## usage

Install this Discord bot with one-click by [markdown-link-preview](https://discord.com/oauth2/authorize?client_id=1565541323333705780)

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
venv/bin/python3 discord_bot.py
```

#### 4. Repository Setup & Dependencies

Clone the repository and set up the Python virtual environment and dependencies:

```shell
git clone https://github.com/i8degrees/markdown-link-preview.git
cd markdown-link-preview
python3 -m venv venv
venv/bin/pip3 install discord.py requests
```

#### run

```shell
venv/bin/python3 discord_bot.py
```

## reference links

## scratchpad
