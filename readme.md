# PalestineMoviesBot

PalestineMoviesBot is a Telegram bot designed to assist users in searching for movies, books, and other types of media available in the @PalestineMovies Telegram channel. Additionally, it provides subscription options, a request feature, and a way to contact the administrator(s). You can use the bot on Telegram by searching for [@PalestineMoviesBot](https://t.me/PalestineMoviesBot).

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Contributing](#contributing)

## Features

- **Search:** Find movies, books, and other media in the @PalestineMovies channel.
- **Subscription:** Receive updates about new media releases from the channel.
- **Request:** Submit requests for specific movies, books, or other media.
- **Contact:** Send messages directly to the administrator.
- **Broadcast:** Admin(s) can broadcast messages and media to all subscribers.

## Getting Started

### Prerequisites

- [Python](https://www.python.org/downloads/) (>=3.6)
- [Pyrogram](https://docs.pyrogram.org/) (for media searching)
- [python-telegram-bot](https://python-telegram-bot.readthedocs.io/) (for Telegram bot functionality)
- [Telegram API credentials](https://my.telegram.org/auth) (for pyrogram)

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/PalestineMoviesBot.git
   ```
   
3. Install the required packages:

   ```
   pip install -r requirements.txt
   ```
   
5. Create a new bot on Telegram using [BotFather](https://t.me/BotFather) and obtain the API token.
6. Create a new application on Telegram using [my.telegram.org](https://my.telegram.org/auth) and obtain the API credentials. You can use your personal Telegram account to create the application.
7. Rename `config.ini.example` to `config.ini` and fill in your bot API token, Pyrogram's API ID and API hash, and other necessary details.

## Usage

Run the bot using the following terminal command:

```
python3 main.py
```

<ins>Note</ins>: the first time you run the bot, you will need to authenticate your account using the phone number and the verification code sent to your Telegram account.

In the bot's folder you will have 6 files:
- `main.py`: the main file to run the bot.
- `localization.py`: contains the bot's messages in different languages.
- `config.ini`: contains the bot's configuration.
- `users.json`: contains the IDs of the bot's users (could be useful to broadcast really important announcements).
- `subscribers.json`: contains the IDs of the bot's subscribers.
- `palestinemoviesbot.session`: contains the Pyrogram's session (to avoid re-authenticating every time you run the bot).

## Commands

**User commands:**
- **/start**: Start the bot and get an introduction message.
- **/search**: Search for movies, books, and other media in the @PalestineMovies channel.
- **/subscribe**: Subscribe to receive updates about the project.
- **/unsubscribe**: Unsubscribe from receiving updates.
- **/request**: Request a specific movie, book, or other media.
- **/contact**: Send a message directly to the administrator.
- **/help**: Display a list of available commands and their descriptions.

**Admin commands (accessible only by the bot administrator):**
- **/reply**: Send a message to a specific user.
- **/broadcast**: Broadcast a message to all subscribers.
- **/stats**: Display the number of users and subscribers.
- **/view**: Show the built media album.
- **/broadcast_album**: Send the media album to all subscribed users.
- **/clear**: Clear the media album.
- **/superbroadcast**: Broadcast a message to all users.
- **/restart**: Restart the bot.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request, or suggest new features and improvements.

Free Palestine 🇵🇸
