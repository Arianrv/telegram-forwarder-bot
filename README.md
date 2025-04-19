# Telegram Forwarder Bot

A lightweight Telegram client-based bot that automatically forwards all incoming private messages from your account to a specified private group.

Built using Telethon and designed for simplicity, reliability, and 24/7 operation.

## Features

- 📩 Automatically forwards private chat messages to a private group
- 👤 Shows original sender ("Forwarded from [username]" format)
- 🔒 Uses `.env` file for secure API configuration
- 🔄 Ready for 24/7 server deployment with systemd
- 🖥️ Easy and fast setup on any Linux server (Ubuntu recommended)

## Requirements

- Python 3.9 or higher
- A Telegram account
- `api_id` and `api_hash` from [Telegram API](https://my.telegram.org)

## Setup

1. Clone or download this repository manually.

2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate

3. Install required libraries from requirements.txt:
   ```bash
   pip install -r requirements.txt

4. Create a apiprivate.env file in the root folder with this format:
   ```bash
   api_id=YOUR_API_ID
   api_hash=YOUR_API_HASH
   target_group_id=YOUR_TARGET_GROUP_ID     # (e.g. -100123456789)

5. Run the bot:
   ```bash
   python forward.py
