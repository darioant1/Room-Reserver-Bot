# UCF Library Room Reservation Bot

A Discord-integrated automation bot that uses Selenium to automatically reserve library study rooms at the University of Central Florida (UCF) based on availability within a preferred time window.

Created by Dario Antonio | [GitHub Profile](https://github.com/darioant1)

---

## Features

-  Automates room reservations at [UCF’s LibCal system](https://ucf.libcal.com/reserve/largestudyrooms)
-  Filters room availability for specific time ranges (e.g., 3 PM to 7 PM)
-  Handles login prompts, form submissions, and dropdown selections
-  Integrates with Discord using `discord.py` to reserve rooms via `!reserve` command
-  Written in Python using `selenium` and `discord.py`

---

## File Structure

├── bot.py # Discord bot integration
├── selenium_reserver.py # Selenium logic to automate room reservations

---

## Setup Instructions

### 1. Install Dependencies

pip install selenium discord.py
Make sure you have ChromeDriver installed and added to your system PATH.

2. Configure Credentials
Replace placeholders in bot.py:

email = 'your_email@ucf.edu'
password = 'your_password'
PID = 'your_UCF_ID'
groupName = 'Your Group Name'

Also, insert your actual Discord bot token into:

TOKEN = 'your_token_here'

How It Works
A user sends !reserve in a Discord channel.

The bot triggers reserve_library_room() from selenium_reserver.py.

Selenium automates the LibCal reservation page:

Selects a time slot

Logs in with NID credentials

Fills out group name, PID, and status

Submits the reservation

The bot confirms the reservation in Discord.

Security Notice
Never hard-code your actual credentials in public repositories. Use environment variables or a .env file with something like python-dotenv for safer credential handling.

Future Improvements
Add time preference customization via command arguments

Support for multiple campuses or libraries

Enhanced error handling and retry logic

Shift credentials to secure .env loading
